from django.shortcuts import render
from rest_framework import generics,status
from .serializers import CategoriasSerializer,ProductosSerializer,proveedor_serializar
from .models import Categorias,Productos,Proveedor

#importando  la tabla users
from django.contrib.auth.models import User
import json
from django.http import HttpResponse,JsonResponse
from rest_framework.permissions import AllowAny,IsAuthenticated
#importando  la tabla tokens
from rest_framework.authtoken.models import Token

#me permite realizar la autenticacion hacia la BD
from django.contrib.auth import authenticate

# importar el decorador para realizar los metodos get,post,delete
from rest_framework.decorators import api_view

#importar la libreria para parsear los datos en JSON
from rest_framework.parsers import JSONParser

class ProductosList(generics.ListAPIView):
    #SELECT * FROM PRODUCTOS
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes=(AllowAny,)

class ProductosCreate(generics.CreateAPIView):
    #SELECT * FROM PRODUCTOS
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer    

#Vista Basada en clase  que me permitira hacer el metodo GET
class CategoriasList(generics.ListAPIView):
    #SELECT * FROM CATEGORIAS
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer    

#Vista Basada en clase  que me permitira hacer el metodo POST
class CategoriasCreate(generics.CreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer    

#Vista Basada en clase  que me permitira hacer el metodo DELETE
class CategoriasDelete(generics.DestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer  
    lookup_field="pk"

#Vista Basada en clase  que me permitira hacer el metodo UPDATE
class CategoriasUpdate(generics.UpdateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer  
    lookup_field="pk"    


#Los Siguentes Servicios permitiran dar de alta a nuevos usuario y  acceder al app

class RegistrarUsuarios(generics.CreateAPIView):
    permission_classes =(AllowAny,)

    def post(self,request):
        #recogiendo la informacion desde el front
        usuario = request.data['username']
        correo = request.data['email']
        contraseña = request.data['password']
        nom = request.data['nombre']
        ape = request.data['apellido']
        admin =request.data['staff']
        #registrandola en la base de datos 
        nuevo_usuario= User.objects.create_user(usuario,correo,contraseña)
        #especicas los demas campos que deseas grabar
        nuevo_usuario.first_name=nom
        nuevo_usuario.last_name=ape
        nuevo_usuario.is_staff=admin
        nuevo_usuario.save()
        #genero el token del usuario registrado anteriormente
        token_usuario=Token.objects.create(user=nuevo_usuario)
        msg={'detail':'Usuario Creado Correctamente con el Token' +token_usuario.key}
        #convierte la cade de texto msg a Json
        rpta=json.dumps(msg)
        return HttpResponse(rpta,content_type='application/json')


class LoginUsuario(generics.CreateAPIView):
        
        def post(self,request):
            usuario = request.data["username"]
            contraseña= request.data["password"]
            usuario =authenticate(username=usuario,password=contraseña)
            if usuario:
                token_usuario=Token.objects.get(user_id=usuario.id)
                msg ={
                    "nombre" :usuario.first_name,
                    "apellido" :usuario.last_name,
                    "correo" :usuario.email,
                    "key":token_usuario.key
                }
            else:
                 msg={'error':'Credenciales Invalidas'}
            rpta=json.dumps(msg)
            return HttpResponse(rpta,content_type='application/json')     

#Crear un servicio que me permita relaizar el GET,POST,DELETE
@api_view(['GET','POST'])
def prove_ser_full(request):
    if request.method=='GET':
        #SELECT * FROM PROVEEDOR
        proveedores=Proveedor.objects.all()
    elif request.method =='POST':
        provee_data = JSONParser().parse(request)
        provee_serializer=proveedor_serializar(data=provee_data)
        if provee_serializer.is_valid():
            provee_serializer.save()
            return JsonResponse(provee_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(provee_serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    provee_serializer=proveedor_serializar(proveedores,many=True) 
    return JsonResponse(provee_serializer.data,safe=False)

#Crear un servicio que me permita relaizar el GET DETalle
@api_view(['GET','DELETE','PUT'])
def prove_ser_detail(request,pk):
    #seleccionado el proveedor que mostrare en el detalle
    proveedor=Proveedor.objects.get(id=pk)
    if request.method == 'GET':
        #SELECT * FROM PROVEEDOR WHERE ID=PK
        provee_serializer=proveedor_serializar(proveedor) 
        return JsonResponse(provee_serializer.data)
    elif request.method=='DELETE':
        proveedor.delete()
        return JsonResponse({'Message':'El Proveedor se elimino con exito'},status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        provee_data = JSONParser().parse(request)
        provee_serializer=proveedor_serializar(proveedor,data=provee_data)
        if provee_serializer.is_valid():
            provee_serializer.save()
            return JsonResponse(provee_serializer.data)
        return JsonResponse(provee_serializer.errors,status=status.HTTP_400_BAD_REQUEST)  









    
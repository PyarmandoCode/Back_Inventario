from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriasSerializer,ProductosSerializer
from .models import Categorias,Productos

#importando  la tabla users
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
from rest_framework.permissions import AllowAny,IsAuthenticated
#importando  la tabla tokens
from rest_framework.authtoken.models import Token

# Create your views here.

class ProductosList(generics.ListAPIView):
    #SELECT * FROM PRODUCTOS
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

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

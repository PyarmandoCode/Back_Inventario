from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriasSerializer,ProductosSerializer
from .models import Categorias,Productos

# Create your views here.

class ProductosList(generics.ListAPIView):
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


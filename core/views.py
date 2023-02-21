from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriasSerializer,ProductosSerializer
from .models import Categorias,Productos

# Create your views here.

class ProductosList(generics.ListAPIView):
    #SELECT * FROM PRODUCTOS
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
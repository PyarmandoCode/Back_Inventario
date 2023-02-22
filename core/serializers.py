from .models import Categorias,Productos,Proveedor
from rest_framework import serializers


#Serializar es convertir informacion de la BD 
#a codigo de PYTHON

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ('id','categoria_nombre','categoria_estado')

class proveedor_serializar(serializers.ModelSerializer):
    class Meta:
        model=Proveedor
        fields = '__all__'



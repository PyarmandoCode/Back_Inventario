from django.db import models

class Categorias(models.Model):
    categorias_opciones=(
        ('COMPUTO','COMPUTO'),
        ('HOGAR','HOGAR'),
        ('ENTRETENIMIENTO','ENTRETENIMIENTO'),
        ('PRODUCTOS BELLEZA','PRODUCTOS BELLEZA')
    )
    categoria_nombre=models.CharField(max_length=90,choices=categorias_opciones)
    categoria_estado=models.BooleanField(default=True)

    def __str__(self):
        return self.categoria_nombre 

class Proveedor(models.Model):
    proveedor_nombre=models.CharField(max_length=90)       
    proveedor_estado=models.BooleanField(default=True)

    def __str__(self):
        return self.proveedor_nombre        

class Productos(models.Model):
    producto_nombre=models.CharField(max_length=100)
    producto_descripcion=models.TextField(blank=True,null=True)
    producto_imagen=models.CharField(max_length=120,blank=True,null=True)
    producto_precio=models.DecimalField(max_digits=7,decimal_places=2)
    producto_estado=models.BooleanField(default=True)
    producto_stock=models.IntegerField()
    categoria=models.ForeignKey(Categorias,on_delete=models.CASCADE)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.producto_nombre







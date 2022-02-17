from django.db import models

# Create your models here.
class categoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        #db_table = ''
        #managed = True
        verbose_name = 'categoriaProducto'
        verbose_name_plural = 'categoriasProductos'
    
    def __str__(self):
        return self.nombre

class Productos(models.Model):
    descripcion=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='productos', null = True, blank= True)
    categorias=models.ForeignKey(categoriaProd, on_delete=models.CASCADE) 
    precio=models.FloatField()
    existencia=models.IntegerField()
    disponible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        #db_table = ''
        #managed = True
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return self.descripcion
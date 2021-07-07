from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=64)

    def __str__(self):
        return f" ({self.categoria})"


""" Producto_categoria={
    (0,'Categoria'),
    (1,'Bebidas'),
    (2,'Comestibles'),
    (3,'Varios')
} """

class Producto(models.Model):
    Nombre=models.CharField(max_length=20)
    categoria=models.ForeignKey(
        Categoria,on_delete=models.CASCADE
    )
    descripcion=models.TextField(max_length=100)
    imagen=models.ImageField(upload_to="productos",null=True)
    precio=models.IntegerField()

    def __str__(self):
        return f"{self.Nombre} {self.categoria}"


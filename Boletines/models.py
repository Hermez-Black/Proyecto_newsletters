from django.db import models

# Create your models here.
class Boletin(models.Model):
    nombre = models.CharField(max_length=400)
    descripcion = models.TextField()
    imagen = models.ImageField()
    objetivo = models.IntegerField()
    frecuencia = models.IntegerField()
    fecha_de_creacion = models.DateField()
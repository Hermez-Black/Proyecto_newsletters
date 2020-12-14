from django.db import models
from Categorias.models import Categoria
# Create your models here.
class Boletin(models.Model):
    nombre = models.CharField(max_length=400)
    descripcion = models.TextField()
    imagen = models.ImageField()
    objetivo = models.IntegerField()
    frecuencia = models.IntegerField()
    fecha_de_creacion = models.DateField()

    categorias = models.OneToOneField(Categoria, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
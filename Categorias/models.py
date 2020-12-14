from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=700)
    fecha_de_creacion = models.DateField()
    def __str__(self):
        return self.nombre
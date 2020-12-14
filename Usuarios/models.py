from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    correo = models.EmailField(max_length=200)
    contraseña = models.CharField(max_length=200)
    def __str__(self):
        return self.nombres
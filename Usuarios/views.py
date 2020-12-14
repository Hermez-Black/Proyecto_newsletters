from django.shortcuts import render
from Usuarios.models import Usuario
from Usuarios.serializers import UsuarioSerializer
from rest_framework import viewsets, status
# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
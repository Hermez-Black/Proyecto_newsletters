from django.shortcuts import render
from Categorias.models import Categoria
from Categorias.serializers import CategoriaSerializer
from rest_framework import viewsets, status
# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
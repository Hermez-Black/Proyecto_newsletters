from django.shortcuts import render
from Boletines.models import Boletin
from Boletines.serializers import BoletinSerializer
from rest_framework import viewsets, status
# Create your views here.
class BoletinViewSet(viewsets.ModelViewSet):
    queryset = Boletin.objects.all()
    serializer_class = BoletinSerializer
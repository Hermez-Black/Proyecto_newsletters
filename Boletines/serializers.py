from rest_framework import serializers
from Boletines.models import Boletin

class BoletinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletin
        fields = '__all__'
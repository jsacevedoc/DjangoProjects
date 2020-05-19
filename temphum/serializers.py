from rest_framework import serializers
from .models import Temphum

from .models import Cultivo

class TemphumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temphum
        fields = ('id', 'type', 'value')

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = ('id', 'codigo', 'latitud', 'longitud', 'producto', 'area') 
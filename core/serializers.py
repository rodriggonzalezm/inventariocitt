from rest_framework import serializers
from .models import Cortinas

class CortinasSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Cortinas
        fields = ['nombre', 'ancho', 'alto', 'direccion', 'numerotelefono', 'imagen']
from django import forms
from django.forms import ModelForm
from .models import Cortinas

class CortinasForm(ModelForm):

    class Meta:
        model = Cortinas
        fields = ['nombre', 'ancho', 'alto', 'direccion', 'numerotelefono']
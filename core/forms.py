from django import forms
from django.forms import ModelForm
from .models import Cortinas
from django.contrib.auth.forms import UserCreationForm
class CortinasForm(ModelForm):

    class Meta:
        model = Cortinas
        fields = ['nombre', 'ancho', 'alto', 'direccion', 'numerotelefono']

class CustomUserForm(UserCreationForm):
    pass
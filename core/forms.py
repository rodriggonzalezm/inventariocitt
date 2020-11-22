from django import forms
from django.forms import ModelForm
from .models import Cortinas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CortinasForm(ModelForm):

    class Meta:
        model = Cortinas
        fields = ['nombre', 'ancho', 'alto', 'direccion', 'numerotelefono']

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password1', 'password2' 
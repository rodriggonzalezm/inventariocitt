from django.shortcuts import render, redirect
from .models import Cortinas
from .forms import CortinasForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login as dj_login
# Create your views here.

def inicio(request):

    return render(request, 'core/inicio.html')

def login(request):
    
    return render(request, 'core/login.html')

def registrar(request):
    
    return render(request, 'core/registrar.html')

def comomedir(request):
    
    return render(request, 'core/comomedir.html')

def comprar(request):
    
    return render(request, 'core/comprar.html')

def contactanos(request):
    
    return render(request, 'core/contactanos.html')

def encuentranos(request):
    
    return render(request, 'core/encuentranos.html')

def listadocortinas(request):
    cortinas = Cortinas.objects.all()
    data = {
        'cortinas':cortinas
    }
    return render(request, 'core/listadocortinas.html', data)

@login_required
@permission_required('core.add_cortinas')
def nuevacortina(request):

    data = {
        'form' : CortinasForm()
    }

    if request.method == 'POST':
        formulario = CortinasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"

    return render(request, 'core/nuevacortina.html', data)

@permission_required('core.change_cortinas')
def modificarcortina(request, id):
    cortinas = Cortinas.objects.get(id=id)
    data = {
        'form':CortinasForm(instance=cortinas)
    }

    if request.method == 'POST':
        formulario = CortinasForm(data=request.POST, instance=cortinas)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data ["form"] = formulario

    return render(request, 'core/modificarcortina.html', data)
@permission_required('core.delete_cortinas')
def eliminarcortinas(request, id):
    cortinas = Cortinas.objects.get(id=id)
    cortinas.delete()

    return redirect(to="listadocortinas")

def registrousuario(request):
    data = {
        'form':CustomUserForm
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            dj_login(request, user)
            return redirect(to="inicio")

    return render(request, 'registration/registrar.html', data)



from django.shortcuts import render, redirect
from .models import Cortinas
from .forms import CortinasForm
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
    return render(request, 'core/listadocortinas.html')

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

def modificarcortina(request, id):

    cortinas = Cortinas.objects.get(id=id)
    data = {
        'form':CortinasForm(instance=cortinas)
    }

    if request.method == 'POST':
        formulario = CortinasForm(instance=cortinas)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data ["form"] = formulario



    return render(request, 'core/modificarcortina.html', data)

def eliminarcortinas(request, id):

    cortinas = Cortinas.objects.get(id=id)
    cortinas.delete()

    return redirect(to="listadocortinas")



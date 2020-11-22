from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=500)
    nombres = models.CharField(max_length=500)
    apellidos = models.CharField(max_length=500)
    direccion = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=500)
    nrocontacto = models.IntegerField()

    def __str__(self):
        return self.rut



class Cortinas (models.Model):
    Nombre = models.CharField(max_length=500)
    Ancho = models.IntegerField()
    Alto = models.IntegerField()
    Direccion = models.CharField(max_length=500)
    NumeroTelefono = models.IntegerField()
    

    def __str__(self):
        return self.Nombre




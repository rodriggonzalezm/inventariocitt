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
    nombre = models.CharField(max_length=500)
    ancho = models.IntegerField()
    alto = models.IntegerField()
    direccion = models.CharField(max_length=500)
    numerotelefono = models.IntegerField()
    

    def __str__(self):
        return self.nombre




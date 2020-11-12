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
    ancho = models.IntegerField()
    alto = models.IntegerField()
    rut = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __integer__(self):
        return self.rut




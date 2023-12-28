from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.DecimalField(max_digits=10, decimal_places=0)

class DatosDeContacto(models.Model):
    telefono = models.DecimalField(max_digits=12, decimal_places=0)
    email = models.EmailField()
    direccion = models.TextField(200)

class Intereses(models.Model):
    autos = models.BooleanField()
    animales = models.BooleanField()
    medioambiente = models.BooleanField()
    viajes = models.BooleanField()
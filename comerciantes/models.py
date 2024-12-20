from django.db import models

# Create your models here.

class Comerciante(models.Model):
    rut = models.TextField(max_length=12)
    razonsocial = models.TextField(max_length=100)
    giro = models.TextField(max_length=100)
    comuna = models.TextField(max_length=50)
    direccion = models.TextField(max_length=100)
    numeroventas = models.IntegerField(null=False)
    estado = models.TextField(max_length=1)
    
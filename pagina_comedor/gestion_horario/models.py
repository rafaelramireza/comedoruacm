from enum import auto
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Horario(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    horario_inicial=models.DateField()
    horario_final=models.DateTimeField()

class Platillo(models.Model):
    id=models.BigAutoField(primary_ke=y=True)
    nombre= models.CharField(max_length=30)
    tipo=models.ForeignKey(Horario: id)
class menu(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    plato=models.ForeignKey(Platillo:id)
    

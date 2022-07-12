from django.db import models

# Create your models here.
class personaje(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()

class mascota(models.Model):
    nombreM=models.CharField(max_length=20)
    edadM=models.IntegerField()

class auto(models.Model):
    marca=models.CharField(max_length=20)
    año=models.DateField()
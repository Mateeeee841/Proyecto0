from django.db import models

# Create your models here.
#los models son clases que generaran objetos mas adelante
class persona(models.Model):
    nombre=models.CharField(max_length=60)      #CharField es para textos
    edad=models.IntegerField()                  #IntegerField() es para numeros
    nacimiento=models.DateField()               #DateField() es para fechas

class auto(models.Model):
    marca=models.CharField(max_length=40)
    velocidad=models.IntegerField()
    email=models.EmailField()
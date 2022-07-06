from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader   

# Create your views here.
def mostrar_inicio(request):
    context={}
    plantilla=loader.get_template("home.html")  
    documento= plantilla.render (context)    
    return HttpResponse(documento)
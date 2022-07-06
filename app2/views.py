from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader             
from .models import pokemons 
# Create your views here.
def crear_pokemon1(request):
    if request.GET:
        name2=str(request.GET["name2"])
        tipo2=str(request.GET["tipo2"])
        lvl2=int(request.GET["lvl2"])
        creation2=str(request.GET["creation2"])
        pokemon1=pokemons(name=name2,tipo=tipo2,lvl=lvl2,creation=creation2)
        pokemon1.save()
    
    info=pokemons.objects.all()
    context={"pokemons":info}

    plantilla=loader.get_template("poke.html")
    documento=plantilla.render(context)
    return HttpResponse(documento)
    
def show(request):

    info=pokemons.objects.all()
    context={"pokemons":info}
    plantilla=loader.get_template("list.html")
    documento=plantilla.render(context)
    return HttpResponse(documento)

def mostrar(request):
    context={}
    plantilla=loader.get_template("index2.html")
    documento=plantilla.render(context)
    return HttpResponse(documento)
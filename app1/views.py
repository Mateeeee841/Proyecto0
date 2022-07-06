from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from django.template import loader              #el loader
from .models import persona, auto                        #Importo de models la clase que crea objetos

# Create your views here.
def saludo(request,nombre):
    return HttpResponse(f"hola {nombre.capitalize()}")

def horario(request):
    horayfecha_actual=datetime.now()
    hora_actual=horayfecha_actual.time()
    fecha_actual=horayfecha_actual.date()
    return HttpResponse(f"Son las: {hora_actual} del {fecha_actual} ")

def mostrar(request):
    context={"imc":0}
    if request.GET:
        altura=float(request.GET["altura"])
        peso=float(request.GET["peso"])
        context["imc"]=peso/altura**2
        
    plantilla=loader.get_template("index.html")
    documento= plantilla.render (context)
    return HttpResponse(documento)

def crear_persona1(request):
    persona1=persona(nombre="Mateo",edad=19,nacimiento="2003-03-03")            #el persona() es la clase que cree en el models
    persona1.save()
    return HttpResponse("Cargado con exito")

def crear_persona2(request):
    if request.GET:                             #el get se usa para tomar los datos del formulario
        nombre2=str(request.GET["nombre2"])     #le asigno variables a los datos que tomo del formulario
        edad2=int(request.GET["edad2"])
        nacimiento2=str(request.GET["nacimiento2"])
        persona2=persona(nombre=nombre2,edad=edad2,nacimiento=nacimiento2) #creo las clases apartir de los datos que tome y de la clase del models
        persona2.save()         #Guardo la persona creada

    info=persona.objects.all()                  #Guarda los objetos de la clase persona en info
    context={"persona":info}                    #le asigna el alias persona a info

    plantilla=loader.get_template("personas.html")      #Me trae lo del personas.html 
    documento= plantilla.render (context)             #la funcion render() toma el archivo que le doy y se lo muestra al usuario
    return HttpResponse(documento)             #HttpResponse(lo_que_quiera_ver_en_la_pagina)
    
def lista_autos(request):           #el request y el get es una solicutud para obtener un dato
    if request.GET:
        marca2=str(request.GET["marca"])           #request.GET["marca"]) aqui adentro colocamos el modelo
        velocidad2=int(request.GET["velocidad"])
        email2=str(request.GET["email"])
        auto4=auto(marca=marca2,velocidad=velocidad2,email=email2)
        auto4.save()

    info=auto.objects.all()                  #Guarda los objetos de auto en info
    context={"autos":info}                    #le asigna el alias persona a info
    plantilla=loader.get_template("listauto.html")      #interpreta el nombre_script.html 
    documento= plantilla.render (context)             #la funcion render() toma el context y lo mustra de manera grafica lo puede hacer gracias al plantilla
    return HttpResponse(documento)   
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import personaje,mascota,auto
from .forms import crearPersonaje,crearMascota,crearAuto
# Create your views here.
def ver_inicio(request):
    context={}
    plantilla=loader.get_template("inicio.html")
    documento=plantilla.render(context)
    return HttpResponse(documento)

def mostrar_base(request):
    context={}
    plantilla=loader.get_template("base.html")      
    documento= plantilla.render (context)            
    return HttpResponse(documento) 

def ver_lista(request):
    if request.GET:
        buscador=request.GET["buscador"]
        info4=personaje.objects.filter(nombre__icontains=buscador)
        info5=mascota.objects.filter(nombreM__icontains=buscador)
        info6=auto.objects.filter(marca__icontains=buscador)
        info=personaje.objects.all()
        info2=mascota.objects.all()
        info3=auto.objects.all()
        context={"personaje":info,"mascota":info2,"auto":info3,"personajes":info4,"mascotas":info5,"autos":info6}
        plantilla=loader.get_template("lista.html")      
        documento= plantilla.render (context)            
        return HttpResponse(documento)  
        

    info=personaje.objects.all()
    info2=mascota.objects.all()
    info3=auto.objects.all()
    context={"personaje":info,"mascota":info2,"auto":info3}
    plantilla=loader.get_template("lista.html")
    documento=plantilla.render(context)
    return HttpResponse(documento)


def personaje_form(request):
     if request.method=="POST":
         personaje_formulario = crearPersonaje(request.POST)
         print(personaje_formulario)
         
         if personaje_formulario.is_valid:
             datos = personaje_formulario.cleaned_data
             personajes=personaje(nombre=datos["nombre"],edad=datos["edad"])
             personajes.save()
             return render(request,"menu.html",{"mensaje":"Sumbit exitoso!!"})

     else:
             personaje_formulario=crearPersonaje()

     return render(request,"personaje_formulario.html",{"personaje_formulario":personaje_formulario})

def mascota_form(request):
     if request.method=="POST":
         mascota_formulario = crearMascota(request.POST)
         print(mascota_formulario)
         
         if mascota_formulario.is_valid:
             datos = mascota_formulario.cleaned_data
             mascotas=mascota(nombreM=datos["nombreM"],edadM=datos["edadM"])
             mascotas.save()
             return render(request,"menu.html",{"mensaje":"Sumbit exitoso!!"})

     else:
             mascota_formulario=crearMascota()

     return render(request,"mascota_form.html",{"mascota_formulario":mascota_formulario})
    
def auto_form(request):
     if request.method=="POST":
         auto_formulario = crearAuto(request.POST)
         print(auto_formulario)
         
         if auto_formulario.is_valid:
             datos = auto_formulario.cleaned_data
             autos=auto(marca=datos["marca"],año=datos["año"])
             autos.save()
             return render(request,"menu.html",{"mensaje":"Sumbit exitoso!!"})

     else:
             auto_formulario=crearAuto()

     return render(request,"auto_form.html",{"auto_formulario":auto_formulario})
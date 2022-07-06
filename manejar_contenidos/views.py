from django.shortcuts import render

# Create your views here.
def mostrar_templates(request):
    return render(request, "manejar_contenidos\home.html",{})

def mostrar_profile(request):
    return render(request, "manejar_contenidos\profile.html",{})

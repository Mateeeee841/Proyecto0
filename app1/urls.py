from django.urls import path
from . import views                                 #importo las views dentro de este script
urlpatterns =[
    path("saludar/persona/<nombre>",views.saludo),    #/saludar/persona/mateo
    path("hora/",views.horario),                      #/hora
    path("pers/",views.mostrar),                       
    path("persona/",views.crear_persona1),
    path("crear/",views.crear_persona2),
    path("autos/",views.lista_autos)
]

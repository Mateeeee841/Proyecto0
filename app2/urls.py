from django.urls import path
from . import views                                 #importo las views dentro de este script

urlpatterns =[
    path("pokemons/",views.crear_pokemon1,name="volver"),       #el name= es para asignar botones
    path("pokelist/",views.show,name="CUALQUIER"),
    path("modelo/",views.mostrar)
]
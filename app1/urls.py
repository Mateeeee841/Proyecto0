from django.urls import path
from . import views 
urlpatterns =[
    path("base/",views.mostrar_base),
    path("inicio/",views.ver_inicio,name="inicio"),
    path("objetos/",views.ver_lista,name="lista"),
    path("personaje/",views.personaje_form,name="form"),
    path("mascota/",views.mascota_form,name="formM"),
    path("auto/",views.auto_form,name="formA"),
]
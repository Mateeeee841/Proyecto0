from django.urls import path
from . import views   
urlpatterns =[
    path("home/",views.mostrar_templates,name="home"),
    path("profile/",views.mostrar_profile,name="profile")
]
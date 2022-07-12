from django.contrib import admin
from .models import personaje,mascota,auto
# Register your models here.
admin.site.register(personaje)

admin.site.register(mascota)

admin.site.register(auto)
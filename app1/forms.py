from django import forms

class crearPersonaje(forms.Form):
    nombre= forms.CharField(required=True)      #El required hace que el usuario si o si tenga que completar el campo
    edad= forms.IntegerField(required=True)

class crearMascota(forms.Form):
    nombreM= forms.CharField(required=True)   
    edadM= forms.IntegerField(required=True)

class crearAuto(forms.Form):
    marca= forms.CharField(required=True)   
    año= forms.DateField(required=True)

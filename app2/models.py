from django.db import models
# Create your models here.
class pokemons(models.Model):
    name=models.CharField(max_length=20)
    tipo=models.CharField(max_length=40)
    lvl=models.IntegerField()
    creation=models.DateField()

#con esto voy a ver el name de los pokemons en el django admin de la pagina
    def __str__(self):              
        return f"{self.name} {self.lvl}"
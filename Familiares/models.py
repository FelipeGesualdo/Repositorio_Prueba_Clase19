from django.db import models

class Familiares(models.Model):
    nombre=models.CharField(max_length=90)
    edad=models.IntegerField()
    nacimiento=models.IntegerField()
    def __str__(self):
        return f"Soy {self.nombre}, tengo {self.edad} y naci en {self.nacimiento}"

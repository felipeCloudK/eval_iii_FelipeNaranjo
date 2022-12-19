from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    anio_creacuin = models.DateField()
    campeon = models.BooleanField()

class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    dorsal = models.CharField(max_length=50)


# CMD :  python manage.py makemigrations mundial_app
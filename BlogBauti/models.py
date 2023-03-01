from django.db import models

class Pelicula(models.Model):
    nombre_pelicula = models.CharField(max_length=40)
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=30)
    descripcion_corta = models.CharField(max_length=200)

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.EmailField()
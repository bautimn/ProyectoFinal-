from django.db import models
from django.contrib.auth.models import User

class Pelicula(models.Model):
    nombre_pelicula = models.CharField(max_length=40)
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=30)
    descripcion_corta = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_pelicula 

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.EmailField()

    def __str__(self):
        return self.nombre + ' - ' + self.mail
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True, default='DEFAULT.png')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Avatares'
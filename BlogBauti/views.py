from django.shortcuts import render
from django.http import HttpResponse

from BlogBauti.models import Usuario

def usuario(self):

    usuario = Usuario(nombre='BautiMoreno', mail='bautiistam10@outlook.com')
    usuario.save()
    respuesta = f'Usuario: {usuario.nombre}, mail: {usuario.mail}'

    return HttpResponse(respuesta)
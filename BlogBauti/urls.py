from django.urls import path
from django.contrib.auth.views import LogoutView

from BlogBauti import views

urlpatterns = [

    path('', views.inicio, name='blogbauti'),
    path('usuario/', views.usuarios, name='usuarios'),
    path('pedido-peliculas/', views.pedidopeliculas, name='pedido-peliculas'),
    path('listado-peliculas/', views.buscar_pelicula,  name='listado-peliculas'),
    path('buscar/', views.buscar, name='buscar'),
    path('formulario-peliculas/', views.pelicula_formulario, name='formulario-peliculas'),
    path('leer-peliculas/', views.leer_peliculas, name='leer-peliculas'),
    path('eliminar-pelicula/<pelicula_id>', views.eliminar_peliculas, name='eliminar-pelicula'),
    path('editar-pelicula/<pelicula_id>', views.editar_pelicula, name='editar-pelicula'),
    path('login', views.login_request, name = 'login'),
    path('registro', views.register, name = 'registro'),
    path('logout', LogoutView.as_view(template_name='BlogBauti/logout.html'), name = 'logout'),
    path('editar-perfil/', views.editar_perfil, name='editar-perfil'),
    path('agregar-avatar/', views.agregar_avatar, name='agregar-avatar'),
    ]
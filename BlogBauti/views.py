from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .forms import FormularioPeliculas, MyUserCreationForm, UserEditForm, AvatarFormulario
from .models import Pelicula

def inicio(request):
    return render(request, 'BlogBauti/inicio.html')

def usuarios(request):
    return render(request, 'BlogBauti/usuarios.html')

def pedidopeliculas(request):
    return render(request, 'BlogBauti/pedido-peliculas.html')

def pelicula_formulario(request):

    if request.method == 'POST':
        mi_formulario = FormularioPeliculas(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            nueva_pelicula = Pelicula(nombre_pelicula = informacion['nombre_pelicula'], 
                                      fecha_estreno =informacion['fecha_estreno'], 
                                      genero = informacion['genero'], 
                                      descripcion_corta = informacion['descripcion_corta'])
            nueva_pelicula.save()
            return redirect('/blogbauti/')

    else:    
        mi_formulario = FormularioPeliculas()
    
    return render(request, 'BlogBauti/formulario-peliculas.html', {'formulario_peliculas': mi_formulario})
    

def buscar_pelicula(request):
    return render(request, 'BlogBauti/listado-peliculas.html')

def buscar(request):

    if request.GET['nombre_pelicula']:
        pelicula_busqueda = request.GET['nombre_pelicula']
        resultado = Pelicula.objects.filter(nombre_pelicula__icontains = pelicula_busqueda)

        return render(request, 'BlogBauti/resultados-busqueda.html', {'pelicula': pelicula_busqueda, 'nombre_pelicula': pelicula_busqueda})

    else:
        respuesta = 'No se encuentra esa película.'

    return HttpResponse(respuesta)

def leer_peliculas(request):
    peliculas = Pelicula.objects.all()
    contexto = {"peliculas": peliculas}
    return render(request, 'BlogBauti/leer-peliculas.html', contexto)

def eliminar_peliculas(request, pelicula_id):
    pelicula = Pelicula.objects.get(id = pelicula_id)
    pelicula.delete()

    peliculas = Pelicula.objects.all()

    contexto = {"peliculas": peliculas}

    return render(request, 'BlogBauti/leer-peliculas.html', contexto)

def editar_pelicula(request, pelicula_id):

    pelicula = Pelicula.objects.get(id=pelicula_id)

    if request.method == 'POST':
        mi_formulario = FormularioPeliculas(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data

            pelicula.nombre_pelicula = informacion['nombre_pelicula']
            pelicula.fecha_estreno = informacion['fecha_estreno']
            pelicula.genero = informacion['genero']
            pelicula.descripcion_corta = informacion['descripcion_corta']

            pelicula.save()

            peliculas = Pelicula.objects.all()
            contexto = {'peliculas': peliculas}

            return render(request, 'BlogBauti/leer-peliculas.html', contexto)
        
    else:
        mi_formulario = FormularioPeliculas(initial={"nombre_pelicula": pelicula.nombre_pelicula, 
                                                        "fecha_estreno": pelicula.fecha_estreno,
                                                        "genero": pelicula.genero,
                                                        "descripcion_corta": pelicula.descripcion_corta})

    contexto = {'mi_formulario': mi_formulario, 'pelicula_id': pelicula_id}

    return render(request, 'BlogBauti/leer-peliculas.html', contexto)

def login_request(request):
    
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                contexto = {'mensaje': f'Bienvenido {usuario}'}
                return render(request, 'BlogBauti/login.html', contexto)
            else:
                contexto = {'mensaje': f'El usuario no existe.', 'form': form}
                return render(request, 'BlogBauti/login.html', contexto)
        else:
            contexto = {'mensaje': f'Ese usuario no existe.', 'form': form}
            return render(request, 'BlogBauti/login.html', contexto)

    contexto = {'form': form}    
    return render(request, 'BlogBauti/login.html', contexto)

def register(request):

    if request.method == 'POST':
        #form=UserCreationForm(request.POST)
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            contexto = {'mensaje': 'Usuario creado satisfactoriamente.'}
            return render(request, 'BlogBauti/inicio.html', contexto)
        
    else:
        #form = UserCreationForm()
        form = MyUserCreationForm()

        contexto = {'form': form}
        return render(request, 'BlogBauti/registro.html', contexto)
    
@login_required
def editar_perfil(request):
    usuario = User.objects.get(username=request.user)

    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']

            usuario.save()
    
    else:

        mi_formulario = UserEditForm(initial={'username': usuario.username,
                                            'email': usuario.email})
    
    return render(request, 'blogbauti/editar-perfil.html', {'mi_formulario': mi_formulario})
    
@login_required
def agregar_avatar(request):
    avatar = request.user.avatar
    mi_formulario = AvatarFormulario(instance=avatar)
     
    if request.method == 'POST':
        mi_formulario = AvatarFormulario(request.POST, request.FILES, instance=avatar)
        if mi_formulario.is_valid():
            mi_formulario.save()
        else:
            contexto = {'mi_formulario': mi_formulario}
            return render(request, 'blogbauti/agregar-avatar.html', contexto)



class PeliculaList(ListView):
    model = Pelicula
    template_name = 'blogbauti/pelicula_list.html'

class PeliculaDetalle(DetailView):
    model = Pelicula
    template_name = 'blogbauti/pelicula_detalle.html'

class PeliculaCreacion(CreateView):
    model = Pelicula
    success_url = '/blogbauti/pelicula/list'
    fields = ['nombre_pelicula', 'fecha_estreno', 'genero', 'descripcion_corta']

class PeliculaUpdate(UpdateView):
    model = Pelicula
    success_url = '/blogbauti/pelicula/list'
    fields = ['nombre_pelicula', 'fecha_estreno', 'genero', 'descripcion_corta']

class PeliculaDelete(DeleteView):
    model = Pelicula
    success_url = '/blogbauti/pelicula/list'


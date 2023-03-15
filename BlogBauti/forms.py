from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class FormularioPeliculas(forms.Form):

    nombre_pelicula = forms.CharField()
    fecha_estreno = forms.DateField()
    genero = forms.CharField() 
    descripcion_corta = forms.CharField()

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}

class UserEditForm(forms.Form):

    username = forms.CharField(label='Modificar Usuario')
    email = forms.EmailField(label='Modificar Email')

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {k: '' for k in fields}

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields='__all__'
        exclude=['user']

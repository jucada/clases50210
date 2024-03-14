from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaEntrega = forms.DateField()
    entregado = forms.BooleanField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()

class RegistroUsuario(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",  "email", "password1", "password2"]


class EditarUsuario(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = ["first_name", "last_name",  "email"]
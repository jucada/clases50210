from django import forms

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
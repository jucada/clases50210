from django import forms

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaEntrega = forms.DateField()
    entregado = forms.BooleanField()
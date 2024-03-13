from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField() 
    edad = models.IntegerField()

    def __str__(self):

        return f"{self.nombre} --- {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

    def __str__(self):

        return f"{self.nombre} --- {self.comision}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
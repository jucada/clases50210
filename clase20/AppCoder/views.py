from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiantes

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")


def ver_estudiantes(request):

    return render(request, "ver_estudiantes.html")

def ver_cursos(request):

    return render(request, "ver_cursos.html")

def ver_profesores(request):

    return render(request, "ver_profes.html")

def ver_entregables(request):

    return render(request, "ver_entregables.html")




def crear_curso(request):

    curso_1 = Curso(nombre="Desarrollo móvil", comision=55555)

    curso_1.save() #guardarlo en su respectiva tabla

    return HttpResponse(f"Hemos creado un curso llamado {curso_1.nombre}!!")


def crear_estudiante(request):

    est_1 = Estudiantes(nombre="Diego", apellido="De La Fuente", email="estudiante@ch.com", edad=28)

    est_2 = Estudiantes(nombre="Belen", apellido="Ulloa", email="estudiante2@ch.com", edad=38)

    est_1.save()
    est_2.save()

    info = {"nombre1":est_1.nombre, "nombre2":est_2.nombre}


    return render(request, "crear_estudiantes.html", info) #1er arg -- request, 2do arg -- template, 3er arg -- contexto(diccionario)
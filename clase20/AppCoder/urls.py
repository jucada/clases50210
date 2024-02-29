from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("curso/", crear_curso),
    path("estudiantes/", crear_estudiante),
    path("ver_cursos", ver_cursos, name="Ver Cursos"),
    path("ver_estudiantes", ver_estudiantes, name="Ver Estudiantes"),
    path("ver_profes", ver_profesores, name="Ver Profes"),
    path("ver_entregas", ver_entregables, name="Ver Entregas"),
    path("", inicio, name="Home"),

]

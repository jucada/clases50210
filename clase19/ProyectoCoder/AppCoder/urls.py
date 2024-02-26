from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("curso/", crear_curso),
    path("estudiantes/", crear_estudiante),
    path("ver_cursos", ver_cursos),
    path("ver_estudiantes", ver_estudiantes),
    path("ver_profes", ver_profesores),
    path("ver_entregas", ver_entregables),
    path("", inicio),

]

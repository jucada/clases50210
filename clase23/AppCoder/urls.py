from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Home"),

    path("login/", iniciar_sesion, name="Iniciar Sesion"),
    path("signup/", registrarse, name="Registrarse"),
    path("logout/", cerrar_sesion, name="Cerrar Sesion"),



    #Urls de CRUD de modelos

    path("crear_estudiante/", crear_nuevo_estudiante, name = "Crear Estudiante"),
    path("ver_estudiantes/", ver_estudiantes, name = "Ver Estudiantes"),
    path("actualizar_estudiante/<estudiante_info>/", actualizar_estudiantes, name = "Editar Estudiante"),
    path("borrar_estudiante/<estudiante_info>/", borrar_estudiante, name = "Eliminar Estudiante"),

    path("crear_curso/", crear_curso),
    path("ver_cursos/", ver_cursos, name="Ver Cursos"),

    
    path("crear_profe/", crear_profesor),
    path("ver_profes/", ver_profesores, name="Ver Profes"),

    path("crear_entrega/", crear_entregable),
    path("ver_entregas/", ver_entregables, name="Ver Entregas"),

    #Urls de busqueda
    path("buscar_curso/", buscar_curso),


    #url de CRUD hecho con clases

    path("lista_cursos/", CursosLista.as_view()),
    path("nuevo_curso/", CursosCrear.as_view()),
    path("editar_curso/<int:pk>", CursosEditar.as_view()),
    path("borrar_curso/<int:pk>", CursosBorrar.as_view())
]

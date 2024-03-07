from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiantes, Entregable, Profesor
from AppCoder.forms import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Vistas basadas en funciones

def inicio(request):

    return render(request, "inicio.html", {"mensaje": "Bienvenido a mi página"})


# Iniciar Sesion

def iniciar_sesion(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            usuario = authenticate(username=info_dic["username"], password=info_dic["password"])

            if usuario is not None: #que el usuario existe!!!

                login(request, usuario)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
        
            
        else:

            return render(request, "inicio.html", {"mensaje":"Credenciales Incorrectas"})
        
    else:

        formulario = AuthenticationForm()

    return render(request, "registro/inicio_sesion.html", {"formu":formulario})




# Registrarse

def registrarse(request):

    if request.method == "POST":

        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():

            formulario.save() #crea el nuevo usuario

            return render(request, "inicio.html", {"mensaje":"El usuario ha sido creado con éxito."})
    
    else:

        formulario = UserCreationForm()



    return render(request, "registro/registro.html", {"formu":formulario})


def cerrar_sesion(request):

    logout(request)

    return render(request, "inicio.html", {"mensaje":"Has cerrado sesión con éxito."})



# CRUD de los modelos
# CRUD de estudiantes

#Sin formulario (crear con valores especificos)
def crear_estudiante(request):

    est_1 = Estudiantes(nombre="Diego", apellido="De La Fuente", email="estudiante@ch.com", edad=28)

    est_2 = Estudiantes(nombre="Belen", apellido="Ulloa", email="estudiante2@ch.com", edad=38)

    est_1.save()
    est_2.save()

    info = {"nombre1":est_1.nombre, "nombre2":est_2.nombre}


    return render(request, "estudiantes/crear_estudiantes.html", info) #1er arg -- request, 2do arg -- template, 3er arg -- contexto(diccionario)

#Con formulario (crear con valores especificos)
@login_required
def crear_nuevo_estudiante(request):

    if request.method == "POST":

        formulario = EstudianteFormulario(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            estudiante_nuevo = Estudiantes(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                email=info_dic["email"],
                edad=info_dic["edad"]
                )
            
            estudiante_nuevo.save()

            return render(request, "inicio.html")
        
    else:

        formulario = EstudianteFormulario()

    return render(request, "estudiantes/crear_estudiantes.html", {"formu":formulario})


def ver_estudiantes(request):

    todos_estudiantes = Estudiantes.objects.all() #obtener todos los estudiantes que existen

    return render(request, "estudiantes/ver_estudiantes.html", {"total":todos_estudiantes})

@login_required
def actualizar_estudiantes(request, estudiante_info):

    estudiante_elegido = Estudiantes.objects.get(id=estudiante_info)

    if request.method == "POST":

        formulario = EstudianteFormulario(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            #Cambiado los datos de un objeto que ya se habia creado!!
            estudiante_elegido.nombre = info_dic["nombre"]
            estudiante_elegido.apellido = info_dic["apellido"]
            estudiante_elegido.email = info_dic["email"]
            estudiante_elegido.edad = info_dic["edad"]

            estudiante_elegido.save()

            return render(request, "inicio.html")
        
    else:

        formulario = EstudianteFormulario(initial={"nombre":estudiante_elegido.nombre, "apellido":estudiante_elegido.apellido,
                                                   "email":estudiante_elegido.email, "edad":estudiante_elegido.edad})

    return render(request, "estudiantes/actualizar_estudiantes.html", {"formu":formulario})

@login_required
def borrar_estudiante(request, estudiante_info):

    estudiante_elegido = Estudiantes.objects.get(id=estudiante_info)

    estudiante_elegido.delete()

    return render(request, "inicio.html")

# CRUD de Cursos

def crear_curso(request):

    if request.method == "POST": #Cuando aprieto el boton de enviar!!!
        
        curso_nuevo = Curso(nombre=request.POST["nombre"],comision=request.POST["comision"])
        #Leer la informacion y guardarla en la base de datos!!!
        curso_nuevo.save()

        return render(request, "inicio.html")

    
    return render(request, "cursos/crear_cursos.html")

@login_required
def ver_cursos(request):

    todos_cursos = Curso.objects.all()

    return render(request, "cursos/ver_cursos.html", {"total":todos_cursos})



def borrar_curso(request, curso_info):

    curso_elegido = Curso.objects.get(id=curso_info)

    curso_elegido.delete()

    return render(request, "inicio.html")


# CRUD de Profesores

def crear_profesor(request):

    if request.method == "POST":

        formulario = ProfesorFormulario(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            profesor_nuevo = Profesor(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                email=info_dic["email"],
                profesion=info_dic["profesion"]
                )
            
            profesor_nuevo.save()

            return render(request, "inicio.html")
        
    else:

        formulario = ProfesorFormulario()

    return render(request, "profes/crear_profesor.html", {"formu":formulario})

def ver_profesores(request):

    return render(request, "profes/ver_profes.html")


#CRUD de Entregables

#Crear un entregable en la base de datos usando un formulario    
def crear_entregable(request):

    if request.method == "POST":

        formulario = EntregableFormulario(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            entrega_nueva = Entregable(
                nombre=info_dic["nombre"],
                fechaEntrega=info_dic["fechaEntrega"],
                entregado=info_dic["entregado"]
                )
            
            entrega_nueva.save()

            return render(request, "inicio.html")
        
    else:

        formulario = EntregableFormulario()

    return render(request, "entregas/crear_entregable.html", {"formu":formulario})

def ver_entregables(request):

    return render(request, "entregas/ver_entregables.html")


# Busqueda 

def buscar_curso(request):
    

    if request.GET: #Solo si es que hay una busqueda!!!

        nombre = request.GET["nombre"]  #leer el diccionario de info del formulario y obtengo el valor de busqueda
        cursos = Curso.objects.filter(nombre__icontains=nombre) #filtrar todos los cursos que tengan dicho nombre!!
        
        mensaje = f"Estamos buscando al curso {nombre}"

        return render(request, "cursos/resultados_cursos.html", {"mensaje":mensaje, "resultados":cursos})

    
    return render(request, "cursos/resultados_cursos.html") #si todavia no hay una busqueda



# Vistas basadas en Clases!!

class CursosLista(ListView):
    model = Curso
    template_name = "cursos/lista_de_cursos.html"

# Create del CRUD
class CursosCrear(LoginRequiredMixin, CreateView):
    model = Curso
    template_name = "cursos/nuevo_curso.html"
    fields = ["nombre", "comision"]
    success_url = "/AppCoder/ver_cursos/"
    

# Update del CRUD
    
class CursosEditar(UpdateView):
    model = Curso
    template_name = "cursos/nuevo_curso.html"
    fields = ["nombre", "comision"]
    success_url = "/AppCoder/"


# Delete del CRUD

class CursosBorrar(DeleteView):
    model = Curso
    template_name = "cursos/borrar_curso.html"
    success_url = "/AppCoder/"
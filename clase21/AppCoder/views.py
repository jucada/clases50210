from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiantes, Entregable
from AppCoder.forms import EntregableFormulario

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

    if request.method == "POST": #Cuando aprieto el boton de enviar!!!
        
        curso_nuevo = Curso(nombre=request.POST["nombre"],comision=request.POST["comision"])
        #Leer la informacion y guardarla en la base de datos!!!
        curso_nuevo.save()

        return render(request, "inicio.html")

    
    return render(request, "crear_cursos.html")

    
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

    return render(request, "crear_entregable.html", {"formu":formulario})



def crear_estudiante(request):

    est_1 = Estudiantes(nombre="Diego", apellido="De La Fuente", email="estudiante@ch.com", edad=28)

    est_2 = Estudiantes(nombre="Belen", apellido="Ulloa", email="estudiante2@ch.com", edad=38)

    est_1.save()
    est_2.save()

    info = {"nombre1":est_1.nombre, "nombre2":est_2.nombre}


    return render(request, "crear_estudiantes.html", info) #1er arg -- request, 2do arg -- template, 3er arg -- contexto(diccionario)




def buscar_curso(request):
    

    if request.GET: #Solo si es que hay una busqueda!!!

        nombre = request.GET["nombre"]  #leer el diccionario de info del formulario y obtengo el valor de busqueda
        cursos = Curso.objects.filter(nombre__icontains=nombre) #filtrar todos los cursos que tengan dicho nombre!!
        
        mensaje = f"Estamos buscando al curso {nombre}"

        return render(request, "resultados_cursos.html", {"mensaje":mensaje, "resultados":cursos})

    
    return render(request, "resultados_cursos.html") #si todavia no hay una busqueda
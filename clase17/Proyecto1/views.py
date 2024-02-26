from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
import random


def saludo(request, nombre):

    return HttpResponse(f"Hola {nombre}, bienvenido a mi pagina!!!!!!!")


def about(request):

    numero_azar = random.randint(1,6)

    f = open(r"C:\Users\dalev\Desktop\CH - 50210\clase17_14_02\ProyectoDjango\Proyecto1\Proyecto1\templates\about.html")

    plantilla = Template(f.read())

    f.close()

    info = {"resultado":numero_azar}

    contexto = Context(info) #vamos a crear un objeto de tipo Contexto con la informacion del diccionario!!

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def tiempo(request):

    ahora = datetime.now() #usamos el modulo datetime de Python

    horas = ahora.hour
    minutos = ahora.minute
    segundos = ahora.second

    f = open(r"C:\Users\dalev\Desktop\CH - 50210\clase17_14_02\ProyectoDjango\Proyecto1\Proyecto1\templates\tiempo.html")

    plantilla = Template(f.read())

    f.close()

    info = {"h":horas, "m":minutos, "s":segundos}

    contexto = Context(info) #vamos a crear un objeto de tipo Contexto con la informacion del diccionario!!

    documento = plantilla.render(contexto)

    #print(f"{horas}--{minutos}--{segundos}")

    return HttpResponse(documento)



def inicio(request):

    nombres = ["Pablo", "Matias", "Lucas", "Gaston"]

    ahora = datetime.now()

    numero_azar = random.randint(1,6)

    info = {"nombres":nombres, "ahora":ahora, "resultado":numero_azar}

    f = open(r"C:\Users\dalev\Desktop\CH - 50210\clase17_14_02\ProyectoDjango\Proyecto1\Proyecto1\templates\inicio.html")

    plantilla = Template(f.read())

    f.close()

    contexto = Context(info)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

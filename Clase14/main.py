#Los módulos se importan
from definiciones.herencia import Cetaceo #lee el archivo llamado herencia dentro del paquete llamado definiciones!!!!!
from definiciones.operaciones import sumar #lee el archivo y de paso trae a una funcion en especifico

print("Inicio del programa --- Creamos un cetaceo")

#la clase cetaceo se encuentra dentro del archivo herencia
ballena = Cetaceo(2, 1, "No", "Cachalote", "Odontoceto más grandes", "Oceano pacífico", 13000)

print(ballena.lugar)

#utilizar la funcion sumar del archivo operaciones
sumar(5,18)
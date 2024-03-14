def es_mayuscula_primera(palabra):
    return palabra[0].isupper() #True si es mayuscula --- False si es minuscula

palabras = ("Argentina", "francia", "italia")

resultado = filter(es_mayuscula_primera, palabras) #filter(funcion_filtradora, secuencia)

print(list(resultado))
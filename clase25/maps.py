cubo = lambda x:x**3

numeros = [1, 2, 3, 4, 5]

resultados = map(cubo, numeros) #map(funcion, secuencia)

print(tuple(resultados)) #convertirla a una lista o tupla
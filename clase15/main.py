f = open(r"C:\Users\dalev\Documents\Datos.txt", "r") #modo read (modo lectura)

#datos = f.read() #leyendo la info del archivo y vamos a guardarlo en una variable

datos = f.readlines()

#datos = f.readline()

#posicion = datos[5]

#print(posicion.upper())

print(datos)

f.close()



from registro import registrar_usuario, mostrar_db #traemos todas las funciones del archivo registro.py

mi_data = {}

usuario, contra = registrar_usuario(mi_data)

mostrar_db(mi_data)

#raw string
mi_archivo = open(r"C:\Users\dalev\Desktop\CH - 50210\clase15\mi_data.txt", "a")

mi_archivo.write(f"Usuario: {usuario} ---- Contraseña: {contra}.\n")


mi_archivo.close() #cerrar un archivo despues de abrirlo
def registrar_usuario(db):
  user=input('Por favor, ingrese su nuevo usuario: ')
  passw=input('Por favor, ingrese la nueva contrasena: ')
  db[user]=passw
  return user, passw

def mostrar_db(db):
  for key, value in db.items():
    print(f'\n El user es: --{key}-- \n y la contrasena es: --{value}--')
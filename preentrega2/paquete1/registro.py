def registrar_usuario(db):
  user=input('Por favor, ingrese su nuevo usuario: ')
  passw=input('Por favor, ingrese la nueva contrasena: ')
  db[user]=passw

def mostrar_db(db):
  for key, value in db.items():
    print(f'\n El user es: --{key}-- \n y la contrasena es: --{value}--')

def login(db):
  #pido user
  login_user=str(input('Por favor ingrese su usuario:'))

  #checkeo si el user es un key dentro de la db, sino termino.
  if login_user in db:
    print(f'User {login_user} OK!')
  else:
    print(f'No se encuentra el usuario {login_user}, intente nuevamente.')
    return

  #pido password
  login_passw=str(input('Por favor ingrese su contrasena:'))
  #tomo la value del key ingresado como password correcta
  correct_password=db.get(login_user,f'No se encuentra el usuario {login_user}')

  #si password coincide con value de db[key]
  if correct_password==login_passw:
    print(f'Password OK! bienvenido {login_user}!!')
  else:
    print('Password incorrecto, adios!')
    return
from src.domain.userbuilder import UserBuilder
from src.domain.database import Database

def crear_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    email = input("Ingrese email: ")

    builder = UserBuilder(usuario, email)

    agregar_edad = input("¿Desea agregar edad? (s/n): ").lower()
    if agregar_edad == 's':
        edad = int(input("Ingrese edad: "))
        builder = builder.with_edad(edad)

    agregar_direccion = input("¿Desea agregar dirección? (s/n): ").lower()
    if agregar_direccion == 's':
        direccion = input("Ingrese dirección: ")
        builder = builder.with_direccion(direccion)

    user = builder.build()
    db = Database()
    db.add_user(user)
    print("Usuario creado exitosamente.\n")

def mostrar_usuarios():
    db = Database()
    usuarios = db.list_users()
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for user in usuarios:
            print(user)
    print()

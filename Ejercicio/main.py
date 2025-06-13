from src.domain.menu import crear_usuario, mostrar_usuarios

def main():
    while True:
        print("===== MENU PRINCIPAL =====")
        print("1. Crear usuario")
        print("2. Mostrar usuarios")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            mostrar_usuarios()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente de nuevo")

if __name__ == "__main__":
    main()

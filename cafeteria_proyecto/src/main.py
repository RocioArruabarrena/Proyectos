from cafeteria import Cafeteria, ProductoBebida, ProductoComida, Mozo, Cajero, Pedido

# Instancia única de la cafetería
cafeteria = Cafeteria("Cafe Terminal")

# Agregamos productos al menú
cafeteria.agregar_producto(ProductoBebida("Cafe", 500, 10))
cafeteria.agregar_producto(ProductoBebida("Te", 400, 8))
cafeteria.agregar_producto(ProductoComida("Medialuna", 300, 12))
cafeteria.agregar_producto(ProductoComida("Tostado", 600, 5))

# Creamos empleados
mozo = Mozo("Federico")
cajero = Cajero("Rocio")

# Menú interactivo
def mostrar_menu():
    print("MENU PRINCIPAL")
    print("1. Ver productos")
    print("2. Realizar pedido")
    print("3. Ver total vendido")
    print("4. Salir")

def mostrar_productos():
    print("PRODUCTOS DISPONIBLES")
    for i, p in enumerate(cafeteria.menu):
        print(f"{i + 1}. {p.descripcion()} (Stock: {p.stock})")

def realizar_pedido():
    mostrar_productos()
    try:
        idx = int(input("Ingrese el numero del producto: ")) - 1
        cantidad = int(input("Cantidad: "))
        tipo = input("Atendido por (mozo/cajero)?: ").lower()

        if tipo == "mozo":
            empleado = mozo
        elif tipo == "cajero":
            empleado = cajero
        else:
            print("Tipo de empleado invalido.")
            return

        producto = cafeteria.menu[idx]
        pedido = Pedido(empleado, producto, cantidad)
        resultado = pedido.procesar()
        print("\n" + resultado)
    except (ValueError, IndexError):
        print("Entrada invalida, intente de nuevo.")

# Programa principal
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            realizar_pedido()
        elif opcion == "3":
            print(f"Total vendido: ${cafeteria.total_vendido}")
        elif opcion == "4":
            print("Gracias por usar el sistema")
            break
        else:
            print("Opcion invalida")

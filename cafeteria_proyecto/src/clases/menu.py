from abc import ABC, abstractmethod

from cafeteria import Cafeteria
from empleados import Cajero, Mozo
from pedido import Pedido
from productos import ProductoBebida, ProductoComida

def menu_terminal():
    cafeteria = Cafeteria("Cafe ZEPPE")
    
    cafeteria.agregar_producto(ProductoBebida("Cafe", 500, 20))
    cafeteria.agregar_producto(ProductoBebida("Te", 400, 15))
    cafeteria.agregar_producto(ProductoComida("Tostada", 600, 10))
    cafeteria.agregar_producto(ProductoComida("Medialuna", 300, 25))

 
    mozo = Mozo("Federico")
    cajero = Cajero("Rocio")

    while True:
        print("Menu Principal")
        print("1. Ver menu")
        print("2. Realizar pedido")
        print("3. Ver total vendido")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cafeteria.mostrar_menu()
        elif opcion == "2":
            cafeteria.mostrar_menu()
            try:
                idx = int(input("Seleccione el numero del producto: ")) - 1
                cantidad = int(input("Ingrese cantidad: "))
                print("Quien atiende el pedido? (1) Mozo / (2) Cajero")
                tipo = input("Ingrese opcion: ")
                empleado = mozo if tipo == "1" else cajero
                pedido = Pedido(empleado, cafeteria.menu[idx], cantidad)
                pedido.procesar()
            except:
                print("Entrada invalida")
        elif opcion == "3":
            cafeteria.mostrar_total()
        elif opcion == "4":
            print("Gracias por usar el sistema")
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    menu_terminal()
from abc import ABC, abstractmethod


class Cafeteria:
    _instancia = None

    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super(Cafeteria, cls).__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.menu = []
            cls._instancia.total_vendido = 0
        return cls._instancia

    def agregar_producto(self, producto):
        self.menu.append(producto)

    def mostrar_menu(self):
        print(f"Menu de {self.nombre}:")
        for idx, prod in enumerate(self.menu):
            print(f"{idx+1}. {prod}")

    def procesar_pedido(self, indice, cantidad):
        if 0 <= indice < len(self.menu):
            prod = self.menu[indice]
            if prod.stock >= cantidad:
                prod.stock -= cantidad
                total = prod.precio * cantidad
                self.total_vendido += total
                print(f"Pedido exitoso: {cantidad} x {prod.nombre} - Total: ${total}")
            else:
                print("No hay suficiente stock")
        else:
            print("Opcion invalida")

    def mostrar_total(self):
        print(f"Total vendido: ${self.total_vendido}")




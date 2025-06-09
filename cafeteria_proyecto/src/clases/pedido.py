from abc import ABC, abstractmethod

class Pedido:
    def __init__(self, empleado, producto, cantidad):
        self.empleado = empleado
        self.producto = producto
        self.cantidad = cantidad

    def procesar(self):
        print(self.empleado.realizar_pedido())
        if self.producto.stock >= self.cantidad:
            self.producto.stock -= self.cantidad
            total = self.producto.precio * self.cantidad
            print(f"Pedido procesado: {self.cantidad} x {self.producto.nombre} = ${total}")
        else:
            print("Stock insuficiente")

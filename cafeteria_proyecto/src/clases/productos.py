from abc import ABC, abstractmethod


class Producto(ABC):
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @abstractmethod
    def descripcion(self):
        pass

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

class ProductoBebida(Producto):
    def descripcion(self):
        return f"Bebida: {self.nombre}, Precio: ${self.precio}"

class ProductoComida(Producto):
    def descripcion(self):
        return f"Comida: {self.nombre}, Precio: ${self.precio}"
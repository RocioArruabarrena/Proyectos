from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def realizar_pedido(self):
        pass

class Mozo(Empleado):
    def realizar_pedido(self):
        return "{self.nombre} toma el pedido del cliente en mesa"

class Cajero(Empleado):
    def realizar_pedido(self):
        return "{self.nombre} registra el pedido en la caja"

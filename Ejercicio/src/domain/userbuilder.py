from src.domain.user import User

class UserBuilder:
    def __init__(self, usuario, email):
        self.usuario = usuario
        self.email = email
        self.edad = None
        self.direccion = None

    def with_edad(self, edad):
        self.edad = edad
        return self

    def with_direccion(self, direccion):
        self.direccion = direccion
        return self

    def build(self):
        return User(self.usuario, self.email, self.edad, self.direccion)


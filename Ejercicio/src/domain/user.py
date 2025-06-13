class User:
    def __init__(self, usuario, email, edad=None, direccion=None):
        self.usuario = usuario
        self.email = email
        self.edad = edad
        self.direccion = direccion

    def __str__(self):
        return f"User(usuario={self.usuario}, email={self.email}, edad={self.edad}, direcciom={self.direccion})"
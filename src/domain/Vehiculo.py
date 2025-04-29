class  Vehiculo():

    ## Atributos
    marca = ""
    modelo = ""
    color = ""
    anio = 0

    ## Constructor 
    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio


    ## Métodos (Acciones)
    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} está encendido.")

    def apagar(self):
        print(f"El vehículo {self.marca} {self.modelo} está apagado.")

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} está acelerando.")

    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} está frenando.")  



    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Año: {self.anio}"


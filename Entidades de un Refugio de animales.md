Entidades de un Refugio de animales

Perro: nombre, edad, peso, estado, raza
Gato: nombre, edad, peso, estado, color_pelaje
Loro: nombre, edad, peso, estado, longitud_alas

HERENCIA:
                    ANIMALES = 
                nombre_edad_peso_estado
PERRO:          GATO:           LORO:
raza            color_pelaje    longitud_alas
comer ()        comer ()        comer ()
_croquetas      _comida humeda  _zanahoria




Class Animales {
    nombre: string,
    edad: numerico,
    peso: numerico,
    estado: string 
},

Class Perro extends Animales{
    raza: string
},

Class Gato extends Animales{
    color_pelaje: string
},

Class Loro extends Animales {
    longitud_alas: string
}





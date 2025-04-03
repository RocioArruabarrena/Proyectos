Refugio de animales

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




public class Animales {
    nombre: string,
    edad: numerico,
    peso: numerico,
    estado: string 
},

private class Perro extends Animales{
    raza: string
},

private class Gato extends Animales{
    color_pelaje: string
},

private class Loro extends Animales {
    longitud_alas: string
}




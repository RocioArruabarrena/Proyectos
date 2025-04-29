
import string
    
class Biblioteca ():
    
    ## No tiene un nombre de una accion, metodo o es un contructor
    def Biblioteca (lista_de_libros, usuarios_registrados):
        return {
            "lista_de_libros": string,
            "usuarios_registrados": string
        }
    
    ## Constructor
    def __init__(self, lista_de_libros, usuarios_registrados):
        self.lista_de_libros = lista_de_libros
        self.usuarios_registrados = usuarios_registrados
        self.libros = []
        self.usuarios = []
        self.biblioteca = {
            "libros": self.libros,
            "usuarios": self.usuarios
        }



## Nombre de una accion, es un metodo o funcion
    def registrar_usuario(biblioteca, usuario):
            biblioteca["usuarios"].append(usuario)
            print('Usuario '{usuario['nombre']}' registrado con exito')

    def agregar_libro(biblioteca, libro):
            biblioteca["libros"].append(libro)
            print('Libro '{libro['titulo']}' agregado a la biblioteca')


    def buscar_por_titulo(biblioteca, titulo):
            resultados = [
                libro for libro in biblioteca["libros"]
                if titulo.lower() in libro["titulo"].lower()
            ]
            if resultados:
                print('Libros encontrados con titulo '{titulo}':')
                for l in resultados:
                    print( - {l['titulo']} ({l['autor']}))
            else:
                print('No se encontraron libros con el titulo '{titulo}'')
            
            return resultados

    def buscar_por_autor(biblioteca, autor):
            resultados = [
                libro for libro in biblioteca["libros"]
                if autor.lower() in libro["autor"].lower()
            ]
            if resultados:
                print('Libros encontrados del autor '{autor}':')
                for l in resultados:
                    print( - {l['titulo']} ({l['autor']}))
            else:
                print('No se encontraron libros del autor '{autor}'')
            return resultados



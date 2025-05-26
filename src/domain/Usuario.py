import string


# Clases en singular
class Usuario ():
    nombre = string
    ID = int
    libros = string
    libros_prestados = []    

    #Definir que hace esta funcion para refactorizar
    def registrar_usuario (nombre, ID, libros_prestados):
        return {
            "nombre" : string,
            "ID": int,
            "libros": string,
            "libros_prestados": []
        }
        
    def prestar_libro (usuario, libro):
        if usuario in [registrar_usuario]:
            if len(usuario["libros_prestados"]) >= 3:
                print(" Error: el usuario ya tiene 3 libros prestados.")
            return False
        if not libro["disponible"]:
            print('Error: el libro'{libro['titulo']} 'no está disponible.')
            return False
        
        usuario["libros_prestados"].append(libro)
        libro["disponible"] = False
        print('Libro '{libro['titulo']}' prestado con éxito a'{usuario['nombre']})
        return True
    
    def devolver_libro(usuario, libro):
        if libro in usuario["libros_prestados"]:
            usuario["libros_prestados"].remove(libro)
            libro["disponible"] = True
            print('Libro '{libro['titulo']}' devuelto por'{usuario['nombre']})
        else:
            print("Este libro no fue prestado a este usuario.")
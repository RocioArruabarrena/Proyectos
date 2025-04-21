import string


class Libros ():
    def regristrar_libro (titulo, autor, ISBN, disponible = True):
        return {
            "titulo": string,
            "autor" : string,
            "ISBN": string,
            "disponible": bool,
            "tipo": "fisico"
        }

class LibroDigital:
    def registrar_libro_digital(titulo, autor, isbn, tamaño_mb, disponible=True):
        return {
            "titulo": string,
            "autor": string,
            "ISBN": string,
            "disponible": bool,
            "tamaño_mb": float,
            "tipo": "digital"
        }
        
    def descargar(libro):
        if libro["disponible"]:
            print('Descargando'{libro['titulo']} ({libro['tamaño_mb']}) MB)
        else:
            print ('El libro digital'{libro['titulo']} 'no esta disponible')
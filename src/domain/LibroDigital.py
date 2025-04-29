class LibroDigital():

    #Attributes
    titulo = ""
    autor = ""
    ISBN = ""
    disponible = True
    tamaño_mb = 0.0
    tipo = "digital"
    
   

    # Registrar libro digital
    def registrar_libro(titulo, autor, ISBN, tamaño_mb, disponible=True):
        return {
            "titulo": titulo,
            "autor": autor,
            "ISBN": ISBN,
            "disponible": disponible,
            "tamaño_mb": tamaño_mb,
            "tipo": "digital"
        }

        
    def descargar(libro):
        if libro["disponible"]:
            print('Descargando'{libro['titulo']} ({libro['tamaño_mb']}) MB)
        else:
            print ('El libro digital'{libro['titulo']} 'no esta disponible')
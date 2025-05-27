
def agregar_nota(nota):
        with open("notes.txt", "a", encoding="utf-8") as archivo:
              archivo.write(nota + "\n")

# Probamos agregar una nota
agregar_nota("Mi primer nota")
print("Nota agregada")

import os
print("Archivo creado en:", os.path.abspath("notes.txt"))

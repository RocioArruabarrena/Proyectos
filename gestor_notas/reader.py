
def mostrar_notas():
    try:
       with open("notes.txt", "r", encoding="utf-8") as archivo:
        notas = archivo.readlines()
        print("Notas guardadas:")
        for nota in notas:
            print("-", nota.strip())
    except FileNotFoundError:
        print("No hay notas guardadas")

mostrar_notas()


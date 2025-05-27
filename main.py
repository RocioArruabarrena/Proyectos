from writer import Writer
from reader import Reader

writer = Writer()
reader = Reader()

writer.addNote("Mi primera nota")
notas = reader.getAllNotes()

print("Notas guardadas:")
for nota in notas:
    print("-", nota)

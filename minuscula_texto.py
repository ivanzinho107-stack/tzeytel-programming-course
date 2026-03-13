with open("datos.txt", "r") as archivo:
    texto = archivo.read()

palabras = texto.lower().split()

print(palabras)

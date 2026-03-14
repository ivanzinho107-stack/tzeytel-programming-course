texto = "Tres tristes Tigres, tragaban trigo en un trigal, en tres tristes..."
#print(texto[10],texto[11],texto[12])

lista = texto.split()
print(lista)

texto = texto.lower()
texto = texto.replace(",", "")
texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace(".", "")

lista_limpia = texto.split()

print('\n')
print(lista_limpia)
print('\n')

for palabra in lista_limpia:
    contador = 0
    for elemento in lista_limpia:
        if elemento == palabra:
            contador += 1
    print(palabra, contador)

print('\n')


# Diccionarios
frecuencias = {}

for numero in lista_limpia:
    if numero in frecuencias:
        frecuencias[numero] += 1
    else:
        frecuencias[numero] = 1

print(frecuencias.get('tigres'))
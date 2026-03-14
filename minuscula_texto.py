import requests

url = "https://raw.githubusercontent.com/ivanzinho107-stack/tzeytel-programming-course/main/datos.txt"

respuesta = requests.get(url)
print(respuesta.status_code)
print(respuesta.text.upper())
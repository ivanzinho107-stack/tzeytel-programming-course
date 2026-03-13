import requests

def significado(palabra):

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{palabra}"

    response = requests.get(url)

    datos = response.json()

    return datos[0]["meanings"][0]["definitions"][0]["definition"]


print(significado("house"))

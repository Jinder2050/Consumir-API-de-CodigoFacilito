import requests

def pokeapi():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/')

    if response.status_code == 200:
        payload = response.json()
        return payload['results']
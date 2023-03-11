import requests

def pokeapi():
    """
    Retorna los nombres de pokemones del API de PokeAPI

    >>> type(pokeapi()) == type(list())
    True
    """


    response = requests.get('https://pokeapi.co/api/v2/pokemon/')

    if response.status_code == 200:
        payload = response.json()
        # print(type(payload['results']))
        return payload['results']
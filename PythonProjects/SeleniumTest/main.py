import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a3a70dd70c734bd0af332c99e54afd38'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_creation = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "12331",
    "name": "Norman",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "9"
}

response_creation = requests.post(url = f'{URL}/pokemons', headers=HEADER,json=body_creation )
print(response_creation.text)


response_change = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_change )
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball )
print(response_pokeball.text)

pokemon_id = response_creation.json()['id']
print(pokemon_id)
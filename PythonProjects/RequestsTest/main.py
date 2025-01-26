import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5a34f0d8b74dd6c16a90a9735b3dc797'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}




body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post (url = f'{URL}/pokemons' , headers = HEADER , json = body_create)
print (response_create.text)





body_name = {
    "pokemon_id": "203719",
    "name": "generate",
    "photo_id": -1
}

response_name = requests.put (url = f'{URL}/pokemons' , headers = HEADER , json = body_name)
print (response_name.text)





body_in_pokeboll = {
    "pokemon_id": "203719"
}

response_in_pokeboll = requests.post (url = f'{URL}/trainers/add_pokeball' , headers = HEADER , json = body_in_pokeboll)
print (response_in_pokeboll.text)
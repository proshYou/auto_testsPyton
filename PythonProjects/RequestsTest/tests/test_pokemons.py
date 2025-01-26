import requests
import pytest



URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5a34f0d8b74dd6c16a90a9735b3dc797'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = 18463


def test_status_code():
    response = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'strapcuter'
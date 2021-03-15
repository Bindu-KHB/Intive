import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')


json_content = json.loads(response.content)

for moves in json_content['moves']:
    pikachu_move = (moves['move']['name'])
    if pikachu_move == "thunder-punch":
        print("Verified thunder-punch move found")


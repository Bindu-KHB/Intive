import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

json_content = json.loads(response.content)

for moves in json_content['moves']:
    pikachu_move = (moves['move']['name'])
    if pikachu_move == "thunder-punch":
        print("Verified thunder-punch move found")


location_area_encounters_var = json_content['location_area_encounters']

encounters_response = requests.get(location_area_encounters_var)
encounters_content = json.loads(encounters_response.content)

for encounter in encounters_content:
    version_details = (encounter['version_details'][0])
    name = (version_details['version']['name'])

    if name == "yellow":
        content = version_details['encounter_details'][0]
        if(content['method']['name']) == 'gift':
            print("Pikachu can be received as a gift")

import requests
import json

url="https://api.tierion.com/v1/records/WYhJtu2_uEOwF_pVbg0pjA"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}


response = requests.get(url, headers=headers)
print(response)
print(response.json())

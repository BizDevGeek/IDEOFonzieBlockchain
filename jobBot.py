#Jozef Nagy
#6/23/17
#Purpos: Search the blockchain for part failure events and take action.
#The action inclues ordering the part and scheduling service.

import requests
import json

url_base="https://api.tierion.com/v1/records?datastoreId=1735"
url = url_base
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}


response = requests.get(url, headers=headers)
print(response)
print(response.json())


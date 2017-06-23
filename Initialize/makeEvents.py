#Initialize some sample objects for:
#   Car
#   ServiceProvider (garage, shop, etc)
#   Part


import requests
import json

CarData = {"datastoreId":1735,
           "object_type"
           "VIN":"123ABC",
           "make":"Ford",
           "model":"Mustang",
           "year":2001,
           "owner":"Marco Polo",
           "drivetrain":{"tranny":"manual", "driveshaft_part":1365}}
data_json = json.dumps(CarData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())

PartData = {"datastoreId":1735,
           "PID":829,
           "description":"Oxygen sensor",
           "manufacturer":"Motorcraft"}
data_json = json.dumps(CarData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())

PartData = {"datastoreId":1735,
           "PID":829,
           "description":"brake pad",
           "manufacturer":"Motorcraft"}
data_json = json.dumps(CarData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())

PartData = {"datastoreId":1735,
           "PID":829,
           "description":"rotor",
           "manufacturer":"Motorcraft"}
data_json = json.dumps(CarData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())

MechanicData = {"datastoreId":1735,
                "MID":34,
                "address":"1 Main St, Boston, MA 02149",
                "credentials":"ASE Certified",
                "makes_can_fix":"mazda,ford,chevy"}
data_json = json.dumps(MechanicData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())



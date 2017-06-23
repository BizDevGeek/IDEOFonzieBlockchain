#Initialize some sample objects for:
#   Car
#   ServiceProvider (garage, shop, etc)
#   Part


import requests
import json

CarData = {"datastoreId":1735,
           "object_type":"car",
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
            "object_type":"part",
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
            "object_type":"part",
           "PID":153,
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
            "object_type":"part",
           "PID":477,
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

PartData = {"datastoreId":1735,
            "object_type":"part",
           "PID":322,
           "description":"air filter",
           "manufacturer":"Autozone"}
data_json = json.dumps(CarData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())

PartData = {"datastoreId":1735,
            "object_type":"part",
           "PID":987,
           "description":"steering wheel",
           "manufacturer":"Autozone"}
data_json = json.dumps(CarData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())


MechanicData = {"datastoreId":1735,
            "object_type":"mechanic",
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

#Car Owner
PersonData = {"datastoreId":1735,
            "object_type":"car_owner",
                "OID":163,
                "name":"Marco Polo",
                "address":"67 Pine St, Boston, MA 02149"}
data_json = json.dumps(MechanicData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())


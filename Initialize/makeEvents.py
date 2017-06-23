#Initialize some sample events for:
#   swap (old part for new part)


import requests
import json

EventData = {"datastoreId":1735,
           "object_type":"event_swap",
           "MID":34,
             "VIN":"11234WG",
           "part_old":256,
            "part_new":829}
data_json = json.dumps(EventData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())


EventData = {"datastoreId":1735,
           "object_type":"event_swap",
             "VIN":"11234WG",
           "MID":34,
           "part_old":829,
            "part_new":810}
data_json = json.dumps(EventData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())

EventData = {"datastoreId":1735,
           "object_type":"event_swap",
             "VIN":"11234WG",
           "MID":34,
           "part_old":153,
            "part_new":102}
data_json = json.dumps(EventData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())

#Transfer Ownership
EventData = {"datastoreId":1735,
           "object_type":"event_title",
             "VIN":"11234WG",
           "owner_old":256,
            "owner_new":829}
data_json = json.dumps(EventData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())

#Part failure
EventData = {"datastoreId":1735,
           "object_type":"event_failure",
             "PID":162,
             "VIN":"1734SD"}
data_json = json.dumps(EventData)
url="https://api.tierion.com/v1/records"
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
response = requests.post(url, data=data_json, headers=headers)
print(response)
print(response.json())






#Jozef Nagy
#6/23/17
#Purpose: Search the blockchain for part failure events and take action.
#The action includes ordering the part and scheduling service.

import requests
import json

def getObject(oid):
    url_base="https://api.tierion.com/v1/records/"
    objectID=oid
    url = url_base + objectID
    headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}
    response = requests.get(url, headers=headers)
    #print(response)
    return response.json()



#MAIN

#get a list of all objects
url_base="https://api.tierion.com/v1/records?datastoreId=1735"
url = url_base
headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}


response = requests.get(url, headers=headers)
raw_data = response.json()

#filter all the returned objects to find:

#loop through all json objects to find the group of data
for key in raw_data:
    value = raw_data[key]
    #print("The key and value are ({}) = ({})".format(key, value))
    if key == "records":
        events=value
        break
pass

#Lookup each ID in the blockchain
for x in events:
    #print(x)
    eid = x["id"]
    json_obj = getObject(eid)
    #print(json_obj)
    #Now check the "object_type" to see if it's an event to bid on.
    for y in json_obj:
        #json_y = json.loads(y)
        #print(json_y["data"])
        print(y)
        
        


#Jozef Nagy
#6/2017
#Based on code from John Oudsteyn


import requests
import serial
import json

def swapPart(rfid):
    print(rfid)
    

def writeRecord(dataPayload):
    setattr(dataPayload, "datastoreId", 1735)
    
    headers = {'Content-type': 'application/json',
           "X-Username":"jozefnagyjr@gmail.com",
           "X-Api-Key":"ZquJZ80IrE/gSq+1V79SImwIyvMtYHY4Z+MzNNuou8o="}

    response = requests.post(baseUrl, data=json.dumps(dataPayload), headers=headers)
    print(response)
    print(response.json())

baseUrl = "https://api.tierion.com/v1/records"
with serial.Serial('\\.\COM3', 9600) as ser:
    while True:
        line = ser.readline()
        swapPart(line.strip())
        #print(line.strip())
        

#Jozef Nagy
#6/2017
#Based on code from John Oudsteyn


import requests
import serial
import json

def swapPart(rfid):
    rfid = rfid   
    print("Part swap detected: " + str(rfid))
    writeRecord(rfid) 
    

def writeRecord(dataPayload):
    url = "https://ideo-autonet-node.run.aws-usw02-pr.ice.predix.io/api/vehicle/equipment/change"
    headers = {
    'content-type': "application/json",
    'x-api-key': "SsjA0MdYOGag8xSmLomllZ0wk2zp2s1GrXrBxhWuwt",
    'cache-control': "no-cache"
    }

    dataPayload = {"change":{"tag":dataPayload}}
    response = requests.request("POST", url, data=json.dumps(dataPayload), headers=headers)
    print(response)
    print(response.text)


#MAIN
#Use Windows-specific path to serial port
with serial.Serial('\\.\COM3', 9600) as ser:
    while True:
        line = ser.readline()
        swapPart(line.strip().decode("utf-8")) 
        #print(line.strip())
        

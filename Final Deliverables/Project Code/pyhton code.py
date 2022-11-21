import json
import time
import sys
import wiotp.sdk.device

myConfig={
    "identity":{
        "orgId": "hrsq7i",
        "typeId": "nodemcu",
        "deviceId": "11111"
    },
    "auth":{
        "token": "12345678"
    }
}
client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()

while True:
    name="velmurugan"
    latitude=8.737350267359217
    longitude=78.01497853901752
    myData={"name":name,"lat":latitude,"lon":longitude}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
    print("Data published")
    time.sleep(5)
client.disconnect()

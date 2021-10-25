import serial
import json
import requests as r

id = "YOUR ID"
url = f"http://192.168.1.65/api/{id}/groups/1/action"
port = "COM3"

def toggle():
    state = r.get(f"http://192.168.1.65/api/{id}/groups/1/").json()["action"]["on"]
    if (state):
        r.put(url, json.dumps({"on":False}))
    elif (state == False):
        r.put(url, json.dumps({"on":True}))

ser = serial.Serial(port, 9600, timeout=0)
while True:
    data = ser.readline()
    decodedData = data.decode("utf8")
    if (decodedData == "toggle"):
        toggle()
        print("-")
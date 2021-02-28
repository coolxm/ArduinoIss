from time import sleep
import serial
import requests
from geopy.geocoders import Nominatim

geoloc = Nominatim(user_agent="iss-tracker-arduino-experiment") #log in to the api
ser = serial.Serial('COM5', 9600) # Establish the connection on a specific port, at speed ...

def getloc(coord):
    location = geoloc.reverse(coord, exactly_one=True, language='en')
    if location == None : 
        print("Ocean")
        return "Ocean"
    else :
        address = location.raw['address']
        country = address.get('country', '')
        print(country)
    return country

def getiss():
    #request from api
    iss = requests.get('http://api.open-notify.org/iss-now.json')

    #More readable
    iss_json = iss.json()
    print(iss_json)
    print(iss_json["timestamp"])

    latitude = iss_json['iss_position']['latitude']
    longitude = iss_json['iss_position']['longitude']
    coords = str(latitude) + ", " + str(longitude)

    print(coords)
    return coords

def onStart():
    while True:
        coords = getiss()
        loc = getloc(coords)

        ser.write(bytes(coords, 'utf-8')) #write to serial
        ser.write(bytes(";" + loc, 'utf-8'))

        print (str(ser.readline())) # Read the newest output from the Arduino
        sleep(2) # Delay for two seconds

onStart()
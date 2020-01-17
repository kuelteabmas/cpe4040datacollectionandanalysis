import time
import smbus2
import bme280
import urllib
import http.client
import requests


key = ""                    # insert here API key for ThingSpeak Channel
interval = 10
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object

while True:
    
    data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
    print(data.id)
    print(data.timestamp)
    print(data.temperature)
    print(data.pressure)
    print(data.humidity)

# there is a handy string representation too
    print(data)

    #Encode all of our values into a single string we can send out
    params = urllib.parse.urlencode({'field1' : data.temperature, 'field2' : data.humidity, 'field3' : data.pressure, 'key':key})

    
    #Try to connect to ThingSpeak and send Data
    try:
        response = requests.post("https://api.thingspeak.com/update.json",params)
        print(response)
        

    #Catch the exception if the connection fails
    except:
        print("connection failed")

    time.sleep(interval)     
    
  


    

import time
import smbus2
import bme280

interval = 5
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object

while True:
    
    data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
    print("Data ID: ", data.id)
    print("Time: ", data.timestamp)
    print("Temperature: ", data.temperature)
    print("Pressure: ", data.pressure)
    print("Humidity: ", data.humidity)

    print("\n", data)
    time.sleep(interval) 

import serial 
import time 

arduino = serial.Serial(port='/dev/ttyACM0',   baudrate=9600, timeout=.1)
print(arduino.readline,"start")

def write_read(x): 
    arduino.write(bytes(x,'utf-8'))
    time.sleep(0.05)
    data = str(arduino.readline())  ## waithing te get a response of a target pose being succesfullly used #will prevent it from overflowing
    print(data)
x = 0
while True:
    print(str(x))
    write_read(str(x))
    print(str(x))
    x += 1
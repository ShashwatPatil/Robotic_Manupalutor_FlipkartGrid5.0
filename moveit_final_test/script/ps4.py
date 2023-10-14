import serial
import time
from pyPS4Controller.controller import Controller

# Arduino connected to Raspberry Pi via USB cable
# Serial communication between arduino and Raspberry Pi
serialobject = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
    
    
class MyController(Controller):    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_down(self, value): #servo1 down ie increment angle 
        if  super().on_L3_down(value) == None:
            serialobject.write(b'a')
            print('a')

    def on_L3_up(self, value):  #servo1 up ie decrement angle 
        if super().on_L3_up(value) == None: 
            serialobject.write(b'b')
            print('b')
    
    def on_L3_left(self, value): #myservo(base) to left -- increment angle 
        if super().on_L3_left(value) == None:
            serialobject.write(b'c')
            print('c')
    
    def on_L3_right(self, value): # myservo to right  --- decrement angle
        if super().on_L3_right(value) == None:
            serialobject.write(b'd')
            print('d')
    
    def on_R3_up(self, value):  # turn vaccume off
        if  super().on_R3_up(value)== None:
            serialobject.write(b'e')
            print('e')


    def on_R3_down(self, value): #turn vaacme on  
        if  super().on_R3_down(value)== None:
            serialobject.write(b'f')
            print('f')


    def on_R2_press(self, value): # go to default location 
        if  super().on_R2_press(value)== None:
            serialobject.write(b'g')
            print('g')


    def on_R3_left(self, value): # 35 kg servo up   ie decrement angle 
        if  super().on_R3_left(value)== None:
            serialobject.write(b'h')
            print('h')


    def on_R3_right(self, value): # 35kg servo down ie increment angle 
        if  super().on_R3_right(value)== None:
            serialobject.write(b'i')
            print('i')


    def on_R3_press(self):
        serialobject.write(b'j')
        print('j')
        return super().on_R3_press()
    
    def on_up_arrow_press(self): #spider bot servo up  ie decrement angle 
        serialobject.write(b'k')
        print('k')    
        return super().on_up_arrow_press()

    def on_down_arrow_press(self): #spider bot serrvo down ie increment angle 
        serialobject.write(b'l')
        print('l')
        return super().on_down_arrow_press()

    def on_left_arrow_press(self): # mg95 meve left increment angle 
        serialobject.write(b'm')
        print('m')
        return super().on_left_arrow_press()
    
    def on_right_arrow_press(self): # mg95 move right decrement angle 
        serialobject.write(b'n')
        print('n')
        return super().on_right_arrow_press()

    def on_L1_press(self): 
        serialobject.write(b'o')
        print('o')
        return super().on_L1_press()

    def on_playstation_button_press(self):
        serialobject.write(b'p')
        print('p')        
        return super().on_playstation_button_press()
    
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
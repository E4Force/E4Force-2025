from machine import Pin, PWM, I2C
from time import sleep, sleep_ms
from servo import *
from motors import *
from hc_sr04 import *			# Library made by Roberto Sánchez, https://github.com/rsc1975/micropython-hcsr04.git
import utime
from apds9960.const import *					# https://github.com/liske/python-apds9960.git
from apds9960 import uAPDS9960 as APDS9960
from color import *
from timer import *


gp20 = Pin(20,Pin.IN)
gp21 = Pin(21,Pin.IN)

motor = m1()

motor.stop()

servo.center(13)



while True:
    
    if gp21.value() == False:
                
        white_calibration()
        sleep(.5)
        motor.forward(96)
        
        break
    
    
while True:
    
    COLOR_DOWN()
    if COLOR_DOWN() == "Red":
        motor.forward(93)
        servo.left(13)
        
        while True:
            COLOR_DOWN()
            if COLOR_DOWN() == "Blue":
                
                
                           
                
                sleep(.4)
            
                servo.center(13)
                motor.forward(96)
                sleep(.5)
           
                break
    elif COLOR_DOWN() == "Blue":
        motor.forward(93)
    
        servo.right(13)
        while True:
            COLOR_DOWN()
            if COLOR_DOWN() == "Red":
            
                
                sleep(.4)
                motor.forward(96)
                servo.center(13)
                sleep(.5)
                  
                break
while True:
    COLOR_FRONT()
    if COLOR_FRONT() == "Red":
        
        servo.left(13)
        sleep(1.5)
        servo.right(13)
        sleep(1)
        servo.center(13)
        sleep(.5)
        
        
    elif COLOR_FRONT() == "Blue":
        
        servo.right(13)
        sleep(1.5)
        servo.left(13)
        sleep(1)
        servo.center(13)
        sleep(.5)
        
    
    else:
        pass
        
        
        
        
    
    
    
    
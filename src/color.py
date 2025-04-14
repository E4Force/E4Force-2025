from machine import Pin, PWM, I2C
from time import sleep, sleep_ms			
import utime
from apds9960.const import *					# https://github.com/liske/python-apds9960.git
from apds9960 import uAPDS9960 as APDS9960

RED = 0
GREEN = 1
BLUE = 2
DOWN = [1,1,1]
FRONT = [1,1,1]
COLOR_COMP = [1,1,1]

WHITE_POINT = .9
try:
    #it tries to connect the front color sensors (GROVE 4)
    i2c_front = I2C(0, scl = Pin(17), sda = Pin(16), freq = 300000)
    front = APDS9960(i2c_front)
    print("Front Sensor Connected")
    
except OSError as e:
	#if it fails to connect it will produce an error message.

    print("Error initializing", e)

try:
    #it tries to connect the down color sensors (GROVE 6)
    i2c_down = I2C(1, scl = Pin(27), sda = Pin(26), freq = 300000)
    down = APDS9960(i2c_down)
    print("Lower Sensor Connected")
    
except OSError as e:
	#if it fails to connect it will produce an error message.
    print("Error initializing", e)

def read():
	global RED, GREEN, BLUE, DOWN, FRONT, COLOR_COMP
	front.enableLightSensor()
	down.enableLightSensor()
	sleep((2.78 * (256 - APDS9960_DEFAULT_ATIME))/1000)
	FRONT = (front.readRedLight()*COLOR_COMP[RED], front.readGreenLight()*COLOR_COMP[GREEN], front.readBlueLight()*COLOR_COMP[BLUE])
	DOWN = (down.readRedLight()*COLOR_COMP[RED], down.readGreenLight()*COLOR_COMP[GREEN], down.readBlueLight()*COLOR_COMP[BLUE])

def white_calibration():
    global RED, GREEN, BLUE, DOWN, FRONT, COLOR_COMP
    front.enableLightSensor()
    down.enableLightSensor()
    for i in range(10):
        sleep(2.78 * ((256 - APDS9960_DEFAULT_ATIME)/ 1000))
        DOWN[RED] += (down.readRedLight())
        DOWN[GREEN] += (down.readGreenLight())
        DOWN[BLUE] += (down.readBlueLight())
        
    DOWN[RED] /= 10 
    DOWN[GREEN] /= 10 
    DOWN[BLUE] /= 10 

    if DOWN[GREEN] <= DOWN[RED] >= DOWN[BLUE]:
    	COLOR_COMP[RED] = 1
    	COLOR_COMP[GREEN] = DOWN[RED] / DOWN[GREEN]
    	COLOR_COMP[BLUE] = DOWN[RED] / DOWN[BLUE]
    
    elif DOWN[RED] <= DOWN[GREEN] >= DOWN[BLUE]:
    	COLOR_COMP[RED] = DOWN[GREEN] / DOWN[RED]
    	COLOR_COMP[GREEN] = 1 
    	COLOR_COMP[BLUE] = DOWN[GREEN] / DOWN[BLUE]
   
    elif DOWN[RED] <= DOWN[BLUE] >= DOWN[GREEN]:
        COLOR_COMP[RED] = DOWN[BLUE] / DOWN[RED]
        COLOR_COMP[GREEN] = DOWN[BLUE] / DOWN[GREEN]
        COLOR_COMP[BLUE] = 1
   
    else:
    	pass

def COLOR_DOWN():
	global RED, GREEN, BLUE, DOWN, FRONT, COLOR_COMP, WHITE_POINT
	read()

	if DOWN[GREEN] <= DOWN[RED] >= DOWN[BLUE]:
		if (DOWN[GREEN] / DOWN[RED]) >= WHITE_POINT and (DOWN[BLUE] / DOWN[RED]) >= WHITE_POINT:
			return"White"
		else:
			return"Red"
	elif DOWN[GREEN] <= DOWN[BLUE] >= DOWN[RED] or DOWN[BLUE] <= DOWN[GREEN] >= DOWN[RED]:
		if (DOWN[GREEN] / DOWN [BLUE]) >= WHITE_POINT and (DOWN[RED] / DOWN[BLUE]) >= WHITE_POINT or (DOWN[BLUE] / DOWN [GREEN]) >= WHITE_POINT and (DOWN[RED] / DOWN[GREEN]) >= WHITE_POINT :
			return"White"
		else:
			return"Blue"
		

 
		

def COLOR_FRONT():
	global RED, GREEN, BLUE, DOWN, FRONT, COLOR_COMP, WHITE_POINT
	read()

	if FRONT[GREEN] <= FRONT[RED] >= FRONT[BLUE]:
		if (FRONT[GREEN] / FRONT[RED]) >= WHITE_POINT and (FRONT[BLUE] / FRONT[RED]) >= WHITE_POINT:
			return"White"
		else:
			return"Red"
	elif FRONT[GREEN] <= FRONT[BLUE] >= FRONT[RED]:
		if (FRONT[RED] / FRONT[BLUE]) >= WHITE_POINT and (FRONT[GREEN] / FRONT[BLUE]) >= WHITE_POINT:
			return"White"
		else:
			return"Blue"
		
	elif FRONT[BLUE] <= FRONT[GREEN] >= FRONT[RED]:
		if (FRONT[BLUE] / FRONT [GREEN]) >= WHITE_POINT and (FRONT[RED] / FRONT[GREEN]) >= WHITE_POINT:
			return"White"
		else:
			return"Green"

    
    
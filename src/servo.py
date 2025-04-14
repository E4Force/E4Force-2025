from machine import Pin, PWM
import time

previous = "center"

class servo:
    
    def left(pin):
        global previous
        move = PWM(Pin(pin))
        move.freq(50)
        move.duty_ns(1_000_000)
        previous = "left"

    def right(pin):
        global previous
        move = PWM(Pin(pin))
        move.freq(50)
        move.duty_ns(2_000_000)
        previous = "right"

        
    def degrees(pin, deg):
        global previous
        calculated_duty = (1500000 + (10000*deg))        
        if calculated_duty >= 600000 and calculated_duty <= 2400000:
            move = PWM(Pin(pin))
            move.freq(50)
            move.duty_ns(int(calculated_duty))        
        elif calculated_duty < 600000:
            move = PWM(Pin(pin))
            move.freq(50)
            move.duty_ns(600000)                        
        elif calculated_duty > 2400000:
            move = PWM(Pin(pin))
            move.freq(50)
            move.duty_ns(2400000)            
        else:
            print("Not allowed")
            
        if deg < 0:
            previous = "left"
            
        elif deg > 0:
            previous = "right"
            
        elif deg == 0:
            previous = "center"
           
    def center(pin):
        compensation = 20
        global previous
        move = PWM(Pin(pin))
        move.freq(50)
        if previous == "center":		# No compensation is needed, hence the degrees are 0
            servo.degrees(pin, 0)           
        elif previous == "left":					# Some compensation is needed to make the car go straight
            servo.degrees(pin, compensation)		# hence the compensation where the 0 degrees would go        
        elif previous == "right":					# since there is some play in the rack and pinion
            servo.degrees(pin, -compensation)
        
                    
    def stop(pin):
        move = PWM(Pin(pin))
        move.deinit()
        
    def test(pin):
        servo.center(pin)
        time.sleep(1)
        servo.left(pin)
        time.sleep(1)
        servo.center(pin)
        time.sleep(1)
        servo.right(pin)
        time.sleep(1)
        servo.center(pin)
        

        

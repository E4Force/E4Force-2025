from machine import Pin, PWM

class m1:
    
    def __init__(self, freq=120):
        self.m1a = PWM(Pin(8))
        self.m1b = PWM(Pin(9))
        self.m1a.freq(freq)
        self.m1b.freq(freq)
        
    def forward(self, speed):
        self.m1a.duty_u16(int(2**(speed/6.25)))
        self.m1b.duty_u16(0)
        
    def reverse(self, speed):
        self.m1a.duty_u16(0)
        self.m1b.duty_u16(int(2**(speed/6.25)))
        
    def stop(self):
        self.m1a.duty_u16(0)
        self.m1b.duty_u16(0)
        
class m2:
    
    def __init__(self, freq=120):
        self.m2a = PWM(Pin(10))
        self.m2b = PWM(Pin(11))
        self.m2a.freq(freq)
        self.m2b.freq(freq)
        
    def forward(self, speed):
        self.m2a.duty_u16(int(2**(speed/6.25)))
        self.m2b.duty_u16(0)
        
    def reverse(self, speed):
        self.m2a.duty_u16(0)
        self.m2b.duty_u16(int(2**(speed/6.25)))
        
    def stop(self):
        self.m2a.duty_u16(0)
        self.m2b.duty_u16(0)
        
class m3:
    
    def __init__(self, freq=120):
        self.m3a = PWM(Pin(12))
        self.m3b = PWM(Pin(13))
        self.m3a.freq(freq)
        self.m3b.freq(freq)
        
    def forward(self, speed):
        self.m3a.duty_u16(int(2**(speed/6.25)))
        self.m3b.duty_u16(0)
        
    def reverse(self, speed):
        self.m3a.duty_u16(0)
        self.m3b.duty_u16(int(2**(speed/6.25)))
        
    def stop(self):
        self.m3a.duty_u16(0)
        self.m3b.duty_u16(0)
        
class m4:
    
    def __init__(self, freq=120):
        self.m4a = PWM(Pin(14))
        self.m4b = PWM(Pin(15))
        self.m4a.freq(freq)
        self.m4b.freq(freq)
        
    def forward(self, speed):
        self.m4a.duty_u16(int(2**(speed/6.25)))
        self.m4b.duty_u16(0)
        
    def reverse(self, speed):
        self.m4a.duty_u16(0)
        self.m4b.duty_u16(int(2**(speed/6.25)))
        
    def stop(self):
        self.m4a.duty_u16(0)
        self.m4b.duty_u16(0)

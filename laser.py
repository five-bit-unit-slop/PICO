from machine import Pin, ADC
import utime

ldr = ADC(Pin(26))
laser = Pin(0, Pin.OUT)

for i in range(2):
    laser.value(i)

while True:
    print(ldr.read_u16())
    utime.sleep(1)
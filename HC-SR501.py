from machine import Pin
import utime

sensor = Pin(0, Pin.IN, Pin.PULL_DOWN)

while True:
    output = sensor.value()
    print(output)
    utime.sleep(1)
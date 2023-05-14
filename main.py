from machine import Pin,PWM
from utime import sleep
PIR =Pin(1, Pin.IN, Pin.PULL_DOWN)

while True:
    print(PIR.value())

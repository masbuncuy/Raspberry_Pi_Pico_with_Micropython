from machine import Pin
import utime

trigger = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)


def ultrasonic_sensor():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("Jarak dari objek adalah ", distance, "cm")


while True:
    ultrasonic_sensor()
    utime.sleep(1)

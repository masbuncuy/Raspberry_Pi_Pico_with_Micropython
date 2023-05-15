from machine import Pin, I2C
import utime as time
from dht11 import DHT11

while True:
    time.sleep(5)
    pin = Pin(3, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    print("suhu: {}". format(sensor.temperature))
    print("kelembapan: {}". format(sensor.humidity))

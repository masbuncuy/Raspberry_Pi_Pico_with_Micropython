from machine import Pin, I2C
import utime as time
from dht11 import DHT11

data = Pin(3, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(data)

while True:
    time.sleep(5)
    print("suhu: {}". format(sensor.temperature))
    print("kelembapan: {}". format(sensor.humidity))

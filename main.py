from machine import Pin
import utime as time

#import file dht11.py
from dht11 import DHT11

#deklarasi pin data
data = Pin(3, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(data)

while True:
    #kita kasih delay 5 detik
    time.sleep(5)
    print("Suhu : {}".format(sensor.temperature))
    print("Kelembapan: {}".format(sensor.humidity))

from machine import Pin
import utime as time

flame = Pin(1, Pin.IN)

while True:
    while flame.value() == 0:
        print("Terdapat Titik Api")
        time.sleep(2)
    while flame.value() == 1:
        print("Tidak ada titik Api")
        time.sleep(2)

from machine import Pin
import utime as time

number = 0
PIR = Pin(1, Pin.IN, Pin.PULL_DOWN)
print("--------------- Pir -------------")
time.sleep(1)
print("---------------------------------")

while True:
    print("Nilai status pir sekarang: " . PIR.value())
    if PIR.value() == 1:
        print("Hayo Mau Gerak Kemana, kamu udah melakukan gerakan ke ", number + 1, "sekian kali")
    time.sleep(1)

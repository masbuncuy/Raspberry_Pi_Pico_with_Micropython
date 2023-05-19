# import  library mq2
from mq2 import MQ2

# untuk library waktu
import utime as time

# deklarasi pin ao
pin = 1

# set pin dan basVoltage
sensor = MQ2(pinData=pin, baseVoltage=3.3)

# panggil kalibrasi untuk melakukan kalibrasi
print("Kalibrasi")
sensor.calibrate()
print("Kalibrasi selesai")
print("Resistansi dasar:{}".format(sensor._ro))

# baca sensor

while True:
    print("Asap: {:1.f}".format(sensor.readSmoke()) + " - ", end="")
    print("LPG: {:1.f}".format(sensor.readLPG()) + " - ", end="")
    print("Metana: {:1.f}".format(sensor.readMethane()) + " - ", end="")
    print("Hidrogen: {:1.f}".format(sensor.readHydrogen()))

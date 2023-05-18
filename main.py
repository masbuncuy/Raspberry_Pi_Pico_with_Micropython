from mq2 import MQ2
import utime as time

pin = 1

sensor = MQ2(pinData=pin, baseVoltage=3.3)

print("Kalibrasi")
sensor.calibrate()
print("Kalibrasi selesai")
print("Resistansi dasar:{}".format(sensor._ro))

while True:
    print("Asap: {:.1f}".format(sensor.readSmoke()) + " - ", end="")
    print("LPG: {:.1f}".format(sensor.readLPG()) + " - ", end="")
    print("Metana: {:.1f}".format(sensor.readMethane()) + " - ", end="")
    print("Hidrogen: {:.1f}".format(sensor.readHydrogen()))
    time.sleep(1)
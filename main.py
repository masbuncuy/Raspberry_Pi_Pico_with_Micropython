from machine import Pin
import utime

# deklarasi trigger, trriger untuk pengirim sinyal ultrasonic
trigger = Pin(4, Pin.OUT)

# deklarasi echo, echo sebagai penerima sinyal ultrasonic
echo = Pin(5, Pin.IN)


def ultrasonic_sensor():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    # cek kondisi dari echo
    while echo.value() == 0:
        # sinyal mati
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        # sinyal hidup
        signalon = utime.ticks_us()

    timepassed = signalon - signaloff
    # jarak
    distance = (timepassed * 0.0343) / 2
    print("Jarak dari objek adalah ", distance, "cm")


while True:
    ultrasonic_sensor()
    utime.sleep(1)

from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(1))

#bisa diisi antara 10 - 12000
buzzer.freq(1000)

#untuk mengatur kenyaringan bisa diisi antara 0 - 1000
buzzer.duty_u16(1000)

sleep(1)

buzzer.duty_u16(0)



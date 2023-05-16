import utime as time
import tm1637
from machine import Pin

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
number = 0

while True:
    tm.write([0, 0, 0, 0])
    tm.show(str(number))
    time.sleep(1)
    number = number + 1

    while number == 9999:
        number = 0

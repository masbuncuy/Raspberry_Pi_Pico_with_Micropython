import utime as time

# import library / driver tm1637
import tm1637
from machine import Pin

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
# inisial awal nomor dimulai dari 0
number = 0

while True:
    # bersihkan tulisan di lcd
    tm.write([0, 0, 0, 0])
    # tampilkan nomor
    tm.show(str(number))
    # buat nomor bertambah satu setiap 1 detik
    time.sleep(1)
    number = number + 1

    # jika nomor = 9999 kembalikan ke angka 0
    while number == 9999:
        number = 0

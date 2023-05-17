from machine import Pin
import utime as time

#inisial pin flame sensor

flame = Pin(1, Pin.IN)

while True:
    #cek apakah terdapat titik api
    while flame.value() == 0:
        print("Terdapat Titik Api")
        # dikasih delay 2 detik
        time.sleep(2)
    #cek kembali jika tidak ada titik api
    while flame.value() == 1:
        print("Tidak Ada Titik Api")
        #kasih delay 2 detik
        time.sleep(2)

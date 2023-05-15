from machine import Pin, I2C
import ssd1306

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello World', 18, 0)
display.text('Dari MasBunCuy', 10, 16)
display.text('Semoga', 38, 32)
display.text('Bermanfaat', 24, 48)
display.show()

from ssd1306_lib import SSD1306_I2C
from machine import Pin, I2C

i2c = I2C(scl=Pin(2), sda=Pin(0))
oled = SSD1306_I2C(128, 64, i2c)
oled.text("hello world",0,0)
oled.show()


# Lcd.py

import RPi.GPIO
import adafruit_charlcd

lcd = Adafruit_CharLCD.Adafruit_CharLCD(pin_rs=14, pin_e=15, pins_db=[2,3,4,17])
lcd.clear()
lcd.message("Hello world !!!")

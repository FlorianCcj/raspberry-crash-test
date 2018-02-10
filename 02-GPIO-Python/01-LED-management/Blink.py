# Blink.py

# Import des modules
import RPi.GPIO as GPIO
import time

frequence = 200
pin = 3

# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)

# On fait clignoter la LED
while True:
    GPIO.output(pin, not GPIO.input(pin))
    time.sleep(1/frequence)

# Button.py

# Import des modules
import RPi.GPIO as GPIO
import time

class Pin:
    input_led = 12
    output_button = 19

    def __init__(self, *args, **kwargs):
        pass

pin = Pin()

print("led's input's pin: %d", pin.input_led)
print("button's output's pin: %d", pin.output_button)

# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin.input_led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin.output_button, GPIO.IN)

# Si on detecte un appui sur le bouton, on allume la LED 
# et on attend que le bouton soit relache
while True:
    state = GPIO.input(pin.output_button)
    print(state)
    if state:
        # on a appuye sur le bouton connecte sur la broche 19
        GPIO.output(pin.input_led, GPIO.HIGH)
        while state:
            print("button is close")
            state = GPIO.input(pin.output_button)
            time.sleep(0.02)  # Pause pour ne pas saturer le processeur
        GPIO.output(pin.input_led, GPIO.LOW)
    time.sleep(0.02)  # Pause pour ne pas saturer le processeur

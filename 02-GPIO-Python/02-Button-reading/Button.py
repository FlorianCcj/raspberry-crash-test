# Button.py

# Import des modules
import RPi.GPIO as GPIO
import time

LED_INPUT_PIN = 12
BUTTON_OUTPUT_PIN = 19
print("led's input's pin: %d", LED_INPUT_PIN)
print("button's output's pin: %d", BUTTON_OUTPUT_PIN)

# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_INPUT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.IN)

# Si on detecte un appui sur le bouton, on allume la LED 
# et on attend que le bouton soit relache
while True:
    state = GPIO.input(19)
    if not state:
        # on a appuye sur le bouton connecte sur la broche 19
        GPIO.output(LED_INPUT_PIN, GPIO.HIGH)
        while not state:
            print("button is close")
            state = GPIO.input(19)
            time.sleep(0.02)  # Pause pour ne pas saturer le processeur
        GPIO.output(LED_INPUT_PIN, GPIO.LOW)
    time.sleep(0.02)  # Pause pour ne pas saturer le processeur

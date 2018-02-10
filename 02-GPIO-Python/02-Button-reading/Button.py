# Button.py

# Import des modules
import RPi.GPIO
import time

# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.IN)

# Si on detecte un appui sur le bouton, on allume la LED 
# et on attend que le bouton soit relache
while True:
    state = GPIO.input(19)
    if not state:
        # on a appuye sur le bouton connecte sur la broche 19
        GPIO.output(12, GPIO.HIGH)
        while not state:
            state = GPIO.input(19)
            time.sleep(0.02)  # Pause pour ne pas saturer le processeur
        GPIO.output(12, GPIO.LOW)
    time.sleep(0.02)  # Pause pour ne pas saturer le processeur

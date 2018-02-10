README.md
# GPIO port management with python
from http://deusyss.developpez.com/tutoriels/RaspberryPi/PythonEtLeGpio/

## Rasp Theorie
### GPIO
penser a utiliser un buffers ou des octocouplers

IO de type CMOS => work with +3.3V
plug TTL cricuit (5V) without transfo => destroy rasp
#### I2C
il faut quelques bibliotheque pour piloté l I2C
sudo apt-get install build-essential libi2c-dev python-dev
sudo apt-get install libffi-dev i2c-tools
sudo pip install smbus-cffi

 * sudo raspi-config
 * advenced options -> I2C -> yes
 * reboot
 * test if I2C work -> lsmod | grep i2c_

#### SPI
sudo apt-get install python2.7-dev
sudo apt-get install python3-dev
sudo apt-get install libevent-dev
sudo pip install spidev

 * sudo raspi-config
 * advenced options -> SPI -> yes
 * reboot
 * test if SPI work -> lsmod | grep spi_
 
#### UART and other
 * sudo raspi-config
 * advenced options -> serial -> yes
 * reboot

## Python and GPIO
 * RPI.GPIO: pip install RPi.GPIO
 * if you don't have pip wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
 * GPIO port only accessible by sudo ...
### GPIO lib
```
import RPi.GPIO as GPIO
low state : GPIO.LOW or 0 or False
high state : GPIO.HIGH or 1 or True
```
#### config
2 numerous type
 * serigraphie du connecteur de la carte (GPIO.BOARD)
 * electronic numerous chip (GPIO.BCM)


`GPIO.setmode(GPIO.BOARD)`
or `GPIO.setmode(GPIO.BCM)`

#### config IO
```
# set pin 12 has num input
GPIO.setup(12, GPIO.IN)
# set pin 12 has num ouput
GPIO.setup(12, GPIO.OUT)
# set pin 12 has num ouput with initial state
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
```
#### read numeric input
`GPIO.input(12)`
#### change num output 
`GPIO.input(12, GPIO.LOW)`
`GPIO.input(12, not GPIO.input(12))`
#### dump num IO config
value possible : GPIO.INPUT, GPIO.OUTPUT, GPIO.SPI, GPIO.I2C, GPIO.HARD_PWN, GPIO.SERIAL, GPIO.UNKNOWN

```
state = GPIO.spio_function(pin)
print(state)
```
#### reset num IO
GPIO.cleanup()
#### PWM
Pulse width modulation : modulate high state duration
```
p = GPIO.PWM(channel, frequence)
p.start(rapport_cyclique) #ici, rapport_cyclique vaut entre 0.0 et 100.0
p.ChangeFrequency(nouvelle_frequence)
p.ChangeDutyCycle(nouveau_rapport_cyclique)
p.stop()
```
#### pull up and pull down
Don't understand ...
#### front interupt and detection
1st solution: stop
```
GPIO.wait_for_edge(channel, GPIO.RISING): stop the script until having a rising front (2nd argument can be GPIO.RISING, GPIO.FALLING, GPIO.BOTH)
```
2nd solution: loop
```
GPIO.add_event_detect(channel, GPIO.RISING)
While true:
  if GPIO.event_detected(channel):
    print('input detected')
```
3rd solution: thread
```
Def my_callback(channel):
  print('an event apened')

# add 75ms to don't have rebund effect
GPIO.add_event_detect(channel, GPIO.BOTH, callback=my_callback, bouncetime=75)

# remove interupt on a chan
GPIO.remove_event_detect(channel)
```

## Go further
KICAD: electronic conception software
Fritzing: electronic conception software
OSH PARK: to create card
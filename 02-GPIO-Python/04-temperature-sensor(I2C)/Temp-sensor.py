# Temp-sensor.py

import time
from smbus import SMBus
bus= SMBus(1)   # 1 indique qu'il faut utiliser le port /dev/i2c-1

while True:
    # Le composant porte l'adresse 0x48 (A0 et A1 relies à GND)
    # On va lire plusieurs octets a partir du registre 0
    data = bus.read_i2c_block_data(0x48, 0) 
    
    tempMSB = data[0]
    tempLSB = data[1]
    
    temperature=(((tempMSB << 8) + tempLSB) >>7) * 0.5
    if temperature > 128 :  # test si la temperature est negative
        # complement a 1 de la temperature
        temperature = (((((tempMSB << 8) + tempLSB) >>7 )* 0.5) -256)
            
    print(temperature)
    fichier = open ('fichier_anne_marie','a')
    fichier.write (str(temperature))
    fichier.write (',  ')
    fichier.close () 
    
    time.sleep(2)

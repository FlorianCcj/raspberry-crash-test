# install by torqu3e

ressources:
 * https://www.raspberrypi.org/forums/viewtopic.php?t=26795

* enter `iwconfig` it should be like in `./00-initial_iwconfig.sh`
* change interfaces `sudo vi /etc/network/interfaces` (or nano, or gedit or ... whatever you want) to add config like `./interfaces`
* (don't work for me) enter `wpa_passphrase myssid password` to have a hach of your password to don t have it in clear in your config
* then edit `/etc/wpa_supplicant/wpa_supplicant.conf` like `./wpa_supplicant.conf`, psk is the hach you took thanks to the previous command
* bring the interface up: `sudo ifup wlan0` you will have return like in `./ifup.sh`
# Wifi
## file to manage

`/etc/network/interfaces`
`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`: to add network

## synthax
```
ap_scan=1
network={
    ssid="nomDuReseau"
    proto= WPA RSN # don t if necessry 
    psk="cléDeSécurité"
    key_mgmt=WPA-PSK
}
```

if WEP key instead of WPA, put `NONE` as value in `key_mgmt`

## command
 * `ifconfig wlan0`: launch wifi
 * `iwlist wlan0 scan`: print available wifi
 * `/etc/init.d/networking restart`: restart wifi
 * `sudo iwconfig wlan0 essid <<SSID>>`: connect to ssid wifi 
 * `sudo iwconfig wlan0 key <<WEP KEY>>`: add key wep
 * `iwconfig`: config wifi
 * `ifdown wlan0` shutdown wifi
 * `ifconfig wlan0 down`: down
 * `man interfaces`: learn how to config /etc/network/interfaces

### config

 ## Resource
  * http://doc.ubuntu-fr.org
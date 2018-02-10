# server web

create by following the tutorial on: https://raspberry-pi.developpez.com/cours-tutoriels/serveur-web/

## Materiel
 * Raspberry pi
 * charger
 * screen
 * micor-SD card with raspbian on it

## basic configuration

### On raspi-config
 * expand_rootfs: expand raspbian particion to all card;
 * configure_keyboard: change keyboard disposition;
 * change_locale: switch language;
 * change_timezone: switch ... timezone;
 * ssh: to active ssh on server;
 * boot_behaviour: to unactive X server
 * memory_split: set 16 Mb to graphical chip
 * overlock: to active

### ssh config

don't let default port for ssh (22), you can choose between 1 and 65536
Don't use already used port : 21, 22, 80, 443
you can change it in /etc/ssh/sshd_config

In the same file :
 * PermitRootLogin : change yes to no
 * AllowUsers : add "pi"

### IPfix

in /etc/network/interfaces
```
auto lo
iface lo inet loopback

iface eth0 inet static
adress 192.168.0.x
gateway 192.168.0.x
netmask 255.255.255.0
```

## go install server

we use nginx, PHP and sqlite/mysql
 * check systeme: `aptitude update && aptitude full-upgrade`
 * add user: `groupadd www-data && usermod -a -G www-data www-data`
 * remove useless package: ```aptitude purge xserver-xorg xserver-xorg-core xserver-xorg-input-all xserver-xorg-input-evdev xserver-xorg-input-synaptics xserver-xorg-video-fbdev xserver-common xpdf xinit x11-common x11-utils x11-xkb-utils xarchiver screen pcmanfm penguinspuzzle lxde-common lxappearance lxde-icon-theme lxinput lxmenu-data lxpanel lxpolkit lxrandr lxsession lxsession-edit lxshortcut lxtask lxterminal leafpad dillo galculator gnome-icon-theme gnome-themes-standard gnome-themes-standard-data gpicview hicolor-icon-theme```
 * remove useless config file : `aptitude purge ~c`
 * install package for server: `aptitude -R install htop iftop nginx sendmail openssl ssl-cert php5 php5-dev php5-gd php5-fpm php5-cli php5-sqlite php5-curl php5-common php5-cgi php5-mysql sqlite php-pear php-apc autoconf automake autotools-dev libapr1 libtool curl libcurl4-openssl-dev php-xml-parser mysql-client mysql-server mutt vsftpd`

 ## Param

 cat > /etc/nginx/sites-available/default << _EOF_
 <<contenu du fichier de ./nginx/sites-available/defaul>>
_EOF_

with x.x.x.x ip of the server

### generate ssl key

openssl req -new -x509 -days 265 -nodes -out /etc/nginx/cert.pem -keyout /etc/nginx/cert.key && chmod 600 /etc/nginx/cert.pem && chmod 600 /etc/nginx/cert.key

### enlarge php data transfert

in /etc/php5/fpm/php.ini
 * upload_max_filesize: to 1000M
 * max_file: to 1000M
 * if owncloud, uncoment upload_tmp_dir and set to /srv/http/owncloud/data
 * create directory: `mkdir -p /srv/http/owncloud/data`

## Secu
 * set sudo password: sudo su && passwd
 * remove sudo: sudo aptitude purge sudo
 * to connect root: su -
 * secure mysql: mysql-secure-installation

### fail2ban
a small program which read log and service ... if multiple fail, ban thanks to iptable

 * install: aptitude -R install fail2ban
  * config: in /etc/fail2ban/jail.conf 
  * add /etc/fail2ban/filter.d
  * `service fail2ban restart`

### denyhost

* will stock ban in /etc/hosts.deny
* config /etc/denyhosts.conf, switch SUSPICIOUS_LOGIN_REPORT_ALLOWED_HOSTS to NO
* edit /var/lib/denyhosts/allowed-hosts to add frient ip
* service denyhosts restart

## access

todo ... but not now
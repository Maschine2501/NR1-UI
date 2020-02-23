Inspired by: https://github.com/diehardsk/Volumio-OledUI
This is a fork from diehrdsk/Volumio-OledUi

# Volumio-OledUI MK2

## To-Do: 
* Tune "Now-Playing" Screen (other fonts, position)
* Play- Pause- and Stop- Icons
* Bootup and Shutdown Logos
* More Buttons via GPIO
* remove one Rotary 

## Allready Done:
* Standby-Screen (when Playback is stoped, Time, Date and IP is Displayed)
* Automatic stop when playback is paused (value could be defined / declared)

## installation steps
```
sudo apt-get update
 
sudo apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio
 
sudo pip install --upgrade setuptools pip wheel
 
sudo pip install --upgrade socketIO-client-2 luma.oled
 
git clone https://github.com/Maschine2501/Volumio-OledUI.git
 
chmod +x ~/Volumio-OledUI/oledui.py
 
sudo cp ~/Volumio-OledUI/oledui.service /lib/systemd/system/
 
sudo systemctl daemon-reload
 
sudo systemctl enable oledui.service

reboot
```

## Hints


-when Volumio is configured to remember the last Playlist after reboot, some strange sh** happens:
If the last Playback was from a local drive (eg. USB), 
Artist and Trackinfo stay corrupt until another Playback-Source was selected.
(Will investigate it sometime later...)


### hardware
* Raspberry Pi 2B/3B/4B with Volumio2 image
* 3.2" 256x64 Pixels 4-wire SPI OLED Display with SSD1322 controller IC (e.g. ER-OLEDM032-1W)
* 4 Buttons (connected with "pull-down" Resistors: 1k to GPIO, 10K to Gnd)
* 1 Rotary Encoder with Push-Button icluded

### dependencies
* [RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
* [socketIO-client-2](https://pypi.python.org/pypi/socketIO-client-2)
* PIL
* [luma.oled](https://luma-oled.readthedocs.io/)

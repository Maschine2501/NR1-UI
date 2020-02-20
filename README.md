All Credits to: https://github.com/diehardsk

This is a fork from diehrdsk/Volumio-OledUi

I'm trying to change: 
* the "Now-Playing" Screen (other fonts, add File-Info and Playtime)
* Play- Pause- and Stop- Icons
* Bootup and Shutdown Logos
* More Buttons via GPIO
* remove one Rotary
* remove rotary Button
* implement a new State : standby,which displays time & ip


## hardware
* Raspberry Pi 2B/3B/4B with Volumio2 image
* 3.2" 256x64 Pixels 4-wire SPI OLED Display with SSD1322 controller IC (e.g. ER-OLEDM032-1W)

## dependencies
* [RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
* [socketIO-client-2](https://pypi.python.org/pypi/socketIO-client-2)
* PIL
* [luma.oled](https://luma-oled.readthedocs.io/)


### installation steps
```
git clone https://github.com/Maschine2501/BraunNR1-OledUI

chmod +x BraunNR1-OledUI/install.sh

cd BraunNR1-OledUI

sudo ./install.sh
```

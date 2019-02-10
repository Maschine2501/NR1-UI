# Volumio-OledUI
Whole project is designed for playback of internet radio streaming, nevertheless you can access some other media as well.
User interface allows you to control volume, queue position, load playlist file or music from Media Library, turn power off/on.

## hardware
* Raspberry Pi 2B/3B with Volumio2 image
* 3.2" 256x64 Pixels 4-wire SPI OLED Display with SSD1322 controller IC (e.g. ER-OLEDM032-1W)
* Two rotary encoders with pushbutton; 20 cycles per revolution
* Optional PCM5102 DAC

![Picture](img/connection.png?raw=true)

It's highly recommended to use pull-up resistors and debounce filter caps for rotary encoders.

## dependencies
* [RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
* [socketIO-client-2](https://pypi.python.org/pypi/socketIO-client-2)
* PIL
* [luma.oled](https://luma-oled.readthedocs.io/)

## install
enable SPI bus by adding
```
dtparam=spi=on
```
to /boot/config.txt -- it's a bit tricky because this file gets overwritten when Volumio system is updated to new version

### installation steps
```
sudo apt-get update
sudo apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio
sudo pip install --upgrade setuptools pip wheel
sudo pip install --upgrade socketIO-client-2 luma.oled
git clone https://github.com/diehardsk/Volumio-OledUI.git
chmod +x ~/Volumio-OledUI/oledui.py
sudo cp ~/Volumio-OledUI/oledui.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable oledui.service
reboot
```

### how to check the logs
```
sudo journalctl -fu oledui.service
```

Do not expect everything to work perfectly on your setup. You may run into problems which you need to solve by yourself.
There's no support hotline. ;-)

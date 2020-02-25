Inspired by: https://github.com/diehardsk/Volumio-OledUI
This is a fork from diehrdsk/Volumio-OledUi

# Volumio-OledUI MK2

Demo Video from early Build:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/WyBcdSjRcxg/0.jpg)](http://www.youtube.com/watch?v=WyBcdSjRcxg "Video-Sample")

## To-Do: 
* Tune "Now-Playing" Screen (other fonts, position)
* Play- Pause- and Stop- Icons
* Bootup and Shutdown Logos
* More Buttons via GPIO
* remove one Rotary 

* ? Use "CAVA" to display a bargraph spectrum ?

## Allready Done:
* Standby-Screen (when Playback is stoped, Time, Date and IP is Displayed)
* Automatic stop when playback is paused (value could be defined / declared)

## installation steps (stable release)
```
If not done yet, set local system time zone:

sudo dpkg-reconfigure tzdata

Step 1:

sudo apt-get update
 
sudo apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio
 
sudo pip install --upgrade setuptools pip wheel
 
sudo pip install --upgrade socketIO-client-2 luma.oled

### Step 1 needs to be done once, not every time you want to update.

Step 2:

git clone https://github.com/Maschine2501/Volumio-OledUI.git
 
chmod +x ~/Volumio-OledUI/oledui.py
 
sudo cp ~/Volumio-OledUI/oledui.service /lib/systemd/system/
 
sudo systemctl daemon-reload
 
sudo systemctl enable oledui.service

reboot
```

## installation steps (nightly build)
(Some changes, but not everything working properly)

### 24.02.2020:
- added newFormat, newSamplerate and newBitdepth
- actual goal is: show File-Format (Flac, Mp3...), Samplerate and Bitdepth on NowPlayingScreen
newFormat = eg. 'flac'         (row6)
newSamplerate = eg. '44.1 khz' (row7)
newBitdepth = eg. '16 bit'     (row8)
#### bug:
- only 'newFormat' is displayed.
- newSamplerate and newBitdepth get lost on the way from "onPushState" to "UpdatePlayingInfo"
- therefore: set some 'print()' actions in the code.
- print is labled (from start -> End) A -> AA -> AAA -> Row6
```
Step 1:

If not done yet, set local system time zone:

sudo dpkg-reconfigure tzdata

sudo apt-get update
 
sudo apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio
 
sudo pip install --upgrade setuptools pip wheel
 
sudo pip install --upgrade socketIO-client-2 luma.oled
 
### Step 1 need to be done once, not every time you want to update.

Step 2:

git clone https://github.com/Maschine2501/Volumio-OledUI.git
 
chmod +x ~/Volumio-OledUI/oledui-nightly.py
 
sudo cp ~/Volumio-OledUI/oledui-nightly.service /lib/systemd/system/
 
sudo systemctl daemon-reload
 
sudo systemctl enable oledui-nightly.service

reboot
```

## installation steps (Update)
```
### for stable:

sudo systemctl disable oledui.service

sudo rm -r Volumio-OledUI

### for nightly:

sudo systemctl disable oledui-nightly.service

sudo rm -r Volumio-OledUI

### after the steps above, follow Step 2 from "installation steps"
```

## Check the logs

#### for the stable build

sudo journalctl -fu oledui.service

#### for the nightly build:

sudo journalctl -fu oledui-nightly.service

## Hints

-when Volumio is configured to remember the last Playlist after reboot, some strange sh** happens:
If the last Playback was from a local drive (eg. USB), 
Artist and Trackinfo stay corrupt until another Playback-Source was selected.
(Will investigate it sometime later...)

## Wiring

... needs to be done
(more shematics will come later)

![Alt text](/img/connection.png?raw=true "wiring")

![Alt text](/img/button.png?raw=true "button mapping")

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

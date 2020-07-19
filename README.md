Inspired by: [diehardsk/Volumio-OledUI](https://github.com/diehardsk/Volumio-OledUI)

### This is the Python3 version of [Maschine2501/Volumio-OledUI](https://github.com/Maschine2501/Volumio-OledUI/)
---

# NR1-UI
Im building a Network Hifi Receiver from scratch.
Main components are a RaspberryPi4 and an HiFi-Berry-Dac.
An old Braun T2 Tuner serves as case for the player.
To keep as much as possible from the look of the device i needed an Interface for Volumio.
And especialy one that supports a 3,2" ssd1322 SPI Oled with 256x64Pixel.
After doing some research i found diehrdsk/Volumio-OledUI.
It fullfills many points on my "wishlist" but not nearly all.
As we all know, the way is the destination, i spent some time (much time....) in modifying the original code.
Unfortuneatly luma.oled does not support Python2 anymore.
So this ist the new version, now depending on python 3.5.2

The project is not finished yet... but close the the goal!

## The Code is now modular:

### To select your display, just change [line 68](https://github.com/Maschine2501/NR1-UI/blob/4d433d40e5b2f0adb7ab96d051b265fadb3e26c7/nr1ui.py#L68) in nr1ui.py
### To change the look just edit [line66](https://github.com/Maschine2501/NR1-UI/blob/4d433d40e5b2f0adb7ab96d051b265fadb3e26c7/nr1ui.py#L66) in nr1ui.py to the desired Screen:

#### Screen1 (ssd1322):
![ssd1322-Screen1](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/ssd1322-Screen1.gif)
#### Screen2 (ssd1322):
![ssd1322-Screen2](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/ssd1322-Screen2.gif)
#### Screen3 (ssd1322):
![ssd1322-Screen3](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/ssd1322-Screen3.gif)
#### Screen4 (ssd1322):
![ssd1322-Screen4](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/ssd1322-Screen4.gif)
#### Screen1 (ssd1306):
![ssd1306-Screen1](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/ssd1306-Screen1.gif)
#### Screen4 (ssd1306):
![ssd1306-Screen4](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/ssd1306-Screen4.gif)

## Features of Maschine2501/NR1-UI:
---
* 4 Button Interface (Button function depends on "State" of the screen, e.g. playback, menu...)
* 1 Rotary with button (function also depends on "State")
* Playback Screen with Artist, Song, file-format, samplerate and bitdepth
* Standby-Screen with Time, Date and IP-Adress
* 3 Menu Screens (Media-Library, Playlists, Queue)
* Button-Layout-Icons on each Screen (depending on "State")
* Media-Library-Information Screen (Statistics about your Media-Library -> Artists, Albums, Songs, total Playtime)
* Boot and Shutdown Logo
* interaction with standby module ([hardware](https://github.com/Maschine2501/NR1-UI/wiki/Standby-Module)
* shutdown interaction with SIGNAL (SIGTERM)
* 8 LED's controlled by an PCF8574T (i2c gpio-extender) -> Cpu-load on 5 LED's, power-, play- and stere-indicator.
* IP adress is selected automaticaly (eth0 or wlan0)
* Playback-"progress bar"
* spectrum display -> "CAVA" is used to display a bargraph spectrum
* easy customization -> realized by a "config"-part at the beginning of the code
* compatible with ssd1306(i2c) and ssd1322(spi) oled displays
* versions without spectrum for ssd1322 and ssd1306 displays
* selectable if you use led's or not -> further selection: LED's by GPIO or i2c extender connected
* selectable if you use external standby equipment -> if so: automatic shutdown!
* All-in-one Version (for both: ssd1306 and ssd1322)
* Screen-Layouts -> selectable in line66 oledui.py
* Added an "Playback-Indicator-Icon" to the NowPlayingScreen
* moved all Layout related stuff to a config file, for more easy handling [(./config/ScreenConfig.py)](https://github.com/Maschine2501/NR1-UI/blob/master/config/ScreenConfig.py)
* maybe more features will come... ^^

* Some bugs will (not often) happen. Will debug it soon.

## To-Do: 
---
- [ ] Tune the whole UI (fonts, positions... etc.)
- [ ] Add RS232 -> Braun Master Control communication
- [ ] Make versions for other displays? like ssd1351, ssd1309? Maybe...
- [ ] A VU-Meter Screen?

## Allready Done:
---
- [x] Standby-Screen (when Playback is stoped, Time, Date and IP is Displayed)
- [x] Automatic stop when playback is paused (value could be defined / declared)
- [x] display Fileformat/Samplerate/Bitdepth in the NowPlayingScreen
- [x] Scroll Text stops before shown completly -> text was defined as scrollText, which makes "black"-boxes arround the text
- [x] one rotary removed
- [x] 4 more Buttons via GPIO (needs some fine tuning)
- [x] MediaInformationScreen (volumio.local/api/v1/collectionstats)
- [x] Icons for the function of each button, depending on "state"
- [x] migration to Python 3.5.2
- [x] implemented an SIGTERM handler
- [x] implemented a new StandbyLED module
- [x] implemented a logic to select the active network card and display it`s IP
- [x] removed Volume Screen and Volume interactions completely
- [x] Add a "progress bar" for Playback
- [x] integrated "CAVA" to display a bargraph spectrum
- [x] added a "config"-part at the beginning of the code, to configure the whole display for your needs
- [x] added a ssd1306 Version
- [x] addes versions without spectrum for ssd1322 and ssd1306 displays
- [x] Combine all Versions to one Code (with configuration at the begining)
- [x] Make More Screen-Layouts -> selectable by config
- [x] Add an "Playback-Indicator-Icon" to the NowPlayingScreen

## [Project on Volumio-Forum](https://forum.volumio.org/256x64-oled-ssd1322-spi-buttons-rotary-interface-t14098.html#p72945)

---

## [Basic Installation Steps <-> First Installation](https://github.com/Maschine2501/NR1-UI/wiki/Basic-Installation-Steps-----First-Installation)

---
## [Installation steps (NR1UI)](https://github.com/Maschine2501/NR1-UI/wiki/Installatin-steps-(NR1UI))
---
## Configuration Manual (will follow soon!)

---


### [wiring / button-layout / truthtable](https://github.com/Maschine2501/NR1-UI/wiki/wiring-and-button-truth-table)
---

### [hardware](https://github.com/Maschine2501/NR1-UI/wiki/hardware)
---

### [dependencies](https://github.com/Maschine2501/NR1-UI/wiki/dependencies)
---

### [font-info and source](https://github.com/Maschine2501/NR1-UI/wiki/font-information-(source))
---

## Your Display is not supported yet? You have an idea for a function/feature?

### [contact me :-)](mailto:Maschine2501@gmx.de?subject=[GitHub]%20Source%20Han%20Sans)

---

### [buy me a coffee, or tip me ;-)](https://paypal.me/maschine2501)

![MS2501](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/MS2501.png)

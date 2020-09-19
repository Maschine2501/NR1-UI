Inspired by: [diehardsk/Volumio-OledUI](https://github.com/diehardsk/Volumio-OledUI)

## 13.09.2020 Upgrade to Python3.8.5

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

I try to assist you, if you got questions or even problems with the code, just contact me.

Time by time more informations in the [wiki](https://github.com/Maschine2501/NR1-UI/wiki) will follow...

## The Code is now modular:

### To modify your Layout use the [config files](https://github.com/Maschine2501/NR1-UI/tree/master/config) -> [here](https://github.com/Maschine2501/NR1-UI/wiki/Styling-Modification-Basics) is a little instruction about it.

### To select your display, just change [line 68](https://github.com/Maschine2501/NR1-UI/blob/7be15f426592573882ba3fdfc91f5898ab6e5aa4/nr1ui.py#L68) in nr1ui.py

### To change the look/layout just press Button-C in "Standby-Screen" (Clock), select the desired Layout with the Rotary-Rotation and push the Rotary once to apply selection -> 
![Screenselect](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screenselect.png)

#### Base ssd1322 (on all Layouts the same):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322%20(2).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322%20(3).png)
#### Spectrum-Left (ssd1322):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen1%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen1%20(2).png)
#### Spectrum-Center (ssd1322):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen2%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen2%20(2).png)
#### Spectrum-Right (ssd1322):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen3%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen3%20(2).png)
#### No-Spectrum (ssd1322):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen4%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen4%20(2).png)
#### Modern (ssd1322):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen5%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen5%20(2).png)
#### VU-Meter-1 (ssd1322):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen6%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen6%20(2).png)
#### VU-Meter-2 (ssd1322):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen7%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen7%20(2).png)
#### VU-Meter-Bar (ssd1322):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen8%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screen8%20(2).png)

#### Base ssd1306 (on all Layouts the same):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1306%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1306%20(2).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1306%20(3).png)
#### Spectrum-Screen (ssd1306):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1306Screen1%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1306Screen1%20(2).png)
#### Progress-Bar (ssd1306):
![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1306Screen2%20(1).png) ![](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1306Screen2%20(2).png)
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
* Screen-Layouts are aviable
* Screen-Layouts are conviniently selectable in a dedicated Menu
* maybe more features will come... ^^

* Some bugs will (not often) happen. Will debug it soon.

## To-Do: 
---
- [ ] Tune the whole UI (fonts, positions... etc.)
- [ ] Add RS232 -> Braun Master Control communication
- [ ] Make versions for other displays? like ssd1351, ssd1309? Maybe...
- [ ] More Layouts and redesigning the existing ones


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
- [x] A VU-Meter Screen
- [x] Screen selection Menu (Aviable in Stand-ByScreen (clock) by pressing button-C)
- [x] VU-Meter-Bar-Layout -> Thanks Mihai for the Background Image! <3
- [x] Peak-Hold enabled in VU-Meter-Bar-Layout -> Thanks [almajiro](https://github.com/almajiro) for providing a sample! <3
- [x] Scrolling-Text is back!
- [x] Tidal Playback is functional now
- [x] Simplyfied installation routine by using a bassh-script
- [x] Upgrade to latest Python (3.8.5) -> Alternative installation!
- [x] added a configuration script to [installer](https://github.com/Maschine2501/NR1-UI/wiki/Installation-Steps-(for-Python3.8.5-Version---Autoconfig-Bash-Script))
- [x] Python 3.5 (Support ends 13. september 2020) -> Upgrade to latest posssible version 
- [x] PIP 21.0 (Support ends January 2021) -> Upgrade to latest posssible version

## [Project on Volumio-Forum](https://community.volumio.org/t/oled-user-inteface-for-volumio-with-rotary-and-4-buttons-modular-highly-configurable-supports-ssd1306-and-ssd1322/40378?u=maschine2501)

---

## [Basic Installation Steps <-> First Installation](https://github.com/Maschine2501/NR1-UI/wiki/Basic-Installation-Steps-----First-Installation)

---
## [Main-Installation steps (Python 3.5.2) (Bash-Script)](https://github.com/Maschine2501/NR1-UI/wiki/Installation-Steps-(Bash-Script))

# [Main-Installation steps (Python 3.8.5) (Bash-Script)](https://github.com/Maschine2501/NR1-UI/wiki/Installation-Steps-(for-Python3.8.5-Version---Bash-Script))
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

## Discord Server for direct contact:
### [Click here to join...](https://discord.gg/GJ4ED3F)

---

## You want to use a display which is not supported yet?
### If you're willing to sponsor me the specific Display, I will implement it.

---

### [buy me a coffee, or tip me ;-)](https://paypal.me/maschine2501)

![MS2501](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/MS2501.png)

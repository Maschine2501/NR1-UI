Inspired by: [diehardsk/Volumio-OledUI](https://github.com/diehardsk/Volumio-OledUI)

### This is the Python3 version of [Maschine2501/Volumio-OledUI](https://github.com/Maschine2501/Volumio-OledUI/)
---

# NR1-UI
Im building a Network Hifi Receiver from scratch.
An old Braun T2 Tuner serves as case for the player.
To keep as much as possible from the look of the device i needed an Interface for Volumio.
And especialy one that supports a 3,2" ssd1322 SPI Oled with 256x64Pixel.
After doing some research i found diehrdsk/Volumio-OledUI.
It fullfills many points on my "wishlist" but not nearly all.
As we all know, the way is the destination, i spent some time (much time....) in modifying the original code.
Unfortuneatly luma.oled does not support Python2 anymore.
So this ist the new version, now depending on python 3.5.2

The project is not finished yet... but close the the goal!

![ssd1322-1](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/BootupAndPlayback1322.gif)

![ssd1322-2](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/QueueWebradio1322.gif)

![ssd1322-3](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/StandbyMediaLibrayInfo1322.gif)

![ssd1306-1](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/BootPlayback1306.gif)

![ssd1306-2](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/QueueWebradio1306.gif)

![ssd1306-3](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/gif/StandByMediaLibraryInfo1306.gif)

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
* maybe more features will come... ^^

* Some bugs will (not often) happen. Will debug it soon.

## To-Do: 
---
- [ ] Tune the whole UI (fonts, positions... etc.)
- [ ] Add RS232 -> Braun Master Control communication
- [ ] Make versions for other displays? like ssd1306, ssd1309? Maybe...

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

## [Project on Volumio-Forum](https://forum.volumio.org/256x64-oled-ssd1322-spi-buttons-rotary-interface-t14098.html#p72945)

---

## [Basic Installation Steps <-> First Installation](https://github.com/Maschine2501/NR1-UI/wiki/Basic-Installation-Steps-----First-Installation)

---
## [Installation steps (ssd1322 with spectrum)](https://github.com/Maschine2501/NR1-UI/wiki/Installation-steps-(ssd1322-with-spectrum))
---
## [Installation steps (ssd1322 without spectrum)](https://github.com/Maschine2501/NR1-UI/wiki/Installation-steps-(ssd1322-without-spectrum))
---
## [Installation steps (ssd1306 with spectrum)](https://github.com/Maschine2501/NR1-UI/wiki/Installation-steps-(ssd1306-with-spectrum))
---
## [Installation steps (ssd1306 without spectrum)](https://github.com/Maschine2501/NR1-UI/wiki/Installation-steps-(ssd1306---without-spectrum))
---
## [Installation steps (Braun NR1 specific)](https://github.com/Maschine2501/NR1-UI/wiki/Installation-steps-(Braun-NR1-specific))
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

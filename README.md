Inspired by: [diehardsk/Volumio-OledUI](https://github.com/diehardsk/Volumio-OledUI)

### This is the Python3.8.5 version of [Maschine2501/Volumio-OledUI](https://github.com/Maschine2501/Volumio-OledUI/)

## February 2021:
#### Hi everyone, I created a small survey about my code:
### https://www.survio.com/survey/d/O5U8Y8N3M6V2O4X4Y
#### I would appreciate it very much if you guys would answer this survey!
### Thanks a lot! :-)
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

## 07.11.2020: You can choose if you want to use CAVA (Spectrum/VU) during setup. 
#### This should be usefull if you don't use a RPi4 (resourcefriendly, but no Spectrum/VU) 
#### Thank you Mihai for this Idea!

## The Code is now modular:

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

## [Features](https://github.com/Maschine2501/NR1-UI/wiki/Features)

## To-Do: 
---
- [ ] Tune the whole UI (fonts, positions... etc.)
- [ ] Add RS232 -> Braun Master Control communication
- [ ] Make versions for other displays? like ssd1351, ssd1309? Maybe...
- [ ] More Layouts and redesigning the existing ones
- [ ] Make an un-installer Script...
- [ ] Make an Volumio-Plugin for NR1-UI
- [ ] Re-implement a second Rotary for Volume Control (selectable in Installation Config Menu)

## [Allready Done](https://github.com/Maschine2501/NR1-UI/wiki/Allready-Done)


## [Project on Volumio-Forum](https://community.volumio.org/t/oled-user-inteface-for-volumio-with-rotary-and-4-buttons-modular-highly-configurable-supports-ssd1306-and-ssd1322/40378?u=maschine2501)

---

## [Basic Installation Steps <-> First Installation](https://github.com/Maschine2501/NR1-UI/wiki/Basic-Installation-Steps-----First-Installation)

---

# [Main-Installation steps (Python 3.8.5) (Bash-Script)](https://github.com/Maschine2501/NR1-UI/wiki/Installation-Steps-(for-Python3.8.5-Version---Autoconfig-Bash-Script))
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


## Does it work with Spotify or Squeezelite Addin?
### Probably yes. 
### I have tested the Spotify plugin: There is a problem with the delivered dataset, it is sometimes not complete after startup, this can crash nr1-ui. 
### Squeezlite does not match my philosophy of use, so I will not support this (which does not mean that it does not work....)

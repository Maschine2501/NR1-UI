Inspired by: [diehardsk/Volumio-OledUI](https://github.com/diehardsk/Volumio-OledUI) // 
This is the Python3.8.5 version of [Maschine2501/Volumio-OledUI](https://github.com/Maschine2501/Volumio-OledUI/)

# 06.09.2021 Workaround found:
[2aCD](https://github.com/2aCD-creator) has found a workaround for the "build-essential"-issue: [Workaround-Thread](https://community.volumio.org/t/cannot-install-build-essential-package/46856/16?u=maschine2501).
I've implemented his workaround in the [Install-Script](https://github.com/Maschine2501/NR1-UI/blob/master/install-buildfix.sh) between line 12 until line 24.
Now the Installation is working fine aggain with latest stable volumio :-)

## 04.09.2021 Attention:
Hi Guys, I have some bad news...
At least with Volumio 2.907 the installation-script for NR1-UI is broken (I guess 2.882/2.873 should work fine...).
Reason: Something in the Volumio-Core has changed, "build-essential" is not installable anymore. 
Without "Build-essential" OpenSSL, Python 3.8.5, and CAVA could not be compiled and installed.
And without this Tools NR1-UI wont run...
-.-
I tried many things to fix it, but did not found any solution yet.
@everyone Maybe anyone of you has an idea for a fix?
But i have slightly good news: As soon as Volumio Buster (actually in Beta-Testing) is released, the installation process will be much lighter (no openssl/python3.85 needed). 
I tested it allready and it is running fine.

-> If you want, here is the Installation Instruction for the Buster-Beta:
[Buster-Beta Installation Instructions](https://github.com/Maschine2501/NR1-UI/wiki/Volumio-Buster-(Beta)-Installation)

## 07.03.2021 New:
- [x] Tune the whole UI (fonts, positions... etc.)
- [x] added Unicode Font (Support for TC/JP..)
- [x] Support for ssd1351(color Oled)
- [x] Support for st7735 (color LCD)
- [x] Enhanced stability when using cava
- [x] prevented screenfreeze when using Roon

# NR1-UI
Im building a Network Hifi Receiver from scratch. Main components are a RaspberryPi4 and an HiFi-Berry-Dac. An old Braun T2 Tuner serves as case for the player.
To keep as much as possible from the look of the device I needed an Interface for Volumio. And especialy one that supports a 3,2" ssd1322 SPI Oled with 256x64Pixel.
After doing some research I found diehrdsk/Volumio-OledUI. It fullfills many points on my "wishlist" but not nearly all.
As we all know, the way is the destination, i spent some time (much time....) in modifying the original code.
The project is not finished yet... but close the the goal!

I try to assist you, if you got questions or even problems with the code, just contact me. 

Time by time more informations in the [wiki](https://github.com/Maschine2501/NR1-UI/wiki) will follow...

## The Code is modular and has a Setup-Process.

#### [Features](https://github.com/Maschine2501/NR1-UI/wiki/Features)


#### [Allready Done](https://github.com/Maschine2501/NR1-UI/wiki/Allready-Done)


#### [Project on Volumio-Forum](https://community.volumio.org/t/oled-user-inteface-for-volumio-with-rotary-and-4-buttons-modular-highly-configurable-supports-ssd1306-and-ssd1322/40378?u=maschine2501)

---

## [1. Basic Installation Steps](https://github.com/Maschine2501/NR1-UI/wiki/Basic-Installation-Steps)

---

## [2. Main-Installation Steps](https://github.com/Maschine2501/NR1-UI/wiki/Main-Installation-Steps)
---

#### Configuration Manual (will follow soon!)
---

#### [wiring / button-layout / truthtable](https://github.com/Maschine2501/NR1-UI/wiki/wiring-and-button-truth-table)
---

#### [hardware](https://github.com/Maschine2501/NR1-UI/wiki/hardware)
---

#### [dependencies](https://github.com/Maschine2501/NR1-UI/wiki/dependencies)
---

#### [font-info and source](https://github.com/Maschine2501/NR1-UI/wiki/font-information-(source))
---

## Your Display is not supported yet? You have an idea for a function/feature?
### -> Contact me:
#### [E-Mail](mailto:Maschine2501@gmx.de?subject=[GitHub]%20Source%20Han%20Sans)
#### [Discord Server for direct contact: Click here to join...](https://discord.gg/GJ4ED3F)


### To change the look/layout just press Button-C in "Standby-Screen" (Clock), select the desired Layout with the Rotary-Rotation and push the Rotary once to apply selection -> 
![Screenselect](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/ssd1322Screenselect.png)

### Screenshots and Layout Overview:
![Screenshots](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/screenshots/Screenshots.png)

### [buy me a coffee, or tip me ;-)](https://paypal.me/maschine2501)

![MS2501](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/MS2501.png)


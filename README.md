Inspired by: [diehardsk/Volumio-OledUI](https://github.com/diehardsk/Volumio-OledUI) // 
This is the Python3 version of [Maschine2501/Volumio-OledUI](https://github.com/Maschine2501/Volumio-OledUI/)

# 18.10.2022: The Journey came to an End.
### I wont push this project any further, cause I do not longer use Volumio. Feel free to fork this Project. I'll leave the Discord Chanel open for you, so you can reach out for each others support.

## It was a great time, Thank you! <3

# 27.03.2022 Volumio 3.xx is now supported:
Today I fixed the installation routine for the new Volumio 3.xx.
I tested the Installation script twice on a fresh installed RPi4 -> Succeeded both times.
If you have an issue, please report it :)
Here is the instruction for the Installation: [Install-Manuall for Volumio 3.xx NR1-UI](https://github.com/Maschine2501/NR1-UI/wiki/Volumio-Buster-Installation)

## Supported Displays:
- [x] SSD1306 (monochrome Oled 128x64)
- [x] SSD1322 (grayscale Oled 256x64)
- [x] SSD1351  (full color Oled 128x128)
- [x] ST7735 (full color LCD 160x128)

## Wishlist/To-Do:
- [ ] ILI9341 (Maybe ILI9488) display support(Alpha-phase)

- [ ] SSD1309 (monochrome Oled 128x64)
- [ ] BGR / RGB Selection for ssd1351 displays
- [ ] Sort out / Clean up Setup
- [ ] Investigate Problem with some DAC's
- [ ] Implement Volume Control
- [ ] Implement Source Dialog
- [ ] Implement a "Settings Menu"



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

## [1. Installation steps](https://github.com/Maschine2501/NR1-UI/wiki/Volumio-Buster-Installation)
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

![MS2501](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/MadeByGloria.jpg)
[Logo made by glorious @Klassik_Otaku](http://www.instagram.com/klassik_otaku)


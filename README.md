Inspired by: https://github.com/diehardsk/Volumio-OledUI
This is a fork from diehrdsk/Volumio-OledUi

# Volumio-OledUI MK2

Demo Video from early Build:

[![Video-Sample](http://img.youtube.com/vi/1nwmKzCCoZE/0.jpg)](http://www.youtube.com/watch?v=1nwmKzCCoZE "Video-Sample")

## Why is the first part of the display empty?

I want to use the display in a case of an old hifi-tuner, the cutout in the front of the device is smaller as the display.

### But you want it on the whole Display?

Simply change the value's from "42" to "0" (self.text1Pos = (42, 2))... that's it! (Tutorials/Guides will follow...)

## To-Do: 
* Tune the whole UI (fonts, positions... etc. / will be done when everything else is running properly)
* change Play- Pause- and Stop- Icons
* Bootup and Shutdown Logos (needs to be improved)

* Maybe integrate "CAVA" to display a bargraph spectrum? (hot topic!!!)

## Allready Done:

* Standby-Screen (when Playback is stoped, Time, Date and IP is Displayed)
* Automatic stop when playback is paused (value could be defined / declared)
* display Fileformat/Samplerate/Bitdepth in the NowPlayingScreen
* Scroll Text stops before shown completly -> text was defined as scrollText, which makes "black"-boxes arround the text
* one rotary removed
* 4 more Buttons via GPIO (needs some fine tuning)
* MediaInformationScreen (volumio.local/api/v1/collectionstats)

## [installation steps (stable release)](https://github.com/Maschine2501/Volumio-OledUI/wiki/Installation-steps-(stable-release))


## [installation steps (nightly build)](https://github.com/Maschine2501/Volumio-OledUI/wiki/Installation-steps-(nightly))

## Check the logs

#### for the stable build

sudo journalctl -fu oledui.service

#### for the nightly build:

sudo journalctl -fu oledui-nightly.service

## [Hints](https://github.com/Maschine2501/Volumio-OledUI/wiki/hints---tricks---nice-to-know)

## [wiring / button-layout / truthtable](https://github.com/Maschine2501/Volumio-OledUI/wiki/Wiring---Button-Truthtable)

### [hardware](https://github.com/Maschine2501/Volumio-OledUI/wiki/Hardware)

### [dependencies](https://github.com/Maschine2501/Volumio-OledUI/wiki/Dependencies)

### [Sources & font-info](https://github.com/Maschine2501/Volumio-OledUI/wiki/Sources---font-information)


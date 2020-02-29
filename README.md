Inspired by: https://github.com/diehardsk/Volumio-OledUI
This is a fork from diehrdsk/Volumio-OledUi

# Volumio-OledUI MK2

Demo Video from early Build:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/xB8cvn7IXr8/0.jpg)](http://www.youtube.com/watch?v=xB8cvn7IXr8 "Video-Sample")

## To-Do: 
* Tune "Now-Playing" Screen (other fonts, position)
* Play- Pause- and Stop- Icons
* Bootup and Shutdown Logos
* More Buttons via GPIO
* MediaInformationScreen (volumio.local/api/v1/collectionstats)
* ? Use "CAVA" to display a bargraph spectrum ?

## Allready Done:
* Standby-Screen (when Playback is stoped, Time, Date and IP is Displayed)
* Automatic stop when playback is paused (value could be defined / declared)
* display Fileformat/Samplerate/Bitdepth in the NowPlayingScreen
* Scroll Text stops before shown completly -> text was defined as scrollText, which makes "black"-boxes arround the text
* one rotary removed

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


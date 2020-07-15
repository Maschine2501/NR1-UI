#!/usr/bin/python3
#      ____  ____  ___   __  ___   __     _   ______ ___
#     / __ )/ __ \/   | / / / / | / /    / | / / __ <  /
#    / __  / /_/ / /| |/ / / /  |/ /    /  |/ / /_/ / / 
#   / /_/ / _, _/ ___ / /_/ / /|  /    / /|  / _, _/ /  
#  /_____/_/ |_/_/  |_\____/_/ |_/    /_/ |_/_/ |_/_/   
#    __  __              ____     __          ___            
#   / / / /__ ___ ____  /  _/__  / /____ ____/ _/__ ________ 
#  / /_/ (_-</ -_) __/ _/ // _ \/ __/ -_) __/ _/ _ `/ __/ -_)
#  \____/___/\__/_/   /___/_//_/\__/\__/_/ /_/ \_,_/\__/\__/ 
#
#  For more Informations visit: https://github.com/Maschine2501/NR1-UI
#   _           __  __ ___ ___ ___  __  _ 
#  | |__ _  _  |  \/  / __|_  ) __|/  \/ |
#  | '_ \ || | | |\/| \__ \/ /|__ \ () | |
#  |_.__/\_, | |_|  |_|___/___|___/\__/|_|
#        |__/                                                                                                                                            
#_________________________________________________________________________
#_________________________________________________________________________
#    ____                           __           
#   /  _/___ ___  ____  ____  _____/ /______   _ 
#   / // __ `__ \/ __ \/ __ \/ ___/ __/ ___/  (_)
# _/ // / / / / / /_/ / /_/ / /  / /_(__  )  _   
#/___/_/ /_/ /_/ .___/\____/_/   \__/____/  (_)  
#             /_/                                
from __future__ import unicode_literals
import requests
import os
import sys
import time
import threading
import signal
import json
import pycurl
import pprint
import subprocess
import RPi.GPIO as GPIO
from time import*
from datetime import timedelta as timedelta
from threading import Thread
from socketIO_client import SocketIO
from datetime import datetime as datetime
from io import BytesIO 
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from modules.pushbutton import PushButton
from modules.rotaryencoder import RotaryEncoder
from modules.displayFull import*
#_________________________________________________________________________
#_________________________________________________________________________
#
#   ______            _____                        __  _                 
#  / ____/___  ____  / __(_)___ ___  ___________ _/ /_(_)___  ____     _ 
# / /   / __ \/ __ \/ /_/ / __ `/ / / / ___/ __ `/ __/ / __ \/ __ \   (_)
#/ /___/ /_/ / / / / __/ / /_/ / /_/ / /  / /_/ / /_/ / /_/ / / / /  _   
#\____/\____/_/ /_/_/ /_/\__, /\__,_/_/   \__,_/\__/_/\____/_/ /_/  (_)  
#                       /____/
#
#config for Button and Rotary-Encoder GPIO-Usage:   !!! Use BCM-Pin-Nr. not the physical Pin-Nr. !!!
oledBtnA = 4
oledBtnB = 17
oledBtnC = 5
oledBtnD = 6
oledRtrLeft = 22
oledRtrRight = 23
oledRtrBtn = 27

#config for Display:
oledrotation = 2           # 2 = 180° rotation, 0 = 0° rotation

#Config Features:
StandbyActive = False
ledActive = False
ledTechnology = None        #None or 'GPIOusage' or 'pcf8574usage'

#Config TextPositions NowPlaying-/StandBy-Screen:
oledtext01 = 0, 2        #Artist
oledtext02 = 0, 22       #Title
oledtext03 = 0, 2       #clock
oledtext04 = 39, 42      #IP
oledtext05 = 55, 29     #Date
oledtext06 = 0, 41       #format
oledtext07 = 24, 41     #samplerate
oledtext08 = 85, 41     #bitdepth
oledtext09 = 116, 54     #LibraryInfoIcon

#configuration NowPlayingScreen visibility:
oledBackgroundVisibility = 200
oledPlaystateIconVisibility = 200

#Config TextPositions Media-Library-Info-Screen:
oledtext10 = 80, 2      #Number of Artists
oledtext11 = 80, 15     #Number of Albums
oledtext12 = 80, 28     #Number of Songs
oledtext13 = 80, 41     #Summary of duration
oledtext14 = 14, 2       #Text for Artists
oledtext15 = 14, 15      #Text for Albums
oledtext16 = 14, 28      #Text for Songs
oledtext17 = 14, 41      #Text for duration
oledtext18 = 60, 52     #Menu-Label Icon
oledtext19 = 120, 54     #LibraryInfoIcon
oledtext20 = 0, 2        #icon for Artists
oledtext21 = 0, 15       #icon for Albums
oledtext22 = 0, 28       #icon for Songs
oledtext23 = 0, 41       #icon for duration

#configuration TextPositions Spectrum-Screen:
oledtext24 = 0, 2        #Artist Non-Stream-Screen
oledtext25 = 0, 22       #Title Non-Stream-Screen
oledtext26 = 0, 2        #Artist Stream-Screen
oledtext27 = 0, 22       #Title Stream-Screen

#configuration Menu-Screen:
oledListEntrys = 4
oledEmptyListText = 'no items..'
oledEmptyListTextPosition = 0, 4
oledListTextPosX = 0
oledListTextPosY = 16    #height of each Entry (4x16 = 64)

#configuration of the duration and playtime (textbox-) positions
oledActualPlaytimeText = 0, 54
oledDurationText = 78, 54

#config for Progress-Bar
oledbarwidth = 28
oledbarLineBorder = 'white'
oledbarLineFill = 'black'
oledbarLineX = 45
oledbarLineThick1 = 59     #difference between both = thickness 
oledbarLineThick2 = 59     # 59 and 59 = 1 Pixel thick
oledbarBorder = 'white'
oledbarFill = 'black'
oledbarX = 45
oledbarThick1 = 56         #difference between both = thickness 
oledbarThick2 = 62         # 56 and 62 = 6 Pixel thick

#config for Spectrum
oledspecBorder = 'white'
oledspecFill = 'white'
oledspecWide1 = 8
oledspecWide2 = 6
oledspecYposTag = 48
oledspecYposNoTag = 63

#config for Text:
oledArt = 'Interpreten :'  #sets the Artists-text for the MediaLibrarayInfo
oledAlb = 'Alben :'        #sets the Albums-text for the MediaLibrarayInfo
oledSon = 'Songs :'        #sets the Songs-text for the MediaLibrarayInfo
oledPla = 'Playtime :'     #sets the Playtime-text for the MediaLibrarayInfo

#config for Icons:
oledlibraryInfo = '\U0001F4D6'
oledlibraryReturn = '\u2302'
oledArtistIcon = '\uF0F3'
oledAlbumIcon = '\uF2BB'
oledSongIcon = '\U0000F001'
oledPlaytimeIcon = '\U0000F1DA'

#config for timers:
oledPause2StopTime = 15.0
oledPlay2SpectrumTime = 15.0
oledPlayFormatRefreshTime = 1.5
oledPlayFormatRefreshLoopCount = 3
#_________________________________________________________________________
#_________________________________________________________________________
#
#    __  ___      _             ______          __         
#   /  |/  /___ _(_)___        / ____/___  ____/ /__     _ 
#  / /|_/ / __ `/ / __ \______/ /   / __ \/ __  / _ \   (_)
# / /  / / /_/ / / / / /_____/ /___/ /_/ / /_/ /  __/  _   
#/_/  /_/\__,_/_/_/ /_/      \____/\____/\__,_/\___/  (_)  
#                                                          

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

firstStart = True

if firstStart == True:
    if ledTechnology == None:
        from modules.StatusLEDempty import*
    if ledTechnology == 'GPIOusage':
        from modules.StatusLEDgpio import*
    if ledTechnology == 'pcf8574usage':
        from modules.StatusLEDpcf import*

volumio_host = 'localhost'
volumio_port = 3000
volumioIO = SocketIO(volumio_host, volumio_port)

if StandbyActive == True:
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(26, GPIO.IN)
    GPIO.output(13, GPIO.HIGH)

b_obj = BytesIO() 
crl = pycurl.Curl() 

STATE_NONE = -1
STATE_PLAYER = 0
STATE_QUEUE_MENU = 1
STATE_LIBRARY_INFO = 2
STATE_SPECTRUM_DISPLAY = 3

UPDATE_INTERVAL = 0.034

interface = i2c(port=1, address=0x3C)
oled = ssd1306(interface) #, rotate=oledrotation) 

oled.WIDTH = 128
oled.HEIGHT = 64
oled.state = 'stop'
oled.stateTimeout = 0
oled.spectrumTimer = 0
oled.timeOutRunning = False
oled.activeSong = ''
oled.activeArtist = 'VOLuMIO'
oled.playState = 'unknown'
oled.playPosition = 0
oled.seek = 1000
oled.duration = 1.0
oled.modal = False
oled.playlistoptions = []
oled.queue = []
oled.libraryFull = []
oled.libraryNames = []
oled.volumeControlDisabled = True
oled.volume = 100
now = datetime.now()                       #current date and time
oled.time = now.strftime("%H:%M:%S")       #resolves time as HH:MM:SS eg. 14:33:15
oled.date = now.strftime("%d.  %m.  %Y")   #resolves time as dd.mm.YYYY eg. 17.04.2020
oled.IP = ''
emit_track = False
newStatus = 0              				   #makes newStatus usable outside of onPushState
oled.activeFormat = ''      			   #makes oled.activeFormat globaly usable
oled.activeSamplerate = ''  			   #makes oled.activeSamplerate globaly usable
oled.activeBitdepth = ''                   #makes oled.activeBitdepth globaly usable
oled.activeArtists = ''                    #makes oled.activeArtists globaly usable
oled.activeAlbums = ''                     #makes oled.activeAlbums globaly usable
oled.activeSongs = ''                      #makes oled.activeSongs globaly usable
oled.activePlaytime = ''                   #makes oled.activePlaytime globaly usable
oled.randomTag = False                     #helper to detect if "Random/shuffle" is set
oled.repeatTag = False                     #helper to detect if "repeat" is set
oled.ShutdownFlag = False                  #helper to detect if "shutdown" is running. Prevents artifacts from Standby-Screen during shutdown
SpectrumStamp = 0.0
oled.selQueue = ''

image = Image.new('1', (oled.WIDTH, oled.HEIGHT))  #for Pixelshift: (oled.WIDTH + 4, oled.HEIGHT + 4)) 
oled.clear()

font = load_font('Oxanium-Bold.ttf', 16)                       #used for Artist
font2 = load_font('Oxanium-Light.ttf', 12)                     #used for all menus
font3 = load_font('Oxanium-Regular.ttf', 14)                   #used for Song
font4 = load_font('Oxanium-Medium.ttf', 12)                    #used for Format/Smplerate/Bitdepth
mediaicon = load_font('fa-solid-900.ttf', 10)    	       #used for icon in Media-library info
iconfont = load_font('entypo.ttf', oled.HEIGHT)                #used for play/pause/stop/shuffle/repeat... icons
labelfont = load_font('entypo.ttf', 12)                       #used for Menu-icons
iconfontBottom = load_font('entypo.ttf', 10)                   #used for icons under the screen / button layout
fontClock = load_font('DSG.ttf', 24)                           #used for clock
fontDate = load_font('DSEG7Classic-Regular.ttf', 10)           #used for Date 
fontIP = load_font('DSEG7Classic-Regular.ttf', 10)             #used for IP  
#above are the "imports" for the fonts. 
#After the name of the font comes a number, this defines the Size (height) of the letters. 
#Just put .ttf file in the 'Volumio-OledUI/fonts' directory and make an import like above. 

def StandByWatcher():
# listens to GPIO 26. If Signal is High, everything is fine, raspberry will keep doing it's shit.
# If GPIO 26 is Low, Raspberry will shutdown.
    StandbySignal = GPIO.input(26)
    while True:
        StandbySignal = GPIO.input(26)
        if StandbySignal == 0:
            oled.ShutdownFlag = True
            volumioIO.emit('stop')
            GPIO.output(13, GPIO.LOW)
            sleep(1)
            oled.clear()
            show_logo("shutdown.ppm", oled)
            volumioIO.emit('shutdown')
        elif StandbySignal == 1:
            sleep(1)

#I inverted the logic above, so GPIO26 does not need an external signal.

def sigterm_handler(signal, frame):
    oled.ShutdownFlag = True
    volumioIO.emit('stop')
    GPIO.output(13, GPIO.LOW)
    oled.clear()
    show_logo("shutdown.ppm", oled)
    print('booyah! bye bye')

def GetIP():
    lanip = GetLANIP()
    print(lanip)
    LANip = str(lanip.decode('ascii'))
    print('LANip: ', LANip)
    wanip = GetWLANIP()
    print(wanip)
    WLANip = str(wanip.decode('ascii'))
    print('WLANip: ', WLANip)
    if LANip != '':
       ip = LANip
       print('LanIP: ', ip)
    elif WLANip != '':
       ip = WLANip
       print('WlanIP: ', ip)
    else:
       ip = "no ip"
    oled.IP = ip

def GetLANIP():
    cmd = \
        "ip addr show eth0 | grep inet  | grep -v inet6 | awk '{print $2}' | cut -d '/' -f 1"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output[:-1]

def GetWLANIP():
    cmd = \
        "ip addr show wlan0 | grep inet  | grep -v inet6 | awk '{print $2}' | cut -d '/' -f 1"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output[:-1]

if StandbyActive == True and firstStart == True:
    signal.signal(signal.SIGTERM, sigterm_handler)
    StandByListen = threading.Thread(target=StandByWatcher, daemon=True)
    StandByListen.start()
    if ledActive != True:
       firstStart = False

GetIP()

if ledActive == True and firstStart == True:
    SysStart()
    sleep (6.0)
    Processor = threading.Thread(target=CPUload, daemon=True)
    Processor.start()
    firstStart = False

def display_update_service():
    while UPDATE_INTERVAL > 0 and oled.ShutdownFlag == False:
        prevTime = time()
        dt = time() - prevTime
        if oled.stateTimeout > 0:
            oled.timeOutRunning = True
            oled.stateTimeout -= dt
        elif oled.stateTimeout <= 0 and oled.timeOutRunning:
            oled.timeOutRunning = False
            oled.stateTimeout = 0
            SetState(STATE_PLAYER)
        image.paste("black", [0, 0, image.size[0], image.size[1]])
        try:
            oled.modal.DrawOn(image)
        except AttributeError:
            print("render error")
            sleep(1)
        cimg = image.crop((0, 0, oled.WIDTH, oled.HEIGHT)) 
        oled.display(cimg)
        sleep(UPDATE_INTERVAL)

#Example to SetState:
#oled.modal = NowPlayingScreen(oled.HEIGHT, oled.WIDTH, oled.activeArtist, oled.activeSong, oled.time, oled.IP, font, hugefontaw, fontClock)
#here you have to define which variables you want to use in "class" (following below)
#simply define which "data" (eg. oled.IP...) you want to display followed by the fonts you want to use
#Hint: the "data" is equal to row1, row2... etc. in the classes, first "data" is row1 and so on...
#oled.activeArtist = row1 / oled.activeSong = row2 ....
	
def SetState(status):
    oled.state = status
    if oled.state == STATE_PLAYER:
        oled.modal = NowPlayingScreen(oled.HEIGHT, oled.WIDTH) 
        oled.modal.SetPlayingIcon(0) 
    elif oled.state == STATE_QUEUE_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH)
    elif oled.state == STATE_LIBRARY_INFO:
        oled.modal = MediaLibrarayInfo(oled.HEIGHT, oled.WIDTH)
    elif oled.state == STATE_SPECTRUM_DISPLAY:
        oled.modal = SpectrumScreen(oled.HEIGHT, oled.WIDTH) 

#In 'onPushState' the whole set of media-information is linked to the variables (eg. artist, song...)
#On every change in the Playback (pause, other track, etc.) Volumio pushes a set of informations on port 3000.
#Volumio-OledUI is always listening on this port. If there's new 'data', the "def onPushState(data):" runs again.

def onPushState(data):
    global OPDsave	
    global newStatus #global definition for newStatus, used at the end-loop to update standby
    global newSong
    global newArtist
    OPDsave = data

    if 'title' in data:
        newSong = data['title']
    else:
        newSong = ''
    if newSong is None:
        newSong = ''
        
    if 'artist' in data:
        newArtist = data['artist']
    else:
        newArtist = ''
    if newArtist is None:   #volumio can push NoneType
        newArtist = ''
	
    if 'stream' in data:
        newFormat = data['stream']
    else:
        newFormat = ''
    if newFormat is None:
        newFormat = ''
    if newFormat == True:
       newFormat = 'WebRadio'

	#If a stream (like webradio) is playing, the data set for 'stream'/newFormat is a boolian (True)
	#drawOn can't handle that and gives an error. 
	#therefore we use "if newFormat == True:" and define a placeholder Word, you can change it.

    if 'samplerate' in data:
        newSamplerate = data['samplerate']
    else:
        newSamplerate = ' '
    if newSamplerate is None:
        newSamplerate = ' '

    if 'bitdepth' in data:
        newBitdepth = data['bitdepth']
    else:
        newBitdepth = ' '
    if newBitdepth is None:
        newBitdepth = ' '  
        
    if 'position' in data:                      # current position in queue
        oled.playPosition = data['position']    # didn't work well with volumio ver. < 2.5
        
    if 'status' in data:
        newStatus = data['status']
        specstatus1 = newStatus
        spectstatus2 = oled.playState
    
    if ledActive == True and 'channels' in data:
        channels = data['channels']
        if channels == 2:
           StereoLEDon()
        else:
           StereoLEDoff()

    if 'duration' in data:
        oled.duration = data['duration']
    else:
        oled.duration = None
    if oled.duration == int(0):
        oled.duration = None

    if 'seek' in data:
        oled.seek = data['seek']
    else:
        oled.seek = None

    if newArtist is None:   #volumio can push NoneType
        newArtist = ''
    
    oled.activeFormat = newFormat
    oled.activeSamplerate = newSamplerate
    oled.activeBitdepth = newBitdepth

    if (newSong != oled.activeSong) or (newArtist != oled.activeArtist):                                # new song and artist
        oled.activeSong = newSong
        oled.activeArtist = newArtist
        if oled.state == STATE_PLAYER and newStatus != 'stop':                                          #this is the "NowPlayingScreen"
            SpectrumStamp = 0.0
            SetState(STATE_PLAYER)
            if ledActive == True:
               PlayLEDon()
            oled.modal.UpdatePlayingInfo()     #here is defined which "data" should be displayed in the class
        if oled.state == STATE_PLAYER and newStatus == 'stop':                                          #this is the "Standby-Screen"
            if ledActive == True:
               PlayLEDoff()
            SpectrumStamp = 0.0
            SetState(STATE_PLAYER)
            oled.modal.UpdateStandbyInfo()                                 #here is defined which "data" should be displayed in the class
        if oled.state == 3 and newStatus != 'stop':                                          #this is the "NowPlayingScreen"
            SpectrumStamp = 0.0
            oled.state = 0
            SetState(STATE_PLAYER)
            if ledActive == True:
               PlayLEDon()
            oled.modal.UpdatePlayingInfo()     #here is defined which "data" should be displayed in the class
        if oled.state == 3 and newStatus == 'stop':                                          #this is the "Standby-Screen"
            if ledActive == True:
               PlayLEDoff()
            SpectrumStamp = 0.0
            oled.state = 0
            SetState(STATE_PLAYER)
            oled.modal.UpdateStandbyInfo()                                 #here is defined which "data" should be displayed in the class

    if newStatus != oled.playState:
        oled.playState = newStatus
        if oled.state == STATE_PLAYER:
            if oled.playState == 'play':
                iconTime = 35
            else:
                iconTime = 80
            SetState(STATE_PLAYER)    
            oled.modal.SetPlayingIcon(iconTime)

def onPushCollectionStats(data):
    data = json.loads(data.decode("utf-8"))             #data import from REST-API (is set when ButtonD short-pressed in Standby)

    if "artists" in data:               #used for Media-Library-Infoscreen
        newArtists = data["artists"]
    else:
        newArtists = ''
    if newArtists is None:
        newArtists = ''

    if 'albums' in data:                #used for Media-Library-Infoscreen
        newAlbums = data["albums"]
    else:
        newAlbums = ''
    if newAlbums is None:
        newAlbums = ''

    if 'songs' in data:                 #used for Media-Library-Infoscreen
        newSongs = data["songs"]
    else:
        newSongs = ''
    if newSongs is None:
        newSongs = ''

    if 'playtime' in data:               #used for Media-Library-Infoscreen
        newPlaytime = data["playtime"]
    else:
        newPlaytime = ''
    if newPlaytime is None:
        newPlaytime = ''

    oled.activeArtists = str(newArtists) 
    oled.activeAlbums = str(newAlbums)
    oled.activeSongs = str(newSongs)
    oled.activePlaytime = str(newPlaytime)
	
    if oled.state == STATE_LIBRARY_INFO and oled.playState == 'info':                                   #this is the "Media-Library-Info-Screen"
       oled.modal.UpdateLibraryInfo() 

def onPushQueue(data):
    oled.queue = [track['name'] if 'name' in track else 'no track' for track in data]

#if you wan't to add more textposition: double check if using STATIC or SCROLL text.
#this needs to be declared two times, first in "self.playingText" AND under: "def UpdatePlayingInfo" or "def UpdateStandbyInfo"

class NowPlayingScreen():
    def __init__(self, height, width): #this line references to oled.modal = NowPlayingScreen
        self.height = height
        self.width = width
        self.playingText1 = ScrollText(self.height, self.width, oled.activeArtist, font)          #Artist /center=True
        self.playingText2 = ScrollText(self.height, self.width, oled.activeSong, font3)        	  #Title
        self.playingText3 = StaticText(self.height, self.width, oled.activeFormat, font4)         #format / flac,MP3...
        self.playingText4 = StaticText(self.height, self.width, oled.activeSamplerate, font4)     #samplerate / 44100
        self.playingText5 = StaticText(self.height, self.width, oled.activeBitdepth, font4)       #bitdepth /16 Bit
        self.standbyText1 = StaticText(self.height, self.width, oled.time, fontClock)    	      #Clock /center=True
        self.standbyText2 = StaticText(self.height, self.width, oled.IP, fontIP)	    	      #IP
        self.standbyText3 = StaticText(self.height, self.width, oled.date, fontDate)     	      #Date
        self.standbyText7 = StaticText(self.height, self.width, oledlibraryInfo, iconfontBottom)  #LibraryInfoIcon
        self.icon = {'play':'\u25B6', 'pause':'\u2389', 'stop':'\u25A0'}       	    	          #entypo icons
        self.playingIcon = self.icon['play']
        self.iconcountdown = 0
        self.text1Pos = oledtext01      #Artist
        self.text2Pos = oledtext02      #Title
        self.text3Pos = oledtext03      #clock
        self.text4Pos = oledtext04      #IP
        self.text5Pos = oledtext05      #Date
        self.text6Pos = oledtext06      #format
        self.text7Pos = oledtext07      #samplerate
        self.text8Pos = oledtext08      #bitdepth
        self.text17Pos = oledtext09     #LibraryInfoIcon
        self.alfaimage = Image.new('1', image.size, ('black'))

# "def __init__(self,...." is the "initialization" of the "NowPlayingScreen". 
#Here you need to define the variables, which "data-string" is which textposition, where each textposition is displayed in the display...

    def UpdatePlayingInfo(self):
        self.playingText1 = ScrollText(self.height, self.width, oled.activeArtist, font)   		  #Artist/ center=True)
        self.playingText2 = ScrollText(self.height, self.width, oled.activeSong, font3)  		  #Title
        self.playingText3 = StaticText(self.height, self.width, oled.activeFormat, font4)  		  #format
        self.playingText4 = StaticText(self.height, self.width, oled.activeSamplerate, font4)  	  #samplerate
        self.playingText5 = StaticText(self.height, self.width, oled.activeBitdepth, font4)  	  #bitdepth

    def UpdateStandbyInfo(self):
        self.standbyText1 = StaticText(self.height, self.width, oled.time, fontClock) 	          #Clock center=True)
        self.standbyText2 = StaticText(self.height, self.width, oled.IP, fontIP)    	          #IP
        self.standbyText3 = StaticText(self.height, self.width, oled.date, fontDate)              #Date
        self.standbyText7 = StaticText(self.height, self.width, oledlibraryInfo, iconfontBottom)  #LibraryInfoIcon

#"def UpdateStandbyInfo" and "def UpdatePlayingInfo" collects the informations.
	
# "def DrawON(..." takes informations from above and creates a "picture" which then is transfered to your display	

    def DrawOn(self, image):
        if self.playingIcon != self.icon['stop'] and oled.duration != None:
            self.playingText1.DrawOn(image, self.text1Pos)    #Artist
            self.playingText2.DrawOn(image, self.text2Pos)    #Title
            self.playingText3.DrawOn(image, self.text6Pos)    #Format
            self.playingText4.DrawOn(image, self.text7Pos)    #Samplerate
            self.playingText5.DrawOn(image, self.text8Pos)    #Bitdep
            self.alfaimage.paste(('black'), [0, 0, image.size[0], image.size[1]])     
            drawalfa = ImageDraw.Draw(self.alfaimage)
            self.playbackPoint = oled.seek / oled.duration / 10
            self.bar = oledbarwidth * self.playbackPoint / 100
            drawalfa.text((oledActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font4, fill='white')
            drawalfa.text((oledDurationText), str(timedelta(seconds=oled.duration)), font=font4, fill='white')
            drawalfa.rectangle((oledbarLineX , oledbarLineThick1, oledbarLineX+oledbarwidth, oledbarLineThick2), outline=oledbarLineBorder, fill=oledbarLineFill)
            drawalfa.rectangle((oledbarX, oledbarThick1, oledbarX+self.bar, oledbarThick2), outline=oledbarBorder, fill=oledbarFill)
            compositeimage = Image.composite(self.alfaimage, image.convert('1'), self.alfaimage)
            image.paste(compositeimage.convert('1'), (0, 0))

        if self.playingIcon != self.icon['stop'] and oled.duration == None:
            self.playingText1.DrawOn(image, self.text1Pos)    #Artist
            self.playingText2.DrawOn(image, self.text2Pos)    #Title
            self.playingText3.DrawOn(image, self.text6Pos)    #Format
            self.playingText4.DrawOn(image, self.text7Pos)    #Samplerate
            self.playingText5.DrawOn(image, self.text8Pos)    #Bitdep
           	
        if self.playingIcon == self.icon['stop']:
            self.standbyText1.DrawOn(image, self.text3Pos)    #Clock
            self.standbyText2.DrawOn(image, self.text4Pos)    #IP
            self.standbyText3.DrawOn(image, self.text5Pos)    #Date
            self.standbyText7.DrawOn(image, self.text17Pos)   #libraryInfo

        if self.iconcountdown > 0:
            compositeimage = Image.composite(self.alfaimage, image.convert('1'), self.alfaimage)
            image.paste(compositeimage.convert('1'), (0, 0))
            self.iconcountdown -= 1
            
    def SetPlayingIcon(self, time=0):
        if oled.playState in self.icon:
           self.playingIcon = self.icon[oled.playState]
        self.alfaimage.paste(('black'), [0, 0, image.size[0], image.size[1]])         
        drawalfa = ImageDraw.Draw(self.alfaimage)
        iconwidth, iconheight = drawalfa.textsize(self.playingIcon, font=iconfont)   
        left = (self.width - iconwidth + 34) / 2						            #here is defined where the play/pause/stop icons are displayed. 
        drawalfa.text((left, 4), self.playingIcon, font=iconfont, fill=('white'))  
        self.iconcountdown = time

class MediaLibrarayInfo():
    def __init__(self, height, width): 
        self.height = height
        self.width = width
        self.LibraryInfoText1 = StaticText(self.height, self.width, oledArt, font4)   	                #Text for Artists
        self.LibraryInfoText2 = StaticText(self.height, self.width, oled.activeArtists, font4)          #Number of Artists
        self.LibraryInfoText3 = StaticText(self.height, self.width, oledAlb, font4)  	                #Text for Albums
        self.LibraryInfoText4 = StaticText(self.height, self.width, oled.activeAlbums, font4)           #Number of Albums
        self.LibraryInfoText5 = StaticText(self.height, self.width, oledSon, font4)   	                #Text for Songs
        self.LibraryInfoText6 = StaticText(self.height, self.width, oled.activeSongs, font4)        	#Number of Songs
        self.LibraryInfoText7 = StaticText(self.height, self.width, oledPla, font4)   	                #Text for duration
        self.LibraryInfoText8 = StaticText(self.height, self.width, oled.activePlaytime, font4)   	    #Summary of duration
        self.LibraryInfoText9 = StaticText(self.height, self.width, oledlibraryInfo, )  	    #Menu-label Icon
        self.LibraryInfoText10 = StaticText(self.height, self.width, oledlibraryReturn, iconfontBottom) #LibraryInfo Return
        self.LibraryInfoText11 = StaticText(self.height, self.width, oledArtistIcon, mediaicon)         #icon for Artists
        self.LibraryInfoText12 = StaticText(self.height, self.width, oledAlbumIcon, mediaicon)          #icon for Albums
        self.LibraryInfoText13 = StaticText(self.height, self.width, oledSongIcon, mediaicon)           #icon for Songs
        self.LibraryInfoText14 = StaticText(self.height, self.width, oledPlaytimeIcon, mediaicon)       #icon for duration
        self.icon = {'info':'\F0CA'}
        self.mediaIcon = self.icon['info']
        self.iconcountdown = 0
        self.text1Pos = oledtext10      					   #Number of Artists
        self.text2Pos = oledtext11      					   #Number of Albums4
        self.text3Pos = oledtext12      					   #Number of Songs
        self.text4Pos = oledtext13      					   #Summary of duration
        self.text5Pos = oledtext14     						   #Text for Artists
        self.text6Pos = oledtext15     						   #Text for Albums
        self.text7Pos = oledtext16     						   #Text for Songs
        self.text8Pos = oledtext17    						   #Text for duration
        self.text9Pos = oledtext18     						   #Menu-Label Icon
        self.text10Pos = oledtext19    						   #LibraryInfoIcon
        self.text11Pos = oledtext20     					   #icon for Artists
        self.text12Pos = oledtext21     					   #icon for Albums
        self.text13Pos = oledtext22    						   #icon for Songs
        self.text14Pos = oledtext23    						   #icon for duration
        self.alfaimage = Image.new('1', image.size, ('black'))

    def UpdateLibraryInfo(self):
        self.LibraryInfoText1 = StaticText(self.height, self.width, oledArt, font4)   	                #Text for Artists
        self.LibraryInfoText2 = StaticText(self.height, self.width, oled.activeArtists, font4)          #Number of Artists
        self.LibraryInfoText3 = StaticText(self.height, self.width, oledAlb, font4)  	                #Text for Albums
        self.LibraryInfoText4 = StaticText(self.height, self.width, oled.activeAlbums, font4)           #Number of Albums
        self.LibraryInfoText5 = StaticText(self.height, self.width, oledSon, font4)   	                #Text for Songs
        self.LibraryInfoText6 = StaticText(self.height, self.width, oled.activeSongs, font4)        	#Number of Songs
        self.LibraryInfoText7 = StaticText(self.height, self.width, oledPla, font4)   	                #Text for duration
        self.LibraryInfoText8 = StaticText(self.height, self.width, oled.activePlaytime, font4)   	    #Summary of duration
        self.LibraryInfoText9 = StaticText(self.height, self.width, oledlibraryInfo, )  	    #Menu-label Icon
        self.LibraryInfoText10 = StaticText(self.height, self.width, oledlibraryReturn, iconfontBottom) #LibraryInfo Return
        self.LibraryInfoText11 = StaticText(self.height, self.width, oledArtistIcon, mediaicon)         #icon for Artists
        self.LibraryInfoText12 = StaticText(self.height, self.width, oledAlbumIcon, mediaicon)          #icon for Albums
        self.LibraryInfoText13 = StaticText(self.height, self.width, oledSongIcon, mediaicon)           #icon for Songs
        self.LibraryInfoText14 = StaticText(self.height, self.width, oledPlaytimeIcon, mediaicon)       #icon for duration


    def DrawOn(self, image):
        if self.mediaIcon == self.icon['info']:
            self.LibraryInfoText1.DrawOn(image, self.text5Pos)     #Text for Artists
            self.LibraryInfoText2.DrawOn(image, self.text1Pos)     #Number of Artists
            self.LibraryInfoText3.DrawOn(image, self.text6Pos)     #Text for Albums
            self.LibraryInfoText4.DrawOn(image, self.text2Pos)     #Number of Albums
            self.LibraryInfoText5.DrawOn(image, self.text7Pos)     #Text for Songs
            self.LibraryInfoText6.DrawOn(image, self.text3Pos)     #Number of Songs
            self.LibraryInfoText7.DrawOn(image, self.text8Pos)     #Text for duration
            self.LibraryInfoText8.DrawOn(image, self.text4Pos) 	   #Number of durati
            self.LibraryInfoText9.DrawOn(image, self.text9Pos)     #menulabelIcon
            self.LibraryInfoText10.DrawOn(image, self.text10Pos)   #LibraryInfo Return
            self.LibraryInfoText11.DrawOn(image, self.text11Pos)   #icon for Artists
            self.LibraryInfoText12.DrawOn(image, self.text12Pos)   #icon for Albums
            self.LibraryInfoText13.DrawOn(image, self.text13Pos)   #icon for Songs
            self.LibraryInfoText14.DrawOn(image, self.text14Pos)   #icon for duration
                   
class SpectrumScreen():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.font4 = font4
        
    def UpdateSpectrumInfo(self):
        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

    def DrawOn(self, image):
        if oled.duration != None:
          self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
          self.playbackPoint = oled.seek / oled.duration / 10
          self.bar = oledbarwidth * self.playbackPoint / 100
          self.draw.text((oledtext24), oled.activeArtist, font=font, fill='white')
          self.draw.text((oledtext25), oled.activeSong, font=font3, fill='white')
          self.draw.text((oledActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font4, fill='white')
          self.draw.text((oledDurationText), str(timedelta(seconds=oled.duration)), font=font4, fill='white')
          self.draw.rectangle((oledbarLineX , oledbarLineThick1, oledbarLineX+oledbarwidth, oledbarLineThick2), outline=oledbarLineBorder, fill=oledbarLineFill)
          self.draw.rectangle((oledbarLineX, oledbarThick1, oledbarX+self.bar, oledbarThick2), outline=oledbarBorder, fill=oledbarFill)
          try: 
              subprocess.check_output('pgrep -x cava', shell = True)
          except:
              subprocess.call("cava &", shell = True)
          cava_fifo = open("/tmp/cava_fifo", 'r')
          data = cava_fifo.readline().strip().split(';')
          for i in range(0, len(data)-1):
              try:
                  self.draw.rectangle((i*oledspecWide1, oledspecYposTag, i*oledspecWide1+oledspecWide2, oledspecYposTag-int(data[i])), outline = oledspecBorder, fill =oledspecFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                  image.paste(self.image, (0, 0))
                  if specstatus1 != specstatus2:
                       oled.activeSong = newSong
                       oled.activeArtist = newArtist
                       if oled.state == STATE_PLAYER and newStatus != 'stop':                                          #this is the "NowPlayingScreen"
                          SetState(STATE_PLAYER)
                          oled.modal.UpdatePlayingInfo(newArtist, newSong, newFormat, newSamplerate, newBitdepth, oled.playIcon, oled.pauseIcon, oled.stopIcon, oled.prevIcon, oled.nextIcon)
                       if oled.state == STATE_PLAYER and newStatus == 'stop' or oled.playState == 'stop':                                          #this is the "Standby-Screen"
                          SetState(STATE_PLAYER)
                          oled.modal.UpdateStandbyInfo(oled.time, oled.IP, oled.date, oled.libraryIcon, oled.playlistIcon, oled.queueIcon, oled.libraryInfo)                        
              except:
                  pass   

        if oled.duration == None:
          self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
          self.draw.text((oledtext26), oled.activeArtist, font=font, fill='white')
          self.draw.text((oledtext27), oled.activeSong, font=font3, fill='white')
          try: 
              subprocess.check_output('pgrep -x cava', shell = True)
          except:
              subprocess.call("cava &", shell = True)
          cava_fifo = open("/tmp/cava_fifo", 'r')
          data = cava_fifo.readline().strip().split(';')
          for i in range(0, len(data)-1):
              try:
                  self.draw.rectangle((i*oledspecWide1, oledspecYposNoTag, i*oledspecWide1+oledspecWide2, oledspecYposNoTag-int(data[i])), outline = oledspecBorder, fill =oledspecFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                  image.paste(self.image, (0, 0))
                  if specstatus1 != specstatus2:
                       oled.activeSong = newSong
                       oled.activeArtist = newArtist
                       if oled.state == STATE_PLAYER and newStatus != 'stop':                                          #this is the "NowPlayingScreen"
                          SetState(STATE_PLAYER)
                          oled.modal.UpdatePlayingInfo()
                       if oled.state == STATE_PLAYER and newStatus == 'stop' or oled.playState == 'stop':                                          #this is the "Standby-Screen"
                          SetState(STATE_PLAYER)
                          oled.modal.UpdateStandbyInfo()                         
              except:
                  pass      

class MenuScreen():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.selectedOption = oled.playPosition
        self.menurows = oledListEntrys
        self.menuText = [None for i in range(self.menurows)]
        self.menuList = oled.queue
        self.totaloptions = len(oled.queue)
        self.onscreenoptions = min(self.menurows, self.totaloptions)
        self.firstrowindex = 0
        self.MenuUpdate()

    def MenuUpdate(self):
        self.firstrowindex = min(self.firstrowindex, self.selectedOption)
        self.firstrowindex = max(self.firstrowindex, self.selectedOption - (self.menurows-1))
        for row in range(self.onscreenoptions):
            if (self.firstrowindex + row) == self.selectedOption:
                color = "black"
                bgcolor = "white"
            else:
                color = "white"
                bgcolor = "black"
            optionText = self.menuList[row+self.firstrowindex]
            self.menuText[row] = StaticText(self.height, self.width, optionText, font2, fill=color, bgcolor=bgcolor)
        if self.totaloptions == 0:
            self.menuText[0] = StaticText(self.height, self.width, oledEmptyListText, font2, fill="white", bgcolor="black")
            
    def NextOption(self):
        self.selectedOption = min(self.selectedOption + 1, self.totaloptions - 1)
        self.MenuUpdate()

    def PrevOption(self):
        self.selectedOption = max(self.selectedOption - 1, 0)
        self.MenuUpdate()

    def SelectedOption(self):
        return self.selectedOption 

    def DrawOn(self, image):
        for row in range(self.onscreenoptions):
            self.menuText[row].DrawOn(image, (oledListTextPosX, row*oledListTextPosY))       #Here is the position of the list entrys from left set (42)
        if self.totaloptions == 0:
            self.menuText[0].DrawOn(image, (oledEmptyListTextPosition))                  #Here is the position of the list entrys from left set (42)
        
def ButtonA_PushEvent(hold_time):
    if hold_time < 2 and oled.state != STATE_LIBRARY_INFO:
#shortpress functions below
        print('ButtonA short press event')
        if oled.state == STATE_PLAYER or oled.state == STATE_SPECTRUM_DISPLAY and oled.playstate != 'stop':
            if oled.playstate == 'play':
                volumioIO.emit('pause')
            else:
                volumioIO.emit('play')

def ButtonB_PushEvent(hold_time):
    if hold_time < 2 and oled.state != STATE_LIBRARY_INFO:
#shortpress functions below
        print('ButtonB short press event')
        if oled.state == STATE_PLAYER or oled.state == STATE_SPECTRUM_DISPLAY and oled.playState != 'stop':
            volumioIO.emit('stop')

def ButtonC_PushEvent(hold_time):
    if hold_time < 2 and oled.state != STATE_LIBRARY_INFO:
#shortpress functions below
        print('ButtonC short press event')
        if oled.state == STATE_PLAYER or oled.state == STATE_SPECTRUM_DISPLAY and oled.playState != 'stop':
            volumioIO.emit('prev')
#Longpress functions below
    elif oled.state == STATE_PLAYER or oled.state == STATE_SPECTRUM_DISPLAY and oled.playState != 'stop':
        print('ButtonC long press event')
        if repeatTag == False:
            volumioIO.emit('setRepeat', {"value":"true"})
            repeatTag = True            
        elif repeatTag == True:
            volumioIO.emit('setRepeat', {"value":"false"})
            repeatTag = False
       
def ButtonD_PushEvent(hold_time):
    if hold_time < 2:
#shortpress functions below
        print('ButtonD short press event')
        if oled.state == STATE_PLAYER or oled.state == STATE_SPECTRUM_DISPLAY and oled.playState != 'stop':
            volumioIO.emit('next')
        if oled.state == STATE_PLAYER and oled.playState == 'stop':
            b_obj = BytesIO()
            crl = pycurl.Curl()
            crl.setopt(crl.URL, 'localhost:3000/api/v1/collectionstats')
            crl.setopt(crl.WRITEDATA, b_obj)
            crl.perform()
            crl.close()
            get_body = b_obj.getvalue()
            print('getBody',get_body)
            SetState(STATE_LIBRARY_INFO)
            oled.playState = 'info'
            onPushCollectionStats(get_body)
            sleep(0.5) 
        elif oled.state == STATE_LIBRARY_INFO:
            SetState(STATE_PLAYER)
#Longpress functions below
    elif oled.state == STATE_PLAYER or oled.state == STATE_SPECTRUM_DISPLAY and oled.playState != 'stop':
        print('ButtonD long press event')
        if randomTag == False:
            volumioIO.emit('setRandom', {"value":"true"})
            randomTag = True
        elif randomTag == True:
            volumioIO.emit('setRandom', {"value":"false"})
            randomTag = False

def RightKnob_RotaryEvent(dir):
    global emit_track
    oled.stateTimeout = 6.0
    if oled.state != STATE_QUEUE_MENU:
        SetState(STATE_QUEUE_MENU)
    if oled.state == STATE_QUEUE_MENU and dir == RotaryEncoder.LEFT:
        oled.modal.PrevOption()
        oled.selQueue = oled.modal.SelectedOption()
        emit_track = True
        SpectrumStamp = 0.0 
    elif oled.state == STATE_QUEUE_MENU and dir == RotaryEncoder.RIGHT:
        oled.modal.NextOption()
        oled.selQueue = oled.modal.SelectedOption()
        emit_track = True
        SpectrumStamp = 0.0 


def RightKnob_PushEvent(hold_time):
    if hold_time < 2 and oled.state == STATE_QUEUE_MENU:
#shortpress fuctions below
        print ('RightKnob_PushEvent SHORT')
        oled.stateTimeout = 0     

ButtonA_Push = PushButton(oledBtnA, max_time=2)
ButtonA_Push.setCallback(ButtonA_PushEvent)
ButtonB_Push = PushButton(oledBtnB, max_time=2)
ButtonB_Push.setCallback(ButtonB_PushEvent)
ButtonC_Push = PushButton(oledBtnC, max_time=2)
ButtonC_Push.setCallback(ButtonC_PushEvent)
ButtonD_Push = PushButton(oledBtnD, max_time=2)
ButtonD_Push.setCallback(ButtonD_PushEvent)

RightKnob_Push = PushButton(oledRtrBtn, max_time=1)
RightKnob_Push.setCallback(RightKnob_PushEvent)
RightKnob_Rotation = RotaryEncoder(oledRtrLeft, oledRtrRight, pulses_per_cycle=4)
RightKnob_Rotation.setCallback(RightKnob_RotaryEvent)

#show_logo("volumio_logo.ppm", oled)
#sleep(2)
SetState(STATE_PLAYER)

updateThread = Thread(target=display_update_service)
updateThread.daemon = True
updateThread.start()

def _receive_thread():
    volumioIO.wait()

receive_thread = Thread(target=_receive_thread)
receive_thread.daemon = True
receive_thread.start()

volumioIO.on('pushState', onPushState)
volumioIO.on('pushQueue', onPushQueue)

# get list of Playlists and initial state
volumioIO.emit('listPlaylist')
volumioIO.emit('getState')
volumioIO.emit('getQueue')

sleep(0.1)

try:
    with open('oledconfig.json', 'r') as f:   #load last playing track number
        config = json.load(f)
except IOError:
    pass
else:
    oled.playPosition = config['track']
    
if oled.playState != 'play':
    volumioIO.emit('play', {'value':oled.playPosition})

varcanc = True                      #helper for pause -> stop timeout counter
InfoTag = 0                         #helper for missing Artist/Song when changing sources
GetIP()

def PlaypositionHelper():
    while True:
          volumioIO.emit('getState')
          sleep(1.0)

PlayPosHelp = threading.Thread(target=PlaypositionHelper, daemon=True)
PlayPosHelp.start()

while True:
    if emit_track and oled.stateTimeout < 4.5:
        emit_track = False
        try:
            SpectrumStamp = 0.0
            SetState(STATE_PLAYER)
            InfoTag = 0
        except IndexError:
            pass
        volumioIO.emit('stop')
        sleep(0.2)
        volumioIO.emit('play', {'value':oled.selQueue})
    sleep(0.1)
    
    if oled.state == STATE_PLAYER and InfoTag <= oledPlayFormatRefreshLoopCount and newStatus != 'stop':
        oled.modal.UpdatePlayingInfo()
        InfoTag += 1
        sleep(oledPlayFormatRefreshTime)
        SpectrumStamp = time()

    if oled.state == STATE_PLAYER and newStatus == 'play' and time() - SpectrumStamp >= oledPlay2SpectrumTime:
        oled.state = 6
        SetState(STATE_SPECTRUM_DISPLAY)
        oled.modal.UpdateSpectrumInfo() 

#this is the loop to push the actual time every 0.1sec to the "Standby-Screen"

    if oled.state == STATE_PLAYER and newStatus == 'stop' and oled.ShutdownFlag == False:
        InfoTag = 0  #resets the InfoTag helper from artist/song update loop
        oled.state = 0
        SetState(STATE_PLAYER)
        oled.time = strftime("%H:%M:%S")
        oled.modal.UpdateStandbyInfo()

#if playback is paused, here is defined when the Player goes back to "Standby"/Stop		
    if oled.state == 3 and newStatus == 'stop':
       SpectrumStamp = 0.0
       SetState(STATE_PLAYER)

    if oled.state == 3 and newStatus == 'pause':
       SpectrumStamp = 0.0
       SetState(STATE_PLAYER)

    if oled.state == STATE_PLAYER and newStatus == 'pause' and varcanc == True:

       secvar = int(round(time()))
       oled.state = 0
       SetState(STATE_PLAYER)
       varcanc = False
    elif oled.state == STATE_PLAYER and newStatus == 'pause' and int(round(time())) - secvar > oledPause2StopTime:
         varcanc = True
         volumioIO.emit('stop')
         secvar = 0.0

sleep(0.1)

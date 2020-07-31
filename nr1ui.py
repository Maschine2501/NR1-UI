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
#________________________________________________________________________________________
#________________________________________________________________________________________
#	
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
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from modules.pushbutton import PushButton
from modules.rotaryencoder import RotaryEncoder
import uuid

#from decimal import Decimal
#________________________________________________________________________________________
#________________________________________________________________________________________
#	
#   ______            _____                        __  _                 
#  / ____/___  ____  / __(_)___ ___  ___________ _/ /_(_)___  ____     _ 
# / /   / __ \/ __ \/ /_/ / __ `/ / / / ___/ __ `/ __/ / __ \/ __ \   (_)
#/ /___/ /_/ / / / / __/ / /_/ / /_/ / /  / /_/ / /_/ / /_/ / / / /  _   
#\____/\____/_/ /_/_/ /_/\__, /\__,_/_/   \__,_/\__/_/\____/_/ /_/  (_)  
#                       /____/
#
#Config Features:
StandbyActive = False          #False or True
ledActive = False              #False or True
ledTechnology = None           #None or 'GPIOusage' or 'pcf8574usage'

DisplayTechnology = 'spi1322'  #'spi1322' or 'i2c1306' or 'Braun' 

ReadScreenLayout = open('/home/volumio/NR1-UI/config/LayoutSet.txt', 'r')
NowPlayingLayout = ReadScreenLayout.read()
ReadScreenLayout.close()

if DisplayTechnology != 'ssd1306':
    ScreenList = ['Spectrum-Left', 'Spectrum-Center', 'Spectrum-Right', 'No-Spectrum', 'Modern', 'VU-Meter-1', 'VU-Meter-2']
if DisplayTechnology == 'ssd1306':
    ScreenList = ['Progress-Bar', 'Spectrum-Screen']

if DisplayTechnology != 'ssd1306':
    if NowPlayingLayout not in ScreenList:
        WriteScreen1 = open('/home/volumio/NR1-UI/config/LayoutSet.txt', 'w')
        WriteScreen1.write('No-Spectrum')
        WriteScreen1.close
        NowPlayingLayout = 'No-Spectrum'
if DisplayTechnology == 'ssd1306':
    if NowPlayingLayout not in ScreenList:
        WriteScreen1 = open('/home/volumio/NR1-UI/config/LayoutSet.txt', 'w')
        WriteScreen1.write('Progress-Bar')
        WriteScreen1.close
        NowPlayingLayout = 'Progress-Bar'        


#config for Button and Rotary-Encoder GPIO-Usage:   !!! Use BCM-Pin-Nr. not the physical Pin-Nr. !!!
oledBtnA = 4
oledBtnB = 17
oledBtnC = 5
oledBtnD = 6
oledRtrLeft = 22
oledRtrRight = 23
oledRtrBtn = 27

#config for Display:
oledrotation = 0           # 2 = 180° rotation, 0 = 0° rotation

#config for timers:
oledPause2StopTime = 15.0
oledPlayFormatRefreshTime = 1.5
oledPlayFormatRefreshLoopCount = 3
#________________________________________________________________________________________
#________________________________________________________________________________________
#   _____ __             __            __     _____       _ __  _                      
#  / ___// /_____ ______/ /_      ____/ /__  / __(_)___  (_) /_(_)___  ____  _____   _ 
#  \__ \/ __/ __ `/ ___/ __/_____/ __  / _ \/ /_/ / __ \/ / __/ / __ \/ __ \/ ___/  (_)
# ___/ / /_/ /_/ / /  / /_/_____/ /_/ /  __/ __/ / / / / / /_/ / /_/ / / / (__  )  _   
#/____/\__/\__,_/_/   \__/      \__,_/\___/_/ /_/_/ /_/_/\__/_/\____/_/ /_/____/  (_)  
#     
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

firstStart = True

if DisplayTechnology == 'spi1322':
   from luma.core.interface.serial import spi
   from luma.oled.device import ssd1322
   from modules.displayFull import*
   from config.ScreenConfig import*

if DisplayTechnology == 'Braun':
   from luma.core.interface.serial import spi
   from luma.oled.device import ssd1322
   from modules.displayBraun import*
   from config.ScreenConfigBraun import*

if DisplayTechnology == 'i2c1306':
    from luma.core.interface.serial import i2c
    from luma.oled.device import ssd1306
    from modules.display1306 import*
    from config.ScreenConfig1306 import*

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
STATE_SCREEN_MENU = 3

UPDATE_INTERVAL = 0.034

if DisplayTechnology == 'spi1322' or DisplayTechnology == 'Braun':
    interface = spi(device=0, port=0)
    oled = ssd1322(interface, rotate=oledrotation) 
    oled.WIDTH = 256
    oled.HEIGHT = 64
if DisplayTechnology == 'i2c1306':
    interface = i2c(port=1, address=0x3C)
    oled = ssd1306(interface) #, rotate=oledrotation)
    oled.WIDTH = 128
    oled.HEIGHT = 64 

oled.state = 'stop'
oled.stateTimeout = 0
oled.playstateIcon = ''
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
if DisplayTechnology != 'i2c1306':
    oled.date = now.strftime("%d.%m.%Y")   #resolves time as dd.mm.YYYY eg. 17.04.2020
if DisplayTechnology == 'i2c1306':
    oled.date = now.strftime("%d.%m.%Y")   #resolves time as dd.mm.YYYY eg. 17.04.2020
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
varcanc = True                      #helper for pause -> stop timeout counter
secvar = 0.0
oled.volume = 100
oled.SelectedScreen = NowPlayingLayout

oled.selQueue = ''

if DisplayTechnology != 'i2c1306':
    image = Image.new('RGB', (oled.WIDTH, oled.HEIGHT))  #for Pixelshift: (oled.WIDTH + 4, oled.HEIGHT + 4)) 
if DisplayTechnology == 'i2c1306':
    image = Image.new('1', (oled.WIDTH, oled.HEIGHT))  #for Pixelshift: (oled.WIDTH + 4, oled.HEIGHT + 4))  
oled.clear()
#________________________________________________________________________________________
#________________________________________________________________________________________
#	
#    ______            __           
#   / ____/___  ____  / /______   _ 
#  / /_  / __ \/ __ \/ __/ ___/  (_)
# / __/ / /_/ / / / / /_(__  )  _   
#/_/    \____/_/ /_/\__/____/  (_)  
#
if DisplayTechnology != 'i2c1306':  
    font = load_font('Oxanium-Bold.ttf', 18)                       #used for Artist ('Oxanium-Bold.ttf', 20)  
    font2 = load_font('Oxanium-Light.ttf', 12)                     #used for all menus
    font3 = load_font('Oxanium-Regular.ttf', 16)                   #used for Song ('Oxanium-Regular.ttf', 18) 
    font4 = load_font('Oxanium-Medium.ttf', 12)                    #used for Format/Smplerate/Bitdepth
    font5 = load_font('Oxanium-Medium.ttf', 12)                    #used for Artist / Screen5
    font6 = load_font('Oxanium-Regular.ttf', 12)                   #used for Song / Screen5
    font7 = load_font('Oxanium-Light.ttf', 10)                     #used for all other / Screen5
    font8 = load_font('Oxanium-Regular.ttf', 10)                   #used for Song / Screen5
    mediaicon = load_font('fa-solid-900.ttf', 10)    	           #used for icon in Media-library info
    iconfont = load_font('entypo.ttf', oled.HEIGHT)                #used for play/pause/stop/shuffle/repeat... icons
    labelfont = load_font('entypo.ttf', 12)                        #used for Menu-icons
    iconfontBottom = load_font('entypo.ttf', 10)                   #used for icons under the screen / button layout
    fontClock = load_font('DSG.ttf', 30)                           #used for clock
    fontDate = load_font('Oxanium-Light.ttf', 12)           #used for Date 'DSEG7Classic-Regular.ttf'
    fontIP = load_font('Oxanium-Light.ttf', 12)             #used for IP 'DSEG7Classic-Regular.ttf'
if DisplayTechnology == 'i2c1306':
    font = load_font('Oxanium-Bold.ttf', 16)                       #used for Artist
    font2 = load_font('Oxanium-Light.ttf', 12)                     #used for all menus
    font3 = load_font('Oxanium-Regular.ttf', 14)                   #used for Song
    font4 = load_font('Oxanium-Medium.ttf', 12)                    #used for Format/Smplerate/Bitdepth
    mediaicon = load_font('fa-solid-900.ttf', 10)    	           #used for icon in Media-library info
    iconfont = load_font('entypo.ttf', oled.HEIGHT)                #used for play/pause/stop/shuffle/repeat... icons
    labelfont = load_font('entypo.ttf', 12)                        #used for Menu-icons
    iconfontBottom = load_font('entypo.ttf', 10)                   #used for icons under the screen / button layout
    fontClock = load_font('DSG.ttf', 24)                           #used for clock
    fontDate = load_font('Oxanium-Medium.ttf.ttf', 12)           #used for Date 
    fontIP = load_font('Oxanium-Medium.ttf.ttf', 12)             #used for IP      
#above are the "imports" for the fonts. 
#After the name of the font comes a number, this defines the Size (height) of the letters. 
#Just put .ttf file in the 'Volumio-OledUI/fonts' directory and make an import like above. 
#________________________________________________________________________________________
#________________________________________________________________________________________
#
#   _____ __                  ____                __                _          
#  / ___// /_____ _____  ____/ / /_  __  __      / /   ____  ____ _(_)____   _ 
#  \__ \/ __/ __ `/ __ \/ __  / __ \/ / / /_____/ /   / __ \/ __ `/ / ___/  (_)
# ___/ / /_/ /_/ / / / / /_/ / /_/ / /_/ /_____/ /___/ /_/ / /_/ / / /__   _   
#/____/\__/\__,_/_/ /_/\__,_/_.___/\__, /     /_____/\____/\__, /_/\___/  (_)  
#                                 /____/                  /____/               
#
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
            show_logo(oledShutdownLogo, oled)
            volumioIO.emit('shutdown')
        elif StandbySignal == 1:
            sleep(1)

def sigterm_handler(signal, frame):
    oled.ShutdownFlag = True
    volumioIO.emit('stop')
    GPIO.output(13, GPIO.LOW)
    oled.clear()
    show_logo("shutdown.ppm", oled)
    print('booyah! bye bye')
#________________________________________________________________________________________
#________________________________________________________________________________________
#
#    ________        ___       __                        
#   /  _/ __ \      /   | ____/ /_______  __________   _ 
#   / // /_/ /_____/ /| |/ __  / ___/ _ \/ ___/ ___/  (_)
# _/ // ____/_____/ ___ / /_/ / /  /  __(__  |__  )  _   
#/___/_/         /_/  |_\__,_/_/   \___/____/____/  (_)  
#   
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
#________________________________________________________________________________________
#________________________________________________________________________________________
#    ____              __        __  __          
#   / __ )____  ____  / /_      / / / /___     _ 
#  / __  / __ \/ __ \/ __/_____/ / / / __ \   (_)
# / /_/ / /_/ / /_/ / /_/_____/ /_/ / /_/ /  _   
#/_____/\____/\____/\__/      \____/ .___/  (_)  
#                                 /_/            
#
signal.signal(signal.SIGTERM, sigterm_handler)
if StandbyActive == True and firstStart == True:
    StandByListen = threading.Thread(target=StandByWatcher, daemon=True)
    StandByListen.start()
    if ledActive != True:
       firstStart = False

GetIP()

if ledActive == True and firstStart == True:
    SysStart()
    Processor = threading.Thread(target=CPUload, daemon=True)
    Processor.start()
    firstStart = False
#________________________________________________________________________________________
#________________________________________________________________________________________
#
#    ____  _            __                  __  __          __      __           
#   / __ \(_)________  / /___ ___  __      / / / /___  ____/ /___ _/ /____     _ 
#  / / / / / ___/ __ \/ / __ `/ / / /_____/ / / / __ \/ __  / __ `/ __/ _ \   (_)
# / /_/ / (__  ) /_/ / / /_/ / /_/ /_____/ /_/ / /_/ / /_/ / /_/ / /_/  __/  _   
#/_____/_/____/ .___/_/\__,_/\__, /      \____/ .___/\__,_/\__,_/\__/\___/  (_)  
#            /_/            /____/           /_/                                 
#
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
#________________________________________________________________________________________
#________________________________________________________________________________________
#
#   ____  __      _           __ _           
#  / __ \/ /_    (_)__  _____/ /( )_____   _ 
# / / / / __ \  / / _ \/ ___/ __/// ___/  (_)
#/ /_/ / /_/ / / /  __/ /__/ /_  (__  )  _   
#\____/_.___/_/ /\___/\___/\__/ /____/  (_)  
#          /___/                             
#
def SetState(status):
    oled.state = status
    if oled.state == STATE_PLAYER:
        oled.modal = NowPlayingScreen(oled.HEIGHT, oled.WIDTH) 
    elif oled.state == STATE_QUEUE_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH)
    elif oled.state == STATE_LIBRARY_INFO:
        oled.modal = MediaLibrarayInfo(oled.HEIGHT, oled.WIDTH)
    elif oled.state == STATE_SCREEN_MENU:
        oled.modal = ScreenSelectMenu(oled.HEIGHT, oled.WIDTH)

#________________________________________________________________________________________
#________________________________________________________________________________________
#        
#    ____        __              __  __                ____              
#   / __ \____ _/ /_____ _      / / / /___ _____  ____/ / /__  _____   _ 
#  / / / / __ `/ __/ __ `/_____/ /_/ / __ `/ __ \/ __  / / _ \/ ___/  (_)
# / /_/ / /_/ / /_/ /_/ /_____/ __  / /_/ / / / / /_/ / /  __/ /     _   
#/_____/\__,_/\__/\__,_/     /_/ /_/\__,_/_/ /_/\__,_/_/\___/_/     (_)  
#   
def onPushState(data):
    if oled.state is not 3:
        global OPDsave	
        global newStatus #global definition for newStatus, used at the end-loop to update standby
        global newSong
        global newArtist
        global newFormat
        OPDsave = data    
    
        if 'title' in data:
            newSong = data['title']
        else:
            newSong = ''
        if newSong is None:
            newSong = ''
        if newSong == 'HiFiBerry ADC':
            newSong = 'Bluetooth-Audio'
            
        if 'artist' in data:
            newArtist = data['artist']
        else:
            newArtist = ''
        if newArtist is None and newSong != 'HiFiBerry ADC':   #volumio can push NoneType
            newArtist = ''
        if newArtist == '' and newSong == 'HiFiBerry ADC':
            newArtist = 'Line-Input:'
    	
        if 'stream' in data:
            newFormat = data['stream']
        else:
            newFormat = ''
        if newFormat is None:
            newFormat = ''
        if newFormat == True and newSong != 'HiFiBerry ADC':
           newFormat = 'WebRadio'
        if newFormat == True and newSong == 'HiFiBerry ADC':
            newFormat = 'Live-Stream'
    
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
            varcanc = True                      #helper for pause -> stop timeout counter
            secvar = 0.0
            if oled.state == STATE_PLAYER and newStatus != 'stop':                                          #this is the "NowPlayingScreen"
                #SetState(STATE_PLAYER)
                if ledActive == True:
                   PlayLEDon()
                oled.modal.UpdatePlayingInfo()     #here is defined which "data" should be displayed in the class
            if oled.state == STATE_PLAYER and newStatus == 'stop':                                          #this is the "Standby-Screen"
                if ledActive == True:
                   PlayLEDoff()
                   StereoLEDoff()

            
        if newStatus != oled.playState:
            varcanc = True                      #helper for pause -> stop timeout counter
    #        secvar = 0.0
            oled.playState = newStatus
            if oled.state == STATE_PLAYER:
                if oled.playState != 'stop':
                    if newStatus == 'pause':
                        if ledActive == True:
                            PlayLEDoff()
                        oled.playstateIcon = oledpauseIcon
                    if newStatus == 'play':
                        if ledActive == True:
                            PlayLEDon()
                        oled.playstateIcon = oledplayIcon
                    #SetState(STATE_PLAYER)
                    oled.modal.UpdatePlayingInfo()
                else:
                    if ledActive == True:
                        PlayLEDoff()
                        StereoLEDoff()
                    SetState(STATE_PLAYER)
                    oled.modal.UpdateStandbyInfo()

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
#________________________________________________________________________________________
#________________________________________________________________________________________
#	
#    ____  _            __                  __  ___                _           
#   / __ \(_)________  / /___ ___  __      /  |/  /__  ____  __  _( )_____   _ 
#  / / / / / ___/ __ \/ / __ `/ / / /_____/ /|_/ / _ \/ __ \/ / / /// ___/  (_)
# / /_/ / (__  ) /_/ / / /_/ / /_/ /_____/ /  / /  __/ / / / /_/ / (__  )  _   
#/_____/_/____/ .___/_/\__,_/\__, /     /_/  /_/\___/_/ /_/\__,_/ /____/  (_)  
#            /_/            /____/                                             
#
class NowPlayingScreen():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def UpdatePlayingInfo(self):
        if DisplayTechnology != 'i2c1306': 
            self.image = Image.new('RGB', (self.width, self.height))
            self.draw = ImageDraw.Draw(self.image)
        if DisplayTechnology == 'i2c1306':
            self.image = Image.new('1', (self.width, self.height))
            self.draw = ImageDraw.Draw(self.image)
        
    def UpdateStandbyInfo(self):
        if DisplayTechnology != 'i2c1306': 
            self.image = Image.new('RGB', (self.width, self.height))
            self.draw = ImageDraw.Draw(self.image)
        if DisplayTechnology == 'i2c1306':
            self.image = Image.new('1', (self.width, self.height))
            self.draw = ImageDraw.Draw(self.image)

    def DrawOn(self, image):
        if NowPlayingLayout == 'Spectrum-Left' and newStatus != 'stop' and DisplayTechnology != 'i2c1306':
            if newStatus != 'stop' and oled.duration != None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')
                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((Screen1specDistance+i*Screen1specWide1, Screen1specYposTag, Screen1specDistance+i*Screen1specWide1+Screen1specWide2, Screen1specYposTag-int(data[i])), outline = Screen1specBorder, fill =Screen1specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            pass
                self.playbackPoint = oled.seek / oled.duration / 10
                self.bar = Screen1barwidth * self.playbackPoint / 100
                self.draw.text((Screen1text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen1text02), oled.activeSong, font=font3, fill='white')
                self.draw.text((Screen1text28), oled.playstateIcon, font=labelfont, fill='white')
                self.draw.text((Screen1text06), oled.activeFormat, font=font4, fill='white')
                self.draw.text((Screen1text07), oled.activeSamplerate, font=font4, fill='white')
                self.draw.text((Screen1text08), oled.activeBitdepth, font=font4, fill='white')
                self.draw.text((Screen1ActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font4, fill='white')
                self.draw.text((Screen1DurationText), str(timedelta(seconds=oled.duration)), font=font4, fill='white')
                self.draw.rectangle((Screen1barLineX , Screen1barLineThick1, Screen1barLineX+Screen1barwidth, Screen1barLineThick2), outline=Screen1barLineBorder, fill=Screen1barLineFill)
                self.draw.rectangle((self.bar+Screen1barLineX-Screen1barNibbleWidth, Screen1barThick1, Screen1barX+self.bar+Screen1barNibbleWidth, Screen1barThick2), outline=Screen1barBorder, fill=Screen1barFill)
                image.paste(self.image, (0, 0))

            if newStatus != 'stop' and oled.duration == None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')
                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((Screen11specDistance+i*Screen11specWide1, Screen11specYposTag, Screen11specDistance+i*Screen11specWide1+Screen11specWide2, Screen11specYposTag-int(data[i])), outline = Screen11specBorder, fill = Screen11specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            pass
                self.draw.text((Screen1text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen1text02), oled.activeSong, font=font3, fill='white')
                image.paste(self.image, (0, 0))

        if NowPlayingLayout == 'Spectrum-Center' and newStatus != 'stop' and DisplayTechnology != 'i2c1306':
            if newStatus != 'stop' and oled.duration != None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')
                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((Screen2specDistance+i*Screen2specWide1, Screen2specYposTag, Screen2specDistance+i*Screen2specWide1+Screen2specWide2, Screen2specYposTag-int(data[i])), outline = Screen2specBorder, fill =Screen2specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            pass
                self.playbackPoint = oled.seek / oled.duration / 10
                self.bar = Screen2barwidth * self.playbackPoint / 100
                self.draw.text((Screen2text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen2text02), oled.activeSong, font=font3, fill='white')
                self.draw.text((Screen2text28), oled.playstateIcon, font=labelfont, fill='white')
                self.draw.text((Screen2text06), oled.activeFormat, font=font4, fill='white')
                self.draw.text((Screen2text07), oled.activeSamplerate, font=font4, fill='white')
                self.draw.text((Screen2text08), oled.activeBitdepth, font=font4, fill='white')
                self.draw.text((Screen2ActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font4, fill='white')
                self.draw.text((Screen2DurationText), str(timedelta(seconds=oled.duration)), font=font4, fill='white')
                self.draw.rectangle((Screen2barLineX , Screen2barLineThick1, Screen2barLineX+Screen2barwidth, Screen2barLineThick2), outline=Screen2barLineBorder, fill=Screen2barLineFill)
                self.draw.rectangle((self.bar+Screen2barLineX-Screen2barNibbleWidth, Screen2barThick1, Screen2barX+self.bar+Screen2barNibbleWidth, Screen2barThick2), outline=Screen2barBorder, fill=Screen2barFill)
                image.paste(self.image, (0, 0))

            if newStatus != 'stop' and oled.duration == None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')
                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((Screen22specDistance+i*Screen22specWide1, Screen22specYposTag, Screen22specDistance+i*Screen22specWide1+Screen22specWide2, Screen22specYposTag-int(data[i])), outline = Screen22specBorder, fill = Screen22specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            pass
                self.draw.text((Screen2text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen2text02), oled.activeSong, font=font3, fill='white')
                image.paste(self.image, (0, 0))

        if NowPlayingLayout == 'Spectrum-Right' and newStatus != 'stop' and DisplayTechnology != 'i2c1306':
            if newStatus != 'stop' and oled.duration != None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')
                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((Screen3specDistance-i*Screen3specWide1, Screen3specYposTag, Screen3specDistance-i*Screen3specWide1+Screen3specWide2, Screen3specYposTag-int(data[i])), outline = Screen3specBorder, fill =Screen3specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            pass
                self.playbackPoint = oled.seek / oled.duration / 10
                self.bar = Screen3barwidth * self.playbackPoint / 100
                self.draw.text((Screen3text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen3text02), oled.activeSong, font=font3, fill='white')
                self.draw.text((Screen3text28), oled.playstateIcon, font=labelfont, fill='white')
                self.draw.text((Screen3text06), oled.activeFormat, font=font4, fill='white')
                self.draw.text((Screen3text07), oled.activeSamplerate, font=font4, fill='white')
                self.draw.text((Screen3text08), oled.activeBitdepth, font=font4, fill='white')
                self.draw.text((Screen3ActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font4, fill='white')
                self.draw.text((Screen3DurationText), str(timedelta(seconds=oled.duration)), font=font4, fill='white')
                self.draw.rectangle((Screen3barLineX , Screen3barLineThick1, Screen3barLineX+Screen3barwidth, Screen3barLineThick2), outline=Screen3barLineBorder, fill=Screen3barLineFill)
                self.draw.rectangle((self.bar+Screen3barLineX-Screen3barNibbleWidth, Screen3barThick1, Screen3barX+self.bar+Screen3barNibbleWidth, Screen3barThick2), outline=Screen3barBorder, fill=Screen3barFill)
                image.paste(self.image, (0, 0))

            if newStatus != 'stop' and oled.duration == None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')
                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((Screen33specDistance+i*Screen33specWide1, Screen33specYposTag, Screen33specDistance+i*Screen33specWide1+Screen33specWide2, Screen33specYposTag-int(data[i])), outline = Screen33specBorder, fill = Screen33specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            pass
                self.draw.text((Screen3text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen3text02), oled.activeSong, font=font3, fill='white')
                image.paste(self.image, (0, 0))

        if NowPlayingLayout == 'No-Spectrum' and newStatus != 'stop' and DisplayTechnology != 'i2c1306':
            if newStatus != 'stop' and oled.duration != None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                self.playbackPoint = oled.seek / oled.duration / 10
                self.bar = Screen4barwidth * self.playbackPoint / 100
                self.draw.text((Screen4text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen4text02), oled.activeSong, font=font3, fill='white')
                self.draw.text((Screen4text28), oled.playstateIcon, font=labelfont, fill='white')
                self.draw.text((Screen4text06), oled.activeFormat, font=font4, fill='white')
                self.draw.text((Screen4text07), oled.activeSamplerate, font=font4, fill='white')
                self.draw.text((Screen4text08), oled.activeBitdepth, font=font4, fill='white')
                self.draw.text((Screen4ActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font4, fill='white')
                self.draw.text((Screen4DurationText), str(timedelta(seconds=oled.duration)), font=font4, fill='white')
                self.draw.rectangle((Screen4barLineX , Screen4barLineThick1, Screen4barLineX+Screen4barwidth, Screen4barLineThick2), outline=Screen4barLineBorder, fill=Screen4barLineFill)
                self.draw.rectangle((self.bar+Screen4barLineX-Screen4barNibbleWidth, Screen4barThick1, Screen4barX+self.bar+Screen4barNibbleWidth, Screen4barThick2), outline=Screen4barBorder, fill=Screen4barFill)
                image.paste(self.image, (0, 0))

            if newStatus != 'stop' and oled.duration == None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                self.draw.text((Screen4text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen4text02), oled.activeSong, font=font3, fill='white')
                image.paste(self.image, (0, 0))

        if NowPlayingLayout == 'Modern' and newStatus != 'stop' and DisplayTechnology != 'i2c1306':
            if newStatus != 'stop' and oled.duration != None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                cava2_fifo = open("/tmp/cava2_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')
                data2 = cava2_fifo.readline().strip().split(';')
                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((Screen5specDistance+i*Screen5specWide1, Screen5specYposTag, Screen5specDistance+i*Screen5specWide1+Screen5specWide2, Screen5specYposTag-int(data[i])), outline = Screen5specBorder, fill =Screen5specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            continue
                if len(data2) >= 3:
                    leftVU = data2[0]
                    rightVU = data2[1]
                    if leftVU != '':
                        leftVU1 = int(leftVU)
                        for i in range(leftVU1):
                            try:
                                self.draw.rectangle((Screen5leftVUDistance+i*Screen5leftVUWide1, Screen5leftVUYpos1, i*Screen5leftVUWide1+Screen5leftVUWide2, Screen5leftVUYpos2), outline = Screen5leftVUBorder, fill = Screen5leftVUFill)
                            except:
                                continue
                    if rightVU != '':
                        rightVU2 = int(rightVU)        
                        for i in range(rightVU2):
                            try:
                                self.draw.rectangle((Screen5rightVUDistance-i*Screen5rightVUWide1, Screen5rightVUYpos1, Screen5rightVUDistance-i*Screen5rightVUWide1+Screen5rightVUWide2, Screen5rightVUYpos2), outline = Screen5rightVUBorder, fill = Screen5rightVUFill)
                            except:
                                continue    
                self.playbackPoint = oled.seek / oled.duration / 10
                self.bar = Screen5barwidth * self.playbackPoint / 100
                TextBaustein = oled.activeArtist + ' - ' + oled.activeSong
                self.textwidth, self.textheight = self.draw.textsize(TextBaustein, font=font6)
                position = Screen5text01
                if self.textwidth <= self.width:
                    position = (int((self.width-self.textwidth)/2), position[1])
                self.draw.text((position), TextBaustein, font=font6, fill='white')
                self.draw.line((0, 36, 255, 36), fill='white', width=1)
                self.draw.line((0, 47, 64, 47), fill='white', width=1)
                self.draw.line((64, 47, 70, 36), fill='white', width=1)
                self.draw.line((190, 47, 255, 47), fill='white', width=1)
                self.draw.line((184, 36, 190, 47), fill='white', width=1)
                self.draw.text((Screen5text28), oled.playstateIcon, font=labelfont, fill='white')
                self.draw.text((Screen5text06), oled.activeFormat, font=font7, fill='white')
                self.draw.text((Screen5text07), oled.activeSamplerate, font=font7, fill='white')
                self.draw.text((Screen5text08), oled.activeBitdepth, font=font7, fill='white')
                self.draw.text((Screen5ActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font7, fill='white')
                self.draw.text((Screen5DurationText), str(timedelta(seconds=oled.duration)), font=font7, fill='white')
                self.draw.rectangle((Screen5barLineX , Screen5barLineThick1, Screen5barLineX+Screen5barwidth, Screen5barLineThick2), outline=Screen5barLineBorder, fill=Screen5barLineFill)
                self.draw.rectangle((self.bar+Screen5barLineX-Screen5barNibbleWidth, Screen5barThick1, Screen5barX+self.bar+Screen5barNibbleWidth, Screen5barThick2), outline=Screen5barBorder, fill=Screen5barFill)
                image.paste(self.image, (0, 0))

            if newStatus != 'stop' and oled.duration == None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                cava2_fifo = open("/tmp/cava2_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')
                data2 = cava2_fifo.readline().strip().split(';')
                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((Screen55specDistance+i*Screen55specWide1, Screen55specYposTag, Screen55specDistance+i*Screen55specWide1+Screen55specWide2, Screen55specYposTag-int(data[i])), outline = Screen55specBorder, fill =Screen55specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            continue
                if len(data2) >= 3:
                    leftVU = data2[0]
                    rightVU = data2[1]
                    if leftVU != '':
                        leftVU1 = int(leftVU)
                        for i in range(leftVU1):
                            try:
                                self.draw.rectangle((Screen55leftVUDistance+i*Screen55leftVUWide1, Screen55leftVUYpos1, i*Screen55leftVUWide1+Screen55leftVUWide2, Screen55leftVUYpos2), outline = Screen55leftVUBorder, fill = Screen55leftVUFill)
                            except:
                                continue
                    if rightVU != '':
                        rightVU2 = int(rightVU)
   
                        for i in range(rightVU2):
                            try:
                                self.draw.rectangle((Screen55rightVUDistance-i*Screen55rightVUWide1, Screen55rightVUYpos1, Screen55rightVUDistance-i*Screen55rightVUWide1+Screen55rightVUWide2, Screen55rightVUYpos2), outline = Screen55rightVUBorder, fill = Screen55rightVUFill)
                            except:
                                continue    
                TextBaustein = oled.activeArtist + ' - ' + oled.activeSong
                self.textwidth, self.textheight = self.draw.textsize(TextBaustein, font=font6)
                position = Screen5text01
                if self.textwidth <= self.width:
                    position = (int((self.width-self.textwidth)/2), position[1])
                self.draw.text((position), TextBaustein, font=font6, fill='white')
                self.draw.line((0, 36, 255, 36), fill='white', width=1)
                self.draw.line((0, 47, 64, 47), fill='white', width=1)
                self.draw.line((64, 47, 70, 36), fill='white', width=1)
                self.draw.line((190, 47, 255, 47), fill='white', width=1)
                self.draw.line((184, 36, 190, 47), fill='white', width=1)
                self.textwidth1, self.textheight1 = self.draw.textsize(oled.activeFormat, font=font6)
                position1 = Screen5text06
                if self.textwidth1 < self.width:
                    position1 = (int((8+self.width-self.textwidth1)/2), position1[1])
                self.draw.text((position1), oled.activeFormat, font=font7, fill='white')
                image.paste(self.image, (0, 0))

        if NowPlayingLayout == 'VU-Meter-1' and newStatus != 'stop' and DisplayTechnology != 'i2c1306':
            self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
            logoImage = Image.open('/home/volumio/NR1-UI/img/vu.png').convert('RGB')
            self.image.paste(logoImage, (0, 0))
            cava2_fifo = open("/tmp/cava2_fifo", 'r')
            data2 = cava2_fifo.readline().strip().split(';')
            TextBaustein = oled.activeArtist + ' - ' + oled.activeSong
            self.textwidth, self.textheight = self.draw.textsize(TextBaustein, font=font6)
            position = Screen6text01
            if self.textwidth <= self.width:
                position = (int((self.width-self.textwidth)/2), position[1])
            self.draw.text((position), TextBaustein, font=font5, fill='white')
            self.draw.text((Screen6text28), oled.playstateIcon, font=labelfont, fill='white')
            if len(data2) >= 3:
                leftVU = data2[0]
                if leftVU != '':
                    leftVU1 = int(leftVU)
                    if leftVU1 == 0:
                        self.draw.line((63, 160, 5, 47), fill='white', width=2)
                    elif leftVU1 == 1:
                        self.draw.line((63, 160, 8, 45), fill='white', width=2)
                    elif leftVU1 == 2:
                        self.draw.line((63, 160, 11, 43), fill='white', width=2)
                    elif leftVU1 == 3:
                        self.draw.line((63, 160, 14, 41), fill='white', width=2)
                    elif leftVU1 == 4:
                        self.draw.line((63, 160, 17, 40), fill='white', width=2)
                    elif leftVU1 == 5:
                        self.draw.line((63, 160, 20, 39), fill='white', width=2)
                    elif leftVU1 == 6:
                        self.draw.line((63, 160, 23, 37), fill='white', width=2)
                    elif leftVU1 == 7:
                        self.draw.line((63, 160, 26, 35), fill='white', width=2)
                    elif leftVU1 == 8:
                        self.draw.line((63, 160, 29, 34), fill='white', width=2)
                    elif leftVU1 == 9:
                        self.draw.line((63, 160, 32, 33), fill='white', width=2)
                    elif leftVU1 == 10:
                        self.draw.line((63, 160, 35, 32), fill='white', width=2)
                    elif leftVU1 == 11:
                        self.draw.line((63, 160, 38, 31), fill='white', width=2)
                    elif leftVU1 == 12:
                        self.draw.line((63, 160, 41, 31), fill='white', width=2)
                    elif leftVU1 == 13:
                        self.draw.line((63, 160, 44, 30), fill='white', width=2)
                    elif leftVU1 == 14:
                        self.draw.line((63, 160, 47, 30), fill='white', width=2)
                    elif leftVU1 == 15:
                        self.draw.line((63, 160, 50, 29), fill='white', width=2)        
                    elif leftVU1 == 16:
                        self.draw.line((63, 160, 53, 28), fill='white', width=2)
                    elif leftVU1 == 17:
                        self.draw.line((63, 160, 56, 28), fill='white', width=2)
                    elif leftVU1 == 18:
                        self.draw.line((63, 160, 59, 28), fill='white', width=2)
                    elif leftVU1 == 19:
                        self.draw.line((63, 160, 62, 28), fill='white', width=2)
                    elif leftVU1 == 20:
                        self.draw.line((63, 160, 65, 29), fill='white', width=2)
                    elif leftVU1 == 21:
                        self.draw.line((63, 160, 68, 29), fill='white', width=2)
                    elif leftVU1 == 22:
                        self.draw.line((63, 160, 71, 29), fill='white', width=2)
                    elif leftVU1 == 23:
                        self.draw.line((63, 160, 74, 29), fill='white', width=2)
                    elif leftVU1 == 24:
                        self.draw.line((63, 160, 77, 30), fill='white', width=2)
                    elif leftVU1 == 25:
                        self.draw.line((63, 160, 80, 30), fill='white', width=2)
                    elif leftVU1 == 26:
                        self.draw.line((63, 160, 83, 31), fill='white', width=2)
                    elif leftVU1 == 27:
                        self.draw.line((63, 160, 86, 31), fill='white', width=2)
                    elif leftVU1 == 28:
                        self.draw.line((63, 160, 89, 32), fill='white', width=2)
                    elif leftVU1 == 29:
                        self.draw.line((63, 160, 92, 32), fill='white', width=2)
                    elif leftVU1 == 30:
                        self.draw.line((63, 160, 95, 33), fill='white', width=2)
                    elif leftVU1 == 31:
                        self.draw.line((63, 160, 98, 33), fill='white', width=2)
                    elif leftVU1 == 32:
                        self.draw.line((63, 160, 101, 34), fill='white', width=2)      
                rightVU = data2[1]
                if rightVU != '':
                    rightVU1 = int(rightVU)
                    if rightVU1 == 0:
                        self.draw.line((191, 160, 133, 47), fill='white', width=2)
                    elif rightVU1 == 1:
                        self.draw.line((191, 160, 136, 45), fill='white', width=2)
                    elif rightVU1 == 2:
                        self.draw.line((191, 160, 139, 43), fill='white', width=2)
                    elif rightVU1 == 3:
                        self.draw.line((191, 160, 142, 41), fill='white', width=2)
                    elif rightVU1 == 4:
                        self.draw.line((191, 160, 145, 40), fill='white', width=2)
                    elif rightVU1 == 5:
                        self.draw.line((191, 160, 148, 39), fill='white', width=2)
                    elif rightVU1 == 6:
                        self.draw.line((191, 160, 151, 37), fill='white', width=2)
                    elif rightVU1 == 7:
                        self.draw.line((191, 160, 154, 35), fill='white', width=2)
                    elif rightVU1 == 8:
                        self.draw.line((191, 160, 157, 34), fill='white', width=2)
                    elif rightVU1 == 9:
                        self.draw.line((191, 160, 160, 33), fill='white', width=2)
                    elif rightVU1 == 10:
                        self.draw.line((191, 160, 163, 32), fill='white', width=2)
                    elif rightVU1 == 11:
                        self.draw.line((191, 160, 166, 31), fill='white', width=2)
                    elif rightVU1 == 12:
                        self.draw.line((191, 160, 169, 31), fill='white', width=2)
                    elif rightVU1 == 13:
                        self.draw.line((191, 160, 172, 30), fill='white', width=2)
                    elif rightVU1 == 14:
                        self.draw.line((191, 160, 175, 30), fill='white', width=2)
                    elif rightVU1 == 15:
                        self.draw.line((191, 160, 178, 29), fill='white', width=2)        
                    elif rightVU1 == 16:
                        self.draw.line((191, 160, 181, 28), fill='white', width=2)
                    elif rightVU1 == 17:
                        self.draw.line((191, 160, 184, 28), fill='white', width=2)
                    elif rightVU1 == 18:
                        self.draw.line((191, 160, 187, 28), fill='white', width=2)
                    elif rightVU1 == 19:
                        self.draw.line((191, 160, 190, 28), fill='white', width=2)
                    elif rightVU1 == 20:
                        self.draw.line((191, 160, 193, 29), fill='white', width=2)
                    elif rightVU1 == 21:
                        self.draw.line((191, 160, 196, 29), fill='white', width=2)
                    elif rightVU1 == 22:
                        self.draw.line((191, 160, 199, 29), fill='white', width=2)
                    elif rightVU1 == 23:
                        self.draw.line((191, 160, 202, 29), fill='white', width=2)
                    elif rightVU1 == 24:
                        self.draw.line((191, 160, 205, 30), fill='white', width=2)
                    elif rightVU1 == 25:
                        self.draw.line((191, 160, 208, 30), fill='white', width=2)
                    elif rightVU1 == 26:
                        self.draw.line((191, 160, 211, 31), fill='white', width=2)
                    elif rightVU1 == 27:
                        self.draw.line((191, 160, 214, 31), fill='white', width=2)
                    elif rightVU1 == 28:
                        self.draw.line((191, 160, 217, 32), fill='white', width=2)
                    elif rightVU1 == 29:
                        self.draw.line((191, 160, 220, 32), fill='white', width=2)
                    elif rightVU1 == 30:
                        self.draw.line((191, 160, 223, 33), fill='white', width=2)
                    elif rightVU1 == 31:
                        self.draw.line((191, 160, 226, 33), fill='white', width=2)
                    elif rightVU1 == 32:
                        self.draw.line((191, 160, 229, 34), fill='white', width=2)                      
            image.paste(self.image, (0, 0))

        if NowPlayingLayout == 'VU-Meter-2' and newStatus != 'stop' and DisplayTechnology != 'i2c1306':
            if newStatus != 'stop' and oled.duration != None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                logoImage = Image.open('/home/volumio/NR1-UI/img/vu2.png').convert('RGB')
                self.image.paste(logoImage, (0, 0))
                cava2_fifo = open("/tmp/cava2_fifo", 'r')
                data2 = cava2_fifo.readline().strip().split(';')
                TextBaustein = oled.activeArtist + ' - ' + oled.activeSong
                self.textwidth, self.textheight = self.draw.textsize(TextBaustein, font=font6)
                position = Screen7text01
                if self.textwidth <= self.width:
                    position = (int((self.width-self.textwidth)/2), position[1])
                self.draw.text((position), TextBaustein, font=font5, fill='white')
                self.playbackPoint = oled.seek / oled.duration / 10
                self.bar = Screen7barwidth * self.playbackPoint / 100
                self.draw.text((Screen7text28), oled.playstateIcon, font=labelfont, fill='white')
                self.draw.text((Screen7text06), oled.activeFormat, font=font8, fill='white')
                self.draw.text((Screen7text07), oled.activeSamplerate, font=font8, fill='white')
                self.draw.text((Screen7text08), oled.activeBitdepth, font=font8, fill='white')
                self.draw.text((Screen7ActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font8, fill='white')
                self.draw.text((Screen7DurationText), str(timedelta(seconds=oled.duration)), font=font8, fill='white')
                self.draw.rectangle((Screen7barLineX , Screen7barLineThick1, Screen7barLineX+Screen7barwidth, Screen7barLineThick2), outline=Screen7barLineBorder, fill=Screen7barLineFill)
                self.draw.rectangle((self.bar+Screen7barLineX-Screen7barNibbleWidth, Screen7barThick1, Screen7barX+self.bar+Screen7barNibbleWidth, Screen7barThick2), outline=Screen7barBorder, fill=Screen7barFill)                
                if len(data2) >= 3:
                    leftVU = data2[0]
                    if leftVU != '':
                        leftVU1 = int(leftVU)
                        if leftVU1 == 0:
                            self.draw.line((63, 160, 5, 59), fill='white', width=2)
                        elif leftVU1 == 1:
                            self.draw.line((63, 160, 8, 57), fill='white', width=2)
                        elif leftVU1 == 2:
                            self.draw.line((63, 160, 11, 55), fill='white', width=2)
                        elif leftVU1 == 3:
                            self.draw.line((63, 160, 14, 53), fill='white', width=2)
                        elif leftVU1 == 4:
                            self.draw.line((63, 160, 17, 52), fill='white', width=2)
                        elif leftVU1 == 5:
                            self.draw.line((63, 160, 20, 51), fill='white', width=2)
                        elif leftVU1 == 6:
                            self.draw.line((63, 160, 23, 49), fill='white', width=2)
                        elif leftVU1 == 7:
                            self.draw.line((63, 160, 26, 47), fill='white', width=2)
                        elif leftVU1 == 8:
                            self.draw.line((63, 160, 29, 46), fill='white', width=2)
                        elif leftVU1 == 9:
                            self.draw.line((63, 160, 32, 45), fill='white', width=2)
                        elif leftVU1 == 10:
                            self.draw.line((63, 160, 35, 44), fill='white', width=2)
                        elif leftVU1 == 11:
                            self.draw.line((63, 160, 38, 43), fill='white', width=2)
                        elif leftVU1 == 12:
                            self.draw.line((63, 160, 41, 43), fill='white', width=2)
                        elif leftVU1 == 13:
                            self.draw.line((63, 160, 44, 42), fill='white', width=2)
                        elif leftVU1 == 14:
                            self.draw.line((63, 160, 47, 42), fill='white', width=2)
                        elif leftVU1 == 15:
                            self.draw.line((63, 160, 50, 41), fill='white', width=2)        
                        elif leftVU1 == 16:
                            self.draw.line((63, 160, 53, 40), fill='white', width=2)
                        elif leftVU1 == 17:
                            self.draw.line((63, 160, 56, 40), fill='white', width=2)
                        elif leftVU1 == 18:
                            self.draw.line((63, 160, 59, 40), fill='white', width=2)
                        elif leftVU1 == 19:
                            self.draw.line((63, 160, 62, 40), fill='white', width=2)
                        elif leftVU1 == 20:
                            self.draw.line((63, 160, 65, 41), fill='white', width=2)
                        elif leftVU1 == 21:
                            self.draw.line((63, 160, 68, 41), fill='white', width=2)
                        elif leftVU1 == 22:
                            self.draw.line((63, 160, 71, 41), fill='white', width=2)
                        elif leftVU1 == 23:
                            self.draw.line((63, 160, 74, 41), fill='white', width=2)
                        elif leftVU1 == 24:
                            self.draw.line((63, 160, 77, 42), fill='white', width=2)
                        elif leftVU1 == 25:
                            self.draw.line((63, 160, 80, 42), fill='white', width=2)
                        elif leftVU1 == 26:
                            self.draw.line((63, 160, 83, 43), fill='white', width=2)
                        elif leftVU1 == 27:
                            self.draw.line((63, 160, 86, 43), fill='white', width=2)
                        elif leftVU1 == 28:
                            self.draw.line((63, 160, 89, 44), fill='white', width=2)
                        elif leftVU1 == 29:
                            self.draw.line((63, 160, 92, 44), fill='white', width=2)
                        elif leftVU1 == 30:
                            self.draw.line((63, 160, 95, 45), fill='white', width=2)
                        elif leftVU1 == 31:
                            self.draw.line((63, 160, 98, 45), fill='white', width=2)
                        elif leftVU1 == 32:
                            self.draw.line((63, 160, 101, 46), fill='white', width=2)      
                    rightVU = data2[1]
                    if rightVU != '':
                        rightVU1 = int(rightVU)
                        if rightVU1 == 0:
                            self.draw.line((191, 160, 133, 59), fill='white', width=2)
                        elif rightVU1 == 1:
                            self.draw.line((191, 160, 136, 57), fill='white', width=2)
                        elif rightVU1 == 2:
                            self.draw.line((191, 160, 139, 55), fill='white', width=2)
                        elif rightVU1 == 3:
                            self.draw.line((191, 160, 142, 53), fill='white', width=2)
                        elif rightVU1 == 4:
                            self.draw.line((191, 160, 145, 52), fill='white', width=2)
                        elif rightVU1 == 5:
                            self.draw.line((191, 160, 148, 51), fill='white', width=2)
                        elif rightVU1 == 6:
                            self.draw.line((191, 160, 151, 49), fill='white', width=2)
                        elif rightVU1 == 7:
                            self.draw.line((191, 160, 154, 47), fill='white', width=2)
                        elif rightVU1 == 8:
                            self.draw.line((191, 160, 157, 46), fill='white', width=2)
                        elif rightVU1 == 9:
                            self.draw.line((191, 160, 160, 45), fill='white', width=2)
                        elif rightVU1 == 10:
                            self.draw.line((191, 160, 163, 44), fill='white', width=2)
                        elif rightVU1 == 11:
                            self.draw.line((191, 160, 166, 43), fill='white', width=2)
                        elif rightVU1 == 12:
                            self.draw.line((191, 160, 169, 43), fill='white', width=2)
                        elif rightVU1 == 13:
                            self.draw.line((191, 160, 172, 42), fill='white', width=2)
                        elif rightVU1 == 14:
                            self.draw.line((191, 160, 175, 42), fill='white', width=2)
                        elif rightVU1 == 15:
                            self.draw.line((191, 160, 178, 41), fill='white', width=2)        
                        elif rightVU1 == 16:
                            self.draw.line((191, 160, 181, 40), fill='white', width=2)
                        elif rightVU1 == 17:
                            self.draw.line((191, 160, 184, 40), fill='white', width=2)
                        elif rightVU1 == 18:
                            self.draw.line((191, 160, 187, 40), fill='white', width=2)
                        elif rightVU1 == 19:
                            self.draw.line((191, 160, 190, 40), fill='white', width=2)
                        elif rightVU1 == 20:
                            self.draw.line((191, 160, 193, 41), fill='white', width=2)
                        elif rightVU1 == 21:
                            self.draw.line((191, 160, 196, 41), fill='white', width=2)
                        elif rightVU1 == 22:
                            self.draw.line((191, 160, 199, 41), fill='white', width=2)
                        elif rightVU1 == 23:
                            self.draw.line((191, 160, 202, 41), fill='white', width=2)
                        elif rightVU1 == 24:
                            self.draw.line((191, 160, 205, 42), fill='white', width=2)
                        elif rightVU1 == 25:
                            self.draw.line((191, 160, 208, 42), fill='white', width=2)
                        elif rightVU1 == 26:
                            self.draw.line((191, 160, 211, 43), fill='white', width=2)
                        elif rightVU1 == 27:
                            self.draw.line((191, 160, 214, 43), fill='white', width=2)
                        elif rightVU1 == 28:
                            self.draw.line((191, 160, 217, 44), fill='white', width=2)
                        elif rightVU1 == 29:
                            self.draw.line((191, 160, 220, 44), fill='white', width=2)
                        elif rightVU1 == 30:
                            self.draw.line((191, 160, 223, 45), fill='white', width=2)
                        elif rightVU1 == 31:
                            self.draw.line((191, 160, 226, 45), fill='white', width=2)
                        elif rightVU1 == 32:
                            self.draw.line((191, 160, 229, 45), fill='white', width=2)                      
                image.paste(self.image, (0, 0))

            if newStatus != 'stop' and oled.duration == None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                logoImage = Image.open('/home/volumio/NR1-UI/img/vu2.png').convert('RGB')
                self.image.paste(logoImage, (0, 0))
                cava2_fifo = open("/tmp/cava2_fifo", 'r')
                data2 = cava2_fifo.readline().strip().split(';')
                TextBaustein = oled.activeArtist + ' - ' + oled.activeSong
                self.textwidth, self.textheight = self.draw.textsize(TextBaustein, font=font6)
                position = Screen7text01
                if self.textwidth <= self.width:
                    position = (int((self.width-self.textwidth)/2), position[1])
                self.draw.text((position), TextBaustein, font=font6, fill='white')          
                if len(data2) >= 3:
                    leftVU = data2[0]
                    if leftVU != '':
                        leftVU1 = int(leftVU)
                        if leftVU1 == 0:
                            self.draw.line((63, 160, 5, 59), fill='white', width=2)
                        elif leftVU1 == 1:
                            self.draw.line((63, 160, 8, 57), fill='white', width=2)
                        elif leftVU1 == 2:
                            self.draw.line((63, 160, 11, 55), fill='white', width=2)
                        elif leftVU1 == 3:
                            self.draw.line((63, 160, 14, 53), fill='white', width=2)
                        elif leftVU1 == 4:
                            self.draw.line((63, 160, 17, 52), fill='white', width=2)
                        elif leftVU1 == 5:
                            self.draw.line((63, 160, 20, 51), fill='white', width=2)
                        elif leftVU1 == 6:
                            self.draw.line((63, 160, 23, 49), fill='white', width=2)
                        elif leftVU1 == 7:
                            self.draw.line((63, 160, 26, 47), fill='white', width=2)
                        elif leftVU1 == 8:
                            self.draw.line((63, 160, 29, 46), fill='white', width=2)
                        elif leftVU1 == 9:
                            self.draw.line((63, 160, 32, 45), fill='white', width=2)
                        elif leftVU1 == 10:
                            self.draw.line((63, 160, 35, 44), fill='white', width=2)
                        elif leftVU1 == 11:
                            self.draw.line((63, 160, 38, 43), fill='white', width=2)
                        elif leftVU1 == 12:
                            self.draw.line((63, 160, 41, 43), fill='white', width=2)
                        elif leftVU1 == 13:
                            self.draw.line((63, 160, 44, 42), fill='white', width=2)
                        elif leftVU1 == 14:
                            self.draw.line((63, 160, 47, 42), fill='white', width=2)
                        elif leftVU1 == 15:
                            self.draw.line((63, 160, 50, 41), fill='white', width=2)        
                        elif leftVU1 == 16:
                            self.draw.line((63, 160, 53, 40), fill='white', width=2)
                        elif leftVU1 == 17:
                            self.draw.line((63, 160, 56, 40), fill='white', width=2)
                        elif leftVU1 == 18:
                            self.draw.line((63, 160, 59, 40), fill='white', width=2)
                        elif leftVU1 == 19:
                            self.draw.line((63, 160, 62, 40), fill='white', width=2)
                        elif leftVU1 == 20:
                            self.draw.line((63, 160, 65, 41), fill='white', width=2)
                        elif leftVU1 == 21:
                            self.draw.line((63, 160, 68, 41), fill='white', width=2)
                        elif leftVU1 == 22:
                            self.draw.line((63, 160, 71, 41), fill='white', width=2)
                        elif leftVU1 == 23:
                            self.draw.line((63, 160, 74, 41), fill='white', width=2)
                        elif leftVU1 == 24:
                            self.draw.line((63, 160, 77, 42), fill='white', width=2)
                        elif leftVU1 == 25:
                            self.draw.line((63, 160, 80, 42), fill='white', width=2)
                        elif leftVU1 == 26:
                            self.draw.line((63, 160, 83, 43), fill='white', width=2)
                        elif leftVU1 == 27:
                            self.draw.line((63, 160, 86, 43), fill='white', width=2)
                        elif leftVU1 == 28:
                            self.draw.line((63, 160, 89, 44), fill='white', width=2)
                        elif leftVU1 == 29:
                            self.draw.line((63, 160, 92, 44), fill='white', width=2)
                        elif leftVU1 == 30:
                            self.draw.line((63, 160, 95, 45), fill='white', width=2)
                        elif leftVU1 == 31:
                            self.draw.line((63, 160, 98, 45), fill='white', width=2)
                        elif leftVU1 == 32:
                            self.draw.line((63, 160, 101, 46), fill='white', width=2)      
                    rightVU = data2[1]
                    if rightVU != '':
                        rightVU1 = int(rightVU)
                        if rightVU1 == 0:
                            self.draw.line((191, 160, 133, 59), fill='white', width=2)
                        elif rightVU1 == 1:
                            self.draw.line((191, 160, 136, 57), fill='white', width=2)
                        elif rightVU1 == 2:
                            self.draw.line((191, 160, 139, 55), fill='white', width=2)
                        elif rightVU1 == 3:
                            self.draw.line((191, 160, 142, 53), fill='white', width=2)
                        elif rightVU1 == 4:
                            self.draw.line((191, 160, 145, 52), fill='white', width=2)
                        elif rightVU1 == 5:
                            self.draw.line((191, 160, 148, 51), fill='white', width=2)
                        elif rightVU1 == 6:
                            self.draw.line((191, 160, 151, 49), fill='white', width=2)
                        elif rightVU1 == 7:
                            self.draw.line((191, 160, 154, 47), fill='white', width=2)
                        elif rightVU1 == 8:
                            self.draw.line((191, 160, 157, 46), fill='white', width=2)
                        elif rightVU1 == 9:
                            self.draw.line((191, 160, 160, 45), fill='white', width=2)
                        elif rightVU1 == 10:
                            self.draw.line((191, 160, 163, 44), fill='white', width=2)
                        elif rightVU1 == 11:
                            self.draw.line((191, 160, 166, 43), fill='white', width=2)
                        elif rightVU1 == 12:
                            self.draw.line((191, 160, 169, 43), fill='white', width=2)
                        elif rightVU1 == 13:
                            self.draw.line((191, 160, 172, 42), fill='white', width=2)
                        elif rightVU1 == 14:
                            self.draw.line((191, 160, 175, 42), fill='white', width=2)
                        elif rightVU1 == 15:
                            self.draw.line((191, 160, 178, 41), fill='white', width=2)        
                        elif rightVU1 == 16:
                            self.draw.line((191, 160, 181, 40), fill='white', width=2)
                        elif rightVU1 == 17:
                            self.draw.line((191, 160, 184, 40), fill='white', width=2)
                        elif rightVU1 == 18:
                            self.draw.line((191, 160, 187, 40), fill='white', width=2)
                        elif rightVU1 == 19:
                            self.draw.line((191, 160, 190, 40), fill='white', width=2)
                        elif rightVU1 == 20:
                            self.draw.line((191, 160, 193, 41), fill='white', width=2)
                        elif rightVU1 == 21:
                            self.draw.line((191, 160, 196, 41), fill='white', width=2)
                        elif rightVU1 == 22:
                            self.draw.line((191, 160, 199, 41), fill='white', width=2)
                        elif rightVU1 == 23:
                            self.draw.line((191, 160, 202, 41), fill='white', width=2)
                        elif rightVU1 == 24:
                            self.draw.line((191, 160, 205, 42), fill='white', width=2)
                        elif rightVU1 == 25:
                            self.draw.line((191, 160, 208, 42), fill='white', width=2)
                        elif rightVU1 == 26:
                            self.draw.line((191, 160, 211, 43), fill='white', width=2)
                        elif rightVU1 == 27:
                            self.draw.line((191, 160, 214, 43), fill='white', width=2)
                        elif rightVU1 == 28:
                            self.draw.line((191, 160, 217, 44), fill='white', width=2)
                        elif rightVU1 == 29:
                            self.draw.line((191, 160, 220, 44), fill='white', width=2)
                        elif rightVU1 == 30:
                            self.draw.line((191, 160, 223, 45), fill='white', width=2)
                        elif rightVU1 == 31:
                            self.draw.line((191, 160, 226, 45), fill='white', width=2)
                        elif rightVU1 == 32:
                            self.draw.line((191, 160, 229, 45), fill='white', width=2)                      
                image.paste(self.image, (0, 0))

        if NowPlayingLayout == 'Spectrum-Screen' and newStatus != 'stop' and DisplayTechnology == 'i2c1306':
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                cava_fifo = open("/tmp/cava_fifo", 'r')
                data = cava_fifo.readline().strip().split(';')

                if len(data) >= 64 and newStatus != 'pause':
                    for i in range(0, len(data)-1):
                        try:
                            self.draw.rectangle((i*Screen1specWide1, Screen1specYposTag, i*Screen1specWide1+Screen1specWide2, Screen1specYposTag-int(data[i])), outline = Screen1specBorder, fill =Screen1specFill)  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
                        except:
                            pass
                self.draw.text((Screen1text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen1text02), oled.activeSong, font=font3, fill='white')
                self.draw.text((Screen1text28), oled.playstateIcon, font=labelfont, fill='white')
                self.draw.text((Screen1text06), oled.activeFormat, font=font4, fill='white')
                self.draw.text((Screen1text07), oled.activeSamplerate, font=font4, fill='white')
                self.draw.text((Screen1text08), oled.activeBitdepth, font=font4, fill='white')
                image.paste(self.image, (0, 0))

        if NowPlayingLayout != 'Progress-Bar' and newStatus != 'stop' and DisplayTechnology == 'i2c1306':
            if newStatus != 'stop' and oled.duration != None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                self.playbackPoint = oled.seek / oled.duration / 10
                self.bar = Screen4barwidth * self.playbackPoint / 100
                self.draw.text((Screen4text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen4text02), oled.activeSong, font=font3, fill='white')
                self.draw.text((Screen4text28), oled.playstateIcon, font=labelfont, fill='white')
                self.draw.text((Screen4text06), oled.activeFormat, font=font4, fill='white')
                self.draw.text((Screen4text07), oled.activeSamplerate, font=font4, fill='white')
                self.draw.text((Screen4text08), oled.activeBitdepth, font=font4, fill='white')
                self.draw.text((Screen4ActualPlaytimeText), str(timedelta(seconds=round(float(oled.seek) / 1000))), font=font4, fill='white')
                self.draw.text((Screen4DurationText), str(timedelta(seconds=oled.duration)), font=font4, fill='white')
                self.draw.rectangle((Screen4barLineX , Screen4barLineThick1, Screen4barLineX+Screen4barwidth, Screen4barLineThick2), outline=Screen4barLineBorder, fill=Screen4barLineFill)
                self.draw.rectangle((Screen4barLineX, Screen4barThick1, Screen4barX+self.bar, Screen4barThick2), outline=Screen4barBorder, fill=Screen4barFill)
                image.paste(self.image, (0, 0))

            if newStatus != 'stop' and oled.duration == None:
                self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
                self.draw.text((Screen4text01), oled.activeArtist, font=font, fill='white')
                self.draw.text((Screen4text02), oled.activeSong, font=font3, fill='white')
                image.paste(self.image, (0, 0))

        elif oled.playState == 'stop':
            self.image.paste(('black'), [0, 0, image.size[0], image.size[1]])
            self.draw.text((oledtext03), oled.time, font=fontClock, fill='white')
            self.draw.text((oledtext04), oled.IP, font=fontIP, fill='white')
            self.draw.text((oledtext05), oled.date, font=fontDate, fill='white')
            self.draw.text((oledtext09), oledlibraryInfo, font=iconfontBottom, fill='white')
            image.paste(self.image, (0, 0))

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
        self.text10Pos = oledtext19    						   #LibraryInfoIcon
        self.text11Pos = oledtext20     					   #icon for Artists
        self.text12Pos = oledtext21     					   #icon for Albums
        self.text13Pos = oledtext22    						   #icon for Songs
        self.text14Pos = oledtext23    						   #icon for duration
        if DisplayTechnology == 'spi1322': 
            self.alfaimage = Image.new('RGBA', image.size, (0, 0, 0, 0))

    def UpdateLibraryInfo(self):
        self.LibraryInfoText1 = StaticText(self.height, self.width, oledArt, font4)   	                #Text for Artists
        self.LibraryInfoText2 = StaticText(self.height, self.width, oled.activeArtists, font4)          #Number of Artists
        self.LibraryInfoText3 = StaticText(self.height, self.width, oledAlb, font4)  	                #Text for Albums
        self.LibraryInfoText4 = StaticText(self.height, self.width, oled.activeAlbums, font4)           #Number of Albums
        self.LibraryInfoText5 = StaticText(self.height, self.width, oledSon, font4)   	                #Text for Songs
        self.LibraryInfoText6 = StaticText(self.height, self.width, oled.activeSongs, font4)        	#Number of Songs
        self.LibraryInfoText7 = StaticText(self.height, self.width, oledPla, font4)   	                #Text for duration
        self.LibraryInfoText8 = StaticText(self.height, self.width, oled.activePlaytime, font4)   	    #Summary of duration
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
            self.LibraryInfoText10.DrawOn(image, self.text10Pos)   #LibraryInfo Return
            self.LibraryInfoText11.DrawOn(image, self.text11Pos)   #icon for Artists
            self.LibraryInfoText12.DrawOn(image, self.text12Pos)   #icon for Albums
            self.LibraryInfoText13.DrawOn(image, self.text13Pos)   #icon for Songs
            self.LibraryInfoText14.DrawOn(image, self.text14Pos)   #icon for duration
                  

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

class ScreenSelectMenu():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        index = ScreenList.index(NowPlayingLayout)
        self.selectedOption = int(index)
        self.menurows = oledListEntrys
        self.menuText = [None for i in range(self.menurows)]
        self.menuList = ScreenList
        self.totaloptions = len(ScreenList)
        print(self.totaloptions)
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

#________________________________________________________________________________________
#________________________________________________________________________________________
#	
#    ____        __  __                 ____                 __  _                      
#   / __ )__  __/ /_/ /_____  ____     / __/_  ______  _____/ /_(_)___  ____  _____   _ 
#  / __  / / / / __/ __/ __ \/ __ \   / /_/ / / / __ \/ ___/ __/ / __ \/ __ \/ ___/  (_)
# / /_/ / /_/ / /_/ /_/ /_/ / / / /  / __/ /_/ / / / / /__/ /_/ / /_/ / / / (__  )  _   
#/_____/\__,_/\__/\__/\____/_/ /_/  /_/  \__,_/_/ /_/\___/\__/_/\____/_/ /_/____/  (_)  
#                                                                                       	
def ButtonA_PushEvent(hold_time):
    if hold_time < 2 and oled.state != STATE_LIBRARY_INFO:
        print('ButtonA short press event')
        if oled.state == STATE_PLAYER and oled.playState != 'stop' and newFormat != 'WebRadio':
            if oled.playState == 'play':
                volumioIO.emit('pause')
            else:
                volumioIO.emit('play')
        if oled.state == STATE_PLAYER and oled.playState != 'stop' and newFormat == 'WebRadio':
            volumioIO.emit('stop')
            oled.modal.UpdateStandbyInfo()  

def ButtonB_PushEvent(hold_time):
    if hold_time < 2 and oled.state != STATE_LIBRARY_INFO:
        print('ButtonB short press event')
        if oled.state == STATE_PLAYER and oled.playState != 'stop':
            volumioIO.emit('stop')
            oled.modal.UpdateStandbyInfo()  

def ButtonC_PushEvent(hold_time):
    if hold_time < 2 and oled.state != STATE_LIBRARY_INFO:
        print('ButtonC short press event')
        if oled.state == STATE_PLAYER and oled.playState != 'stop':
            volumioIO.emit('prev')
        if oled.state == STATE_PLAYER and oled.playState == 'stop':
            print ('RightKnob_PushEvent SHORT')
            SetState(STATE_SCREEN_MENU)
            oled.state = 3
            oled.modal = ScreenSelectMenu(oled.HEIGHT, oled.WIDTH)
            sleep(0.2)
    elif oled.state == STATE_PLAYER and oled.playState != 'stop':
        print('ButtonC long press event')
        if repeatTag == False:
            volumioIO.emit('setRepeat', {"value":"true"})
            repeatTag = True            
        elif repeatTag == True:
            volumioIO.emit('setRepeat', {"value":"false"})
            repeatTag = False
       
def ButtonD_PushEvent(hold_time):
    if hold_time < 2:
        print('ButtonD short press event')
        if oled.state == STATE_PLAYER and oled.playState != 'stop':
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
    elif oled.state == STATE_PLAYER and oled.playState != 'stop':
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
    if oled.state == STATE_PLAYER:
        SetState(STATE_QUEUE_MENU)
    elif oled.state == STATE_QUEUE_MENU and dir == RotaryEncoder.LEFT:
        oled.modal.PrevOption()
        oled.selQueue = oled.modal.SelectedOption()
        emit_track = True
    elif oled.state == STATE_QUEUE_MENU and dir == RotaryEncoder.RIGHT:
        oled.modal.NextOption()
        oled.selQueue = oled.modal.SelectedOption()
        emit_track = True
    elif oled.state == STATE_SCREEN_MENU and dir == RotaryEncoder.LEFT:
        oled.modal.PrevOption()
        oled.SelectedScreen = oled.modal.SelectedOption()
    elif oled.state == STATE_SCREEN_MENU and dir == RotaryEncoder.RIGHT:
        oled.modal.NextOption()
        oled.SelectedScreen = oled.modal.SelectedOption()

def RightKnob_PushEvent(hold_time):
    if hold_time < 1:
        if oled.state == STATE_QUEUE_MENU:
            print ('RightKnob_PushEvent SHORT')
            oled.stateTimeout = 0
        if oled.state == STATE_SCREEN_MENU:
            print ('RightKnob_PushEvent Long')
            global NowPlayingLayout
            oled.SelectedScreen = oled.modal.SelectedOption()
            Screen = ScreenList[oled.SelectedScreen]
            WriteSelScreen = open('/home/volumio/NR1-UI/config/LayoutSet.txt', 'w')
            WriteSelScreen.write(Screen)
            WriteSelScreen.close
            NowPlayingLayout = Screen
            SetState(STATE_PLAYER)
            volumioIO.emit('stop') 
#________________________________________________________________________________________
#________________________________________________________________________________________
#    
#    ____        __  __                  _       __      __       __                  
#   / __ )__  __/ /_/ /_____  ____      | |     / /___ _/ /______/ /_  ___  _____   _ 
#  / __  / / / / __/ __/ __ \/ __ \_____| | /| / / __ `/ __/ ___/ __ \/ _ \/ ___/  (_)
# / /_/ / /_/ / /_/ /_/ /_/ / / / /_____/ |/ |/ / /_/ / /_/ /__/ / / /  __/ /     _   
#/_____/\__,_/\__/\__/\____/_/ /_/      |__/|__/\__,_/\__/\___/_/ /_/\___/_/     (_)  
#   
ButtonA_Push = PushButton(oledBtnA, max_time=2)
ButtonA_Push.setCallback(ButtonA_PushEvent)
ButtonB_Push = PushButton(oledBtnB, max_time=2)
ButtonB_Push.setCallback(ButtonB_PushEvent)
ButtonC_Push = PushButton(oledBtnC, max_time=2)
ButtonC_Push.setCallback(ButtonC_PushEvent)
ButtonD_Push = PushButton(oledBtnD, max_time=2)
ButtonD_Push.setCallback(ButtonD_PushEvent)

RightKnob_Push = PushButton(oledRtrBtn, max_time=2)
RightKnob_Push.setCallback(RightKnob_PushEvent)
RightKnob_Rotation = RotaryEncoder(oledRtrLeft, oledRtrRight, pulses_per_cycle=4)
RightKnob_Rotation.setCallback(RightKnob_RotaryEvent)
#________________________________________________________________________________________
#________________________________________________________________________________________
#    
#    ____              __        __                          
#   / __ )____  ____  / /_      / /   ____  ____ _____     _ 
#  / __  / __ \/ __ \/ __/_____/ /   / __ \/ __ `/ __ \   (_)
# / /_/ / /_/ / /_/ / /_/_____/ /___/ /_/ / /_/ / /_/ /  _   
#/_____/\____/\____/\__/     /_____/\____/\__, /\____/  (_)  
#    
show_logo(oledBootLogo, oled)
sleep(2)
SetState(STATE_PLAYER)
#________________________________________________________________________________________
#________________________________________________________________________________________
#  
#   __  __          __      __          ________                        __         
#  / / / /___  ____/ /___ _/ /____     /_  __/ /_  ________  ____ _____/ /____   _ 
# / / / / __ \/ __  / __ `/ __/ _ \     / / / __ \/ ___/ _ \/ __ `/ __  / ___/  (_)
#/ /_/ / /_/ / /_/ / /_/ / /_/  __/    / / / / / / /  /  __/ /_/ / /_/ (__  )  _   
#\____/ .___/\__,_/\__,_/\__/\___/    /_/ /_/ /_/_/   \___/\__,_/\__,_/____/  (_)  
#    /_/ 
#     
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

InfoTag = 0                         #helper for missing Artist/Song when changing sources
GetIP()

def PlaypositionHelper():
    while True:
          volumioIO.emit('getState')
          sleep(1.0)

PlayPosHelp = threading.Thread(target=PlaypositionHelper, daemon=True)
PlayPosHelp.start()
#________________________________________________________________________________________
#________________________________________________________________________________________
#	
#    __  ___      _             __                          
#   /  |/  /___ _(_)___        / /   ____  ____  ____     _ 
#  / /|_/ / __ `/ / __ \______/ /   / __ \/ __ \/ __ \   (_)
# / /  / / /_/ / / / / /_____/ /___/ /_/ / /_/ / /_/ /  _   
#/_/  /_/\__,_/_/_/ /_/     /_____/\____/\____/ .___/  (_)  
#  
while True:
#    print('State: ', oled.state)
#    print('palyState: ', oled.playState)
#    print('newStatus: ', newStatus)
#    print(oled.modal)
    if emit_track and oled.stateTimeout < 4.5:
        emit_track = False
        try:
            SetState(STATE_PLAYER)
            InfoTag = 0
        except IndexError:
            pass
        volumioIO.emit('stop')
        sleep(0.01)
        volumioIO.emit('play', {'value':oled.selQueue})
    sleep(0.1)

#Helper for Format, Samplerate and Bitdepth    
    if oled.state == STATE_PLAYER and InfoTag <= oledPlayFormatRefreshLoopCount and newStatus != 'stop':
        SetState(STATE_PLAYER)
        oled.modal.UpdatePlayingInfo()
        InfoTag += 1
        sleep(oledPlayFormatRefreshTime)

#this is the loop to push the actual time every 0.1sec to the "Standby-Screen"
    if oled.state == STATE_PLAYER and newStatus == 'stop' and oled.ShutdownFlag == False:
        #if oled.state is not 3 or oled.state is not STATE_SCREEN_MENU:
        InfoTag = 0  #resets the InfoTag helper from artist/song update loop
        oled.state = 0
        oled.time = strftime("%H:%M:%S")
        SetState(STATE_PLAYER)
        oled.modal.UpdateStandbyInfo()
        sleep(0.2)  

#if playback is paused, here is defined when the Player goes back to "Standby"/Stop		
    if oled.state == STATE_PLAYER and newStatus == 'pause' and varcanc == True:
        secvar = int(round(time()))
        oled.state = 0
        SetState(STATE_PLAYER)
        varcanc = False
    elif oled.state == STATE_PLAYER and newStatus == 'pause' and int(round(time())) - secvar > oledPause2StopTime:
        varcanc = True
        volumioIO.emit('stop')
        SetState(STATE_PLAYER)
        oled.modal.UpdateStandbyInfo()
        secvar = 0.0

sleep(0.02)

#        date_string = str(uuid.uuid1())
#        print(date_string)
#        image.save('/home/volumio/'+date_string+'.png')
#!/usr/bin/python

from __future__ import unicode_literals

import requests
import os
import sys
import time
import json
import pycurl
import pprint
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 

from time import*
from threading import Thread
from socketIO_client import SocketIO
from datetime import datetime
from io import BytesIO 

# Imports for OLED display
from luma.core.interface.serial import spi
from luma.oled.device import ssd1322
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from modules.pushbutton import PushButton
from modules.rotaryencoder import RotaryEncoder
from modules.display import *

volumio_host = 'localhost'
volumio_port = 3000
VOLUME_DT = 5    #volume adjustment step

volumioIO = SocketIO(volumio_host, volumio_port)

#imports for REST API (MediaInfoScreen)
b_obj = BytesIO() 
crl = pycurl.Curl() 

STATE_NONE = -1
STATE_PLAYER = 0
STATE_PLAYLIST_MENU = 1
STATE_QUEUE_MENU = 2
STATE_VOLUME = 3
STATE_SHOW_INFO = 4
STATE_LIBRARY_MENU = 5
STATE_LIBRARY_INFO = 6

UPDATE_INTERVAL = 0.034
PIXEL_SHIFT_TIME = 120    #time between picture position shifts in sec.

interface = spi(device=0, port=0)
oled = ssd1322(interface, rotate=2) 
#without rotate display is 0 degrees, with rotate=2 its 180 degrees

oled.WIDTH = 256
oled.HEIGHT = 64
oled.state = 'stop'
oled.stateTimeout = 0
oled.timeOutRunning = False
oled.activeSong = ''
oled.activeArtist = 'VOLuMIO'
oled.playState = 'unknown'
oled.playPosition = 0
oled.modal = False
oled.playlistoptions = []
oled.queue = []
oled.libraryFull = []
oled.libraryNames = []
oled.volumeControlDisabled = True
oled.volume = 100
now = datetime.now()                                                             #current date and time
oled.time = now.strftime("%H:%M:%S")                                             #resolves time as HH:MM:SS eg. 14:33:15
oled.date = now.strftime("%d.  %m.  %Y")                                         #resolves time as dd.mm.YYYY eg. 17.04.2020
oled.IP = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]   #resolves IP from Ethernet Adapator
emit_volume = False
emit_track = False
newStatus = 0              							 #makes newStatus usable outside of onPushState
oled.activeFormat = ''      							 #makes oled.activeFormat globaly usable
oled.activeSamplerate = ''  							 #makes oled.activeSamplerate globaly usable
oled.activeBitdepth = ''                                                         #makes oled.activeBitdepth globaly usable
oled.activeArtists = ''                                                          #makes oled.activeArtists globaly usable
oled.activeAlbums = ''                                                           #makes oled.activeAlbums globaly usable
oled.activeSongs = ''                                                      	 #makes oled.activeSongs globaly usable
oled.activePlaytime = ''                                                         #makes oled.activePlaytime globaly usable
oled.Art = 'Interpreten :'                                                       #sets the Artists-text for the MediaLibrarayInfo
oled.Alb = 'Alben :'                                                             #sets the Albums-text for the MediaLibrarayInfo
oled.Son = 'Songs :'                                                             #sets the Songs-text for the MediaLibrarayInfo
oled.Pla = 'Playtime :'                                                          #sets the Playtime-text for the MediaLibrarayInfo
oled.randomTag = False                                                           #helper to detect if "Random/shuffle" is set
oled.repeatTag = False                                                           #helper to detect if "repeat" is set
oled.ShutdownFlag = False                                                           #helper to detect if "shutdown" is running. Prevents artifacts from Standby-Screen during shutdown

image = Image.new('RGB', (oled.WIDTH, oled.HEIGHT))  #for Pixelshift: (oled.WIDTH + 4, oled.HEIGHT + 4)) 
oled.clear()

font = load_font('Oxanium-Bold.ttf', 26)                       #used for Artist
font2 = load_font('Oxanium-Light.ttf', 12)                     #used for all menus
font3 = load_font('Oxanium-Regular.ttf', 22)                   #used for Song
font4 = load_font('Oxanium-Medium.ttf', 14)                    #used for Format/Smplerate/Bitdepth
hugefontaw = load_font('fa-solid-900.ttf', oled.HEIGHT - 4)    #used for play/pause/stop icons -> Status change overlay
iconfont = load_font('entypo.ttf', oled.HEIGHT - 2)           #used for play/pause/stop/shuffle/repeat... icons
fontClock = load_font('DSG.ttf', 41)                           #used for clock
fontDate = load_font('DSEG7Classic-Regular.ttf', 10)           #used for Date 
fontIP = load_font('DSEG7Classic-Regular.ttf', 10)             #used for IP  

#above are the "imports" for the fonts. 
#After the name of the font comes a number, this defines the Size (height) of the letters. 
#Just put .ttf file in the 'Volumio-OledUI/fonts' directory and make an import like above. 

def display_update_service():
    pixshift = [2, 2]
    lastshift = prevTime = time()
    while UPDATE_INTERVAL > 0:
        dt = time() - prevTime
        prevTime = time()
       # auto return to home display screen (from volume display / queue list..)
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
            print "render error"
	    sleep(1)
        cimg = image.crop((pixshift[0], pixshift[1], pixshift[0] + oled.WIDTH, pixshift[1] + oled.HEIGHT)) 
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
        oled.modal = NowPlayingScreen(oled.HEIGHT, oled.WIDTH, oled.activeArtist, oled.activeSong, oled.time, oled.IP, oled.date, oled.activeFormat, oled.activeSamplerate, oled.activeBitdepth, font, fontClock, fontDate, fontIP, font3, font4, iconfont)
        oled.modal.SetPlayingIcon(oled.playState, 0)
    elif oled.state == STATE_VOLUME:
        oled.modal = VolumeScreen(oled.HEIGHT, oled.WIDTH, oled.volume, font, font2)
    elif oled.state == STATE_PLAYLIST_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.playlistoptions, rows=3, label='_/ PlaylistAuswahl \______________________________')
    elif oled.state == STATE_QUEUE_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.queue, rows=4, selected=oled.playPosition, showIndex=True)
    elif oled.state == STATE_LIBRARY_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.libraryNames, rows=3, label='_/ Musikbibliothek \________________________________')
    elif oled.state == STATE_LIBRARY_INFO:
        oled.modal = MediaLibrarayInfo(oled.HEIGHT, oled.WIDTH, oled.activeArtists, oled.activeAlbums, oled.activeSongs, oled.activePlaytime, oled.Art, oled.Alb, oled.Son, oled.Pla, hugefontaw, font4)

def LoadPlaylist(playlistname):
    print ("loading playlist: " + playlistname.encode('ascii', 'ignore'))
    oled.playPosition = 0
    volumioIO.emit('playPlaylist', {'name':playlistname})
    SetState(STATE_PLAYER)

#In 'onPushState' the whole set of media-information is linked to the variables (eg. artist, song...)
#On every change in the Playback (pause, other track, etc.) Volumio pushes a set of informations on port 3000.
#Volumio-OledUI is always listening on this port. If there's new 'data', the "def onPushState(data):" runs again.

def onPushState(data):
	
#    print(data) #for log, if enabled you see the values for 'data'

    OPDsave = data

    global OPDsave	
    global newStatus #global definition for newStatus, used at the end-loop to update standby

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
        
    if oled.state != STATE_VOLUME:              #get volume on startup and remote control
        try:                                    #it is either number or unicode text
            oled.volume = int(data['volume'])
        except (KeyError, ValueError):
            pass
    
    if 'disableVolumeControl' in data:
        oled.volumeControlDisabled = data['disableVolumeControl']
    
    oled.activeFormat = newFormat
    oled.activeSamplerate = newSamplerate
    oled.activeBitdepth = newBitdepth

    print(newSong.encode('ascii', 'ignore'))
    if (newSong != oled.activeSong) or (newArtist != oled.activeArtist):                                # new song and artist
        oled.activeSong = newSong
        oled.activeArtist = newArtist
	if oled.state == STATE_PLAYER and newStatus != 'stop':                                          #this is the "NowPlayingScreen"
            oled.modal.UpdatePlayingInfo(newArtist, newSong, newFormat, newSamplerate, newBitdepth)     #here is defined which "data" should be displayed in the class
	if oled.state == STATE_PLAYER and newStatus == 'stop':                                          #this is the "Standby-Screen"
            oled.modal.UpdateStandbyInfo(oled.time, oled.IP, oled.date)                                 #here is defined which "data" should be displayed in the class
    
    if newStatus != oled.playState:
        oled.playState = newStatus
        if oled.state == STATE_PLAYER:
            if oled.playState == 'play':
                iconTime = 35
            else:
                iconTime = 80
            oled.modal.SetPlayingIcon(oled.playState, iconTime)

def onPushCollectionStats(data):
    data = json.loads(data)             #data import from REST-API (is set when ButtonD short-pressed in Standby)
            
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
	oled.modal.UpdateLibraryInfo(oled.activeArtists, oled.activeAlbums, oled.activeSongs, oled.activePlaytime, oled.Art, oled.Alb, oled.Son, oled.Pla)  

def onPushQueue(data):
    oled.queue = [track['name'] if 'name' in track else 'no track' for track in data]
    print('Queue length is ' + str(len(oled.queue)))

def onPushBrowseSources(data):
#    print('Browse sources:')
#    for item in data:
#        print(item['uri']) 
    pass

def onLibraryBrowse(data):
    oled.libraryFull = data
    itemList = oled.libraryFull['navigation']['lists'][0]['items']
    oled.libraryNames = [item['title'] if 'title' in item else 'empty' for item in itemList]
    SetState(STATE_LIBRARY_MENU)

def EnterLibraryItem(itemNo):
    selectedItem = oled.libraryFull['navigation']['lists'][0]['items'][itemNo]
    print("Entering library item: " + oled.libraryNames[itemNo].encode('ascii', 'ignore'))
    if selectedItem['type'][-8:] == 'category' or selectedItem['type'] == 'folder':
        volumioIO.emit('browseLibrary',{'uri':selectedItem['uri']})
    else:
        print("Sending new Queue")
        volumioIO.emit('clearQueue')        #clear queue and add whole list of items
        oled.queue = []
        volumioIO.emit('addToQueue', oled.libraryFull['navigation']['lists'][0]['items'])
        oled.stateTimeout = 5.0       #maximum time to load new queue
        while len(oled.queue) == 0 and oled.stateTimeout > 0.1:
            sleep(0.1) 
        oled.stateTimeout = 0.2
        print("Play position = " + str(itemNo))
        volumioIO.emit('play', {'value':itemNo})

def LibraryReturn():        #go to parent category
    if not 'prev' in oled.libraryFull['navigation']:
        SetState(STATE_PLAYER)
    else:
        parentCategory = oled.libraryFull['navigation']['prev']['uri']
        print ("Navigating to parent category in library: " + parentCategory.encode('ascii', 'ignore'))
        if parentCategory != '' and parentCategory != '/': 
            volumioIO.emit('browseLibrary',{'uri':parentCategory})
        else:
            SetState(STATE_PLAYER)

def onPushListPlaylist(data):
    global oled
    if len(data) > 0:
        oled.playlistoptions = data

#if you wan't to add more textposition: double check if using STATIC or SCROLL text.
#this needs to be declared two times, first in "self.playingText" AND under: "def UpdatePlayingInfo" or "def UpdateStandbyInfo"

class NowPlayingScreen():
    def __init__(self, height, width, row1, row2, row3, row4, row5, row6, row7, row8, font, fontClock, fontDate, fontIP, font3, font4, iconfont): #this line references to oled.modal = NowPlayingScreen
        self.height = height
        self.width = width
        self.font = font
        self.font3 = font3
        self.font4 = font4
	self.iconfont = iconfont
        self.fontClock = fontClock
        self.fontDate = fontDate
        self.fontIP = fontIP
        self.playingText1 = ScrollText(self.height, self.width, row1, font)         #Artist /center=True
        self.playingText2 = ScrollText(self.height, self.width, row2, font3)        #Title
        self.playingText3 = StaticText(self.height, self.width, row6, font4)        #format / flac,MP3...
        self.playingText4 = StaticText(self.height, self.width, row7, font4)        #samplerate / 44100
        self.playingText5 = StaticText(self.height, self.width, row8, font4)        #bitdepth /16 Bit
        self.standbyText1 = StaticText(self.height, self.width, row3, fontClock)    #Clock /center=True
        self.standbyText2 = StaticText(self.height, self.width, row4, fontIP)	    #IP
        self.standbyText3 = StaticText(self.height, self.width, row5, fontDate)     #Date
	self.icon = {'play':'\u25B6', 'pause':'\u2389', 'stop':'\u25A0'}       	    #entypo icons
        self.playingIcon = self.icon['play']
        self.iconcountdown = 0
        self.text1Pos = (42, 2)        #Artist /
        self.text2Pos = (42, 27)       #Title
        self.text3Pos = (42, 4)        #clock
        self.text4Pos = (46, 54)       #IP
        self.text5Pos = (182, 54)      #Date
        self.text6Pos = (42, 52)       #format
        self.text7Pos = (156, 52)      #samplerate
        self.text8Pos = (217, 52)      #bitdepth
	self.alfaimage = Image.new('RGBA', image.size, (0, 0, 0, 0))

# "def __init__(self,...." is the "initialization" of the "NowPlayingScreen". 
#Here you need to define the variables, which "data-string" is which textposition, where each textposition is displayed in the display...

    def UpdatePlayingInfo(self, row1, row2, row6, row7, row8):
        self.playingText1 = ScrollText(self.height, self.width, row1, font)   #Artist/ center=True)
        self.playingText2 = ScrollText(self.height, self.width, row2, font3)  #Title
        self.playingText3 = StaticText(self.height, self.width, row6, font4)  #format
        self.playingText4 = StaticText(self.height, self.width, row7, font4)  #samplerate
        self.playingText5 = StaticText(self.height, self.width, row8, font4)  #bitdepth

    def UpdateStandbyInfo(self, row3, row4, row5):
        self.standbyText1 = StaticText(self.height, self.width, row3, fontClock) #Clock center=True)
        self.standbyText2 = StaticText(self.height, self.width, row4, fontIP)    #IP
        self.standbyText3 = StaticText(self.height, self.width, row5, fontDate)  #Date

#"def UpdateStandbyInfo" and "def UpdatePlayingInfo" collects the informations.
	
# "def DrawON(..." takes informations from above and creates a "picture" which then is transfered to your display	

    def DrawOn(self, image):
        if self.playingIcon != self.icon['stop']:
            self.playingText1.DrawOn(image, self.text1Pos) #Artist
            self.playingText2.DrawOn(image, self.text2Pos) #Title
            self.playingText3.DrawOn(image, self.text6Pos) #Format
            self.playingText4.DrawOn(image, self.text7Pos) #Samplerate
            self.playingText5.DrawOn(image, self.text8Pos) #Bitdepth
        if self.playingIcon == self.icon['stop']:
            self.standbyText1.DrawOn(image, self.text3Pos) #Clock
            self.standbyText2.DrawOn(image, self.text4Pos) #IP
            self.standbyText3.DrawOn(image, self.text5Pos) #Date
            
        if self.iconcountdown > 0:
            compositeimage = Image.composite(self.alfaimage, image.convert('RGBA'), self.alfaimage)
            image.paste(compositeimage.convert('RGB'), (0, 0))
            self.iconcountdown -= 1
            
    def SetPlayingIcon(self, state, time=0):
        if state in self.icon:
		self.playingIcon = self.icon[state]
        self.alfaimage.paste((0, 0, 0, 200), [0, 0, image.size[0], image.size[1]])                 #(0, 0, 0, 200) means Background (nowplayingscreen with artist, song etc.) is darkend. Change 200 to 0 -> Background is completely visible. 255 -> Bachground is not visible. scale = 0-255
        drawalfa = ImageDraw.Draw(self.alfaimage)
	iconwidth, iconheight = drawalfa.textsize(self.playingIcon, font=self.iconfont)            #entypo
        left = (self.width - iconwidth + 42) / 2						   #here is defined where the play/pause/stop icons are displayed. 
	drawalfa.text((left, 4), self.playingIcon, font=self.iconfont, fill=(255, 255, 255, 200))  #(255, 255, 255, 200) means Icon is nearly white. Change 200 to 0 -> icon is not visible. scale = 0-255
        self.iconcountdown = time

class MediaLibrarayInfo():
    def __init__(self, height, width, row1, row2, row3, row4, row5, row6, row7, row8, fontaw, font4): #this line references to oled.modal = NowPlayingScreen
        self.height = height
        self.width = width
        self.font4 = font4
        self.fontaw = fontaw
        self.LibraryInfoText1 = StaticText(self.height, self.width, row5, font4)   #Text for Artists
        self.LibraryInfoText2 = StaticText(self.height, self.width, row1, font4)   #Number of Artists
        self.LibraryInfoText3 = StaticText(self.height, self.width, row6, font4)   #Text for Albums
        self.LibraryInfoText4 = StaticText(self.height, self.width, row2, font4)   #Number of Albums
        self.LibraryInfoText5 = StaticText(self.height, self.width, row7, font4)   #Text for Songs
        self.LibraryInfoText6 = StaticText(self.height, self.width, row3, font4)   #Number of Songs
        self.LibraryInfoText7 = StaticText(self.height, self.width, row8, font4)   #Text for duration
        self.LibraryInfoText8 = StaticText(self.height, self.width, row4, font4)   #Summary of duration
        self.icon = {'info':'\F0CA'}
        self.mediaIcon = self.icon['info']
        self.iconcountdown = 0
        self.text1Pos = (140, 4)        					   #Number of Artists
        self.text2Pos = (140, 18)      						   #Number of Albums
        self.text3Pos = (140, 32)      						   #Number of Songs
        self.text4Pos = (140, 46)      						   #Summary of duration
        self.text5Pos = (42, 4)      						   #Text for Artists
        self.text6Pos = (42, 18)     						   #Text for Albums
        self.text7Pos = (42, 32)     						   #Text for Songs
        self.text8Pos = (42, 46)     						   #Text for duration
        self.alfaimage = Image.new('RGBA', image.size, (0, 0, 0, 0))

    def UpdateLibraryInfo(self, row1, row2, row3, row4, row5, row6, row7, row8):
        self.LibraryInfoText1 = StaticText(self.height, self.width, row5, font4)  #Text for Artists
        self.LibraryInfoText2 = StaticText(self.height, self.width, row1, font4)   #Number of Artists
        self.LibraryInfoText3 = StaticText(self.height, self.width, row6, font4)  #Text for Albums
        self.LibraryInfoText4 = StaticText(self.height, self.width, row2, font4)  #Number of Albums
        self.LibraryInfoText5 = StaticText(self.height, self.width, row7, font4)  #Text for Songs
        self.LibraryInfoText6 = StaticText(self.height, self.width, row3, font4)  #Number of Songs
        self.LibraryInfoText7 = StaticText(self.height, self.width, row8, font4)  #Text for duration
        self.LibraryInfoText8 = StaticText(self.height, self.width, row4, font4)  #Summary of duration

    def DrawOn(self, image):
        if self.mediaIcon == self.icon['info']:
            self.LibraryInfoText1.DrawOn(image, self.text5Pos) #Text for Artists
            self.LibraryInfoText2.DrawOn(image, self.text1Pos)  #Number of Artists
            self.LibraryInfoText3.DrawOn(image, self.text6Pos) #Text for Albums
            self.LibraryInfoText4.DrawOn(image, self.text2Pos) #Number of Albums
            self.LibraryInfoText5.DrawOn(image, self.text7Pos) #Text for Songs
            self.LibraryInfoText6.DrawOn(image, self.text3Pos) #Number of Songs
            self.LibraryInfoText7.DrawOn(image, self.text8Pos) #Text for duration
            self.LibraryInfoText8.DrawOn(image, self.text4Pos) #Number of duration
                    
        if self.iconcountdown > 0:
            compositeimage = Image.composite(self.alfaimage, image.convert('RGBA'), self.alfaimage)
            image.paste(compositeimage.convert('RGB'), (0, 0))
            self.iconcountdown -= 1
            
    def SetPlayingIcon(self, state, time=0):
        if state in self.icon:
            self.mediaIcon = self.icon[state]
        self.alfaimage.paste((0, 0, 0, 0), [0, 0, image.size[0], image.size[1]])
        drawalfa = ImageDraw.Draw(self.alfaimage)
        iconwidth, iconheight = drawalfa.textsize(self.playingIcon, font=self.fontaw)
        left = (self.width - iconwidth + 42) / 2 #here is defined where the play/pause/stop icons are displayed. 
        drawalfa.text((left, 4), self.playingIcon, font=self.fontaw, fill=(255, 255, 255, 96))
        self.iconcountdown = time

class VolumeScreen():
    def __init__(self, height, width, volume, font, font2):
        self.height = height
        self.width = width
        self.font = font
        self.font2 = font2
        self.volumeLabel = None
        self.labelPos = (40, 5)
        self.volumeNumber = None
        self.numberPos = (40, 25)
        self.barHeight = 22
        self.barWidth = 140
        self.volumeBar = Bar(self.height, self.width, self.barHeight, self.barWidth)
        self.barPos = (105, 27)
        self.volume = 0
        self.DisplayVolume(volume)

    def DisplayVolume(self, volume):
        self.volume = volume
        self.volumeNumber = StaticText(self.height, self.width, str(volume) + '%', self.font)
        self.volumeLabel = StaticText(self.height, self.width, 'Volume', self.font2)
        self.volumeBar.SetFilledPercentage(volume)

    def DrawOn(self, image):
        self.volumeLabel.DrawOn(image, self.labelPos)
        self.volumeNumber.DrawOn(image, self.numberPos)
        self.volumeBar.DrawOn(image, self.barPos)

class MenuScreen():
    def __init__(self, height, width, font2, menuList, selected=0, rows=3, label='', showIndex=False):
        self.height = height
        self.width = width
        self.font2 = font2
        self.selectedOption = selected
        self.menuLabel = StaticText(self.height, self.width, label, self.font2)
        if label == '':
            self.hasLabel = 0
        else:
            self.hasLabel = 1
        self.labelPos = (42, 2)                      #here is the position of the menu title
        self.menuYPos = 2 + 12 * self.hasLabel
        self.menurows = rows
        self.menuText = [None for i in range(self.menurows)]
        self.menuList = menuList
        self.totaloptions = len(menuList)
        self.onscreenoptions = min(self.menurows, self.totaloptions)
        self.firstrowindex = 0
        self.showIndex = showIndex
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
            if self.showIndex:
                width = 1 + len(str(self.totaloptions))      # more digits needs more space
                optionText = '{0:{width}d} {1}'.format(row + self.firstrowindex + 1, optionText, width=width)
            self.menuText[row] = StaticText(self.height, self.width, optionText, self.font2, fill=color, bgcolor=bgcolor)
        if self.totaloptions == 0:
            self.menuText[0] = StaticText(self.height, self.width, 'no items..', self.font2, fill="white", bgcolor="black")
            
    def NextOption(self):
        self.selectedOption = min(self.selectedOption + 1, self.totaloptions - 1)
        self.MenuUpdate()

    def PrevOption(self):
        self.selectedOption = max(self.selectedOption - 1, 0)
        self.MenuUpdate()

    def SelectedOption(self):
        return self.selectedOption

    def DrawOn(self, image):
        if self.hasLabel:
            self.menuLabel.DrawOn(image, self.labelPos)
        for row in range(self.onscreenoptions):
            self.menuText[row].DrawOn(image, (42, self.menuYPos + row*16))       #Here is the position of the list entrys from left set (42)
        if self.totaloptions == 0:
            self.menuText[0].DrawOn(image, (42, self.menuYPos))                  #Here is the position of the list entrys from left set (42)
	
def ButtonA_PushEvent(hold_time):
    global UPDATE_INTERVAL
    if hold_time < 3:
#shortpress functions below
        print('ButtonA short press event')
        if oled.state == STATE_PLAYER and oled.playState != 'stop':
            if oled.playState == 'play':
                volumioIO.emit('pause')
            else:
                volumioIO.emit('play')
        elif oled.state == STATE_PLAYER and oled.playState == 'stop':
              oled.stateTimeout = 10.0
              volumioIO.emit('browseLibrary',{'uri':'music-library'})
        elif oled.state == STATE_LIBRARY_INFO:
              oled.stateTimeout = 10.0
              volumioIO.emit('browseLibrary',{'uri':'music-library'})
        elif oled.state == STATE_PLAYLIST_MENU or oled.state == STATE_QUEUE_MENU or oled.state == STATE_LIBRARY_MENU:
              oled.modal.PrevOption()
#longpress functions below
    elif oled.state == STATE_PLAYER and oled.playState == 'stop':
	print('ButtonA long press event')
	oled.ShutdownFlag = True
        sleep(0.1)
        show_logo("shutdown.ppm", oled)
        sleep(5)
        oled.cleanup()                                              # put display into low power mode
        volumioIO.emit('shutdown')
        sleep(60)

def ButtonB_PushEvent(hold_time):
    global UPDATE_INTERVAL
    if hold_time < 2:
#shortpress functions below
        print('ButtonB short press event')
	if oled.state == STATE_PLAYER and oled.playState != 'stop':
            volumioIO.emit('stop')
        elif oled.state == STATE_PLAYER and oled.playState == 'stop':
              volumioIO.emit('listPlaylist')
              oled.stateTimeout = 10.0
              SetState(STATE_PLAYLIST_MENU)
        elif oled.state == STATE_LIBRARY_INFO:
              volumioIO.emit('listPlaylist')
              oled.stateTimeout = 10.0
              SetState(STATE_PLAYLIST_MENU)
        elif oled.state == STATE_PLAYLIST_MENU or oled.state == STATE_QUEUE_MENU or oled.state == STATE_LIBRARY_MENU:
              oled.modal.NextOption()

def ButtonC_PushEvent(hold_time):
    global UPDATE_INTERVAL
    if hold_time < 3:
#shortpress functions below
        print('ButtonC short press event')
        if oled.state == STATE_PLAYER and oled.playState != 'stop':
            volumioIO.emit('prev')
        elif oled.state == STATE_PLAYER and oled.playState == 'stop':
              oled.stateTimeout = 6.0
              SetState(STATE_QUEUE_MENU)
        elif oled.state == STATE_LIBRARY_INFO:
              oled.stateTimeout = 6.0
              SetState(STATE_QUEUE_MENU)
#Longpress functions below
    elif oled.state == STATE_PLAYER and oled.playState != 'stop':
        print('ButtonC long press event')
        if oled.repeatTag == False:
            volumioIO.emit('setRepeat', {"value":"true"})
            oled.repeatTag = True
        elif oled.randomTag == True:
            volumioIO.emit('setRepeat', {"value":"false"})
            oled.repeatTag = False

def ButtonD_PushEvent(hold_time):
    global UPDATE_INTERVAL
    b_obj = BytesIO()
    crl = pycurl.Curl()
    if hold_time < 3:
#shortpress functions below
        print('ButtonD short press event')
        if oled.state == STATE_PLAYER and oled.playState != 'stop':
            volumioIO.emit('next')
        elif oled.state == STATE_PLAYER and oled.playState == 'stop':
            SetState(STATE_LIBRARY_INFO)
	    oled.playState = 'info'
            crl.setopt(crl.URL, 'localhost:3000/api/v1/collectionstats')
            crl.setopt(crl.WRITEDATA, b_obj)
            crl.perform()
            crl.close()
            get_body = b_obj.getvalue()
            onPushCollectionStats(get_body)
            sleep(0.5) 
        elif oled.state == STATE_LIBRARY_INFO:
            SetState(STATE_PLAYER)
            onPushState(OPDsave)
        elif oled.state == STATE_PLAYLIST_MENU:
            LoadPlaylist(oled.playlistoptions[oled.modal.SelectedOption()])
        elif oled.state == STATE_LIBRARY_MENU:
            oled.stateTimeout = 10.0
            EnterLibraryItem(oled.modal.SelectedOption())
        elif oled.state == STATE_QUEUE_MENU:
            oled.playPosition = oled.modal.SelectedOption()
            emit_track = True         # return to player mode
#Longpress functions below
    elif oled.state == STATE_PLAYER and oled.playState != 'stop':
        print('ButtonD long press event')
        if oled.randomTag == False:
	    volumioIO.emit('setRandom', {"value":"true"})
            oled.randomTag = True
        elif oled.randomTag == True:
            volumioIO.emit('setRandom', {"value":"false"})
            oled.randomTag = False

def RightKnob_RotaryEvent(dir):
    global emit_track
    if oled.state == STATE_PLAYLIST_MENU or oled.state == STATE_LIBRARY_MENU:
        oled.stateTimeout = 10.0
        if dir == RotaryEncoder.LEFT:
            oled.modal.PrevOption()
        elif dir == RotaryEncoder.RIGHT:
            oled.modal.NextOption()
    elif oled.state == STATE_QUEUE_MENU:
        oled.stateTimeout = 6.0        
        if dir == RotaryEncoder.LEFT:
            oled.modal.PrevOption()
        elif dir == RotaryEncoder.RIGHT:
            oled.modal.NextOption()        
        oled.playPosition = oled.modal.SelectedOption()
        emit_track = True
    elif oled.state == STATE_PLAYER and oled.playState != 'stop':
        oled.stateTimeout = 10.0
        SetState(STATE_QUEUE_MENU)
    elif oled.state == STATE_PLAYER and oled.playState == 'stop':
        oled.stateTimeout = 10.0
        volumioIO.emit('browseLibrary',{'uri':'music-library'})
    elif oled.state == STATE_LIBRARY_INFO:
        oled.stateTimeout = 10.0
        volumioIO.emit('browseLibrary',{'uri':'music-library'})        

def RightKnob_PushEvent(hold_time):
    if hold_time < 1:
#shortpress fuctions below
        print ('RightKnob_PushEvent SHORT')
        if oled.state == STATE_PLAYER and oled.playState != 'stop':
            if oled.playState == 'play':
                volumioIO.emit('pause')
            else:
                volumioIO.emit('play')
        elif oled.state == STATE_PLAYER and oled.playState == 'stop':
            oled.stateTimeout = 10.0
            volumioIO.emit('browseLibrary',{'uri':'music-library'})
        elif oled.state == STATE_LIBRARY_INFO:
            oled.stateTimeout = 10.0
            volumioIO.emit('browseLibrary',{'uri':'music-library'})   
        elif oled.state == STATE_PLAYLIST_MENU:
            LoadPlaylist(oled.playlistoptions[oled.modal.SelectedOption()])
        elif oled.state == STATE_LIBRARY_MENU:
            oled.stateTimeout = 10.0
            EnterLibraryItem(oled.modal.SelectedOption())
        elif oled.state == STATE_QUEUE_MENU:
            oled.playPosition = oled.modal.SelectedOption()
            emit_track = True         # return to player mode
#longpress functions below
    else:
        print ('RightKnob_PushEvent')
        if oled.state == STATE_PLAYER and oled.playState != 'stop':        
            oled.stateTimeout = 10.0
            volumioIO.emit('browseLibrary',{'uri':'music-library'})
        elif oled.state == STATE_LIBRARY_INFO:        
            oled.stateTimeout = 10.0
            volumioIO.emit('browseLibrary',{'uri':'music-library'})


#Down below is the defenition for the physical buttons.
#Sample: RightKnob_Push = PushButton(27, max_time=1) -> GPIO 27 is used
#Which Button is conected to which GPIO? (regarding to wiring diagram Maschine2501/Volumio-OledUI)
# Button A: GPIO 4
# Button B: GPIO 17
# Button C: GPIO 5
# Button D: GPIO 6
# Button right-Rotary: GPIO 27

ButtonA_Push = PushButton(4, max_time=3)
ButtonA_Push.setCallback(ButtonA_PushEvent)
ButtonB_Push = PushButton(17, max_time=1)
ButtonB_Push.setCallback(ButtonB_PushEvent)
ButtonC_Push = PushButton(5, max_time=3)
ButtonC_Push.setCallback(ButtonC_PushEvent)
ButtonD_Push = PushButton(6, max_time=3)
ButtonD_Push.setCallback(ButtonD_PushEvent)

RightKnob_Push = PushButton(27, max_time=1)
RightKnob_Push.setCallback(RightKnob_PushEvent)
RightKnob_Rotation = RotaryEncoder(22, 23, pulses_per_cycle=4)
RightKnob_Rotation.setCallback(RightKnob_RotaryEvent)
#IR receiver is connected to port 13

show_logo("volumio_logo.ppm", oled)
sleep(2)
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
#volumioIO.on('pushcollectionstats', onPushCollectionStats)
volumioIO.on('pushListPlaylist', onPushListPlaylist)
volumioIO.on('pushQueue', onPushQueue)
volumioIO.on('pushBrowseSources', onPushBrowseSources)
volumioIO.on('pushBrowseLibrary', onLibraryBrowse)

# get list of Playlists and initial state
volumioIO.emit('listPlaylist')
volumioIO.emit('getState')
volumioIO.emit('getQueue')
#volumioIO.emit('collectionstats')

#volumioIO.emit('getBrowseSources')
sleep(0.1)

#def timeupdate()
#    start_time = datetime.datetime.now()

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
while True:
    if emit_volume:
        emit_volume = False
        print("volume: " + str(oled.volume))
        volumioIO.emit('volume', oled.volume)
    if emit_track and oled.stateTimeout < 4.5:
        emit_track = False
        try:
            print('Track selected: ' + str(oled.playPosition+1) + '/' + str(len(oled.queue)) + ' ' + oled.queue[oled.playPosition].encode('ascii', 'ignore'))
        except IndexError:
            pass
        volumioIO.emit('play', {'value':oled.playPosition})
    sleep(0.1)

#this is the loop to get artist/song when changing sources (loops three times)
    
    if oled.state == STATE_PLAYER and InfoTag <= 3 and newStatus != 'stop':
        oled.modal.UpdatePlayingInfo(oled.activeArtist, oled.activeSong, oled.activeFormat, oled.activeSamplerate, oled.activeBitdepth)
        InfoTag += 1
        sleep(1.5)

#this is the loop to push the actual time every 0.1sec to the "Standby-Screen"

    if oled.state == STATE_PLAYER and newStatus == 'stop' and oled.ShutdownFlag == False:
    	InfoTag = 0  #resets the InfoTag helper from artist/song update loop
        oled.time = strftime("%H:%M:%S")
        oled.modal.UpdateStandbyInfo(oled.time, oled.IP, oled.date)

#if playback is paused, here is defined when the Player goes back to "Standby"/Stop		

    if oled.state == STATE_PLAYER and newStatus == 'pause' and varcanc == True:
       secvar = int(round(time()))
       varcanc = False
    elif oled.state == STATE_PLAYER and newStatus == 'pause' and int(round(time())) - secvar > 15:
         varcanc = True
         volumioIO.emit('stop')
sleep(0.1)

#!/usr/bin/python

from __future__ import unicode_literals

"""
Volumio User Interface: OLED 256x64 + 2x rotary encoder with pushbutton
DiehardSK 2019
Inspired by Volumio HandsOn script
"""

import requests
import os
import sys
import json
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 

from time import time, sleep
from threading import Thread
from socketIO_client import SocketIO
from datetime import datetime

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

STATE_NONE = -1
STATE_PLAYER = 0
STATE_PLAYLIST_MENU = 1
STATE_QUEUE_MENU = 2
STATE_VOLUME = 3
STATE_SHOW_INFO = 4
STATE_LIBRARY_MENU = 5

UPDATE_INTERVAL = 0.034
PIXEL_SHIFT_TIME = 120    #time between picture position shifts in sec.

interface = spi(device=0, port=0)
oled = ssd1322(interface, rotate=2) 
#without rotate display is 0 degrees, with rotate=2 its 180 degrees

oled.WIDTH = 256
oled.HEIGHT = 64
oled.state = STATE_NONE
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
oled.volumeControlDisabled = False
oled.volume = 100
now = datetime.now() # current date and time
oled.time = now.strftime("%H:%M:%S") #resolves time as HH:MM:SS eg. 14:33:15
oled.date = now.strftime("%d/%m/%y") #resolves time as dd.mm.yyyy eg. 17.04.2020
oled.IP = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0] #resolves IP from Ethernet Adapator
emit_volume = False
emit_track = False

image = Image.new('RGB', (oled.WIDTH + 4, oled.HEIGHT + 4))  #enlarged for pixelshift
oled.clear()

font = load_font('Roboto-Regular.ttf', 24)
font2 = load_font('PixelOperator.ttf', 15)
hugefontaw = load_font('fa-solid-900.ttf', oled.HEIGHT - 4)
fontClock = load_font('digi.ttf', 50)
fontDate = load_font('digi.ttf', 14)  
fontIP = load_font('digi.ttf', 14)  
#above are the "imports" for the fonts. 
#After the name of the font comes a number, this defines the Size (height) of the letters. 
#Just put .ttf file in the 'Volumio-OledUI/fonts' directory and make an import like above. 

def display_update_service():
    pixshift = [2, 2]
    lastshift = prevTime = time()
    while UPDATE_INTERVAL > 0:
        dt = time() - prevTime
        prevTime = time()
        if prevTime-lastshift > PIXEL_SHIFT_TIME: #it's time for pixel shift
            lastshift = prevTime
            if pixshift[0] == 4 and pixshift[1] < 4:
                pixshift[1] += 1
            elif pixshift[1] == 0 and pixshift[0] < 4:
                pixshift[0] += 1
            elif pixshift[0] == 0 and pixshift[1] > 0:
                pixshift[1] -= 1
            else:
                pixshift[0] -= 1
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
        oled.modal = NowPlayingScreen(oled.HEIGHT, oled.WIDTH, oled.activeArtist, oled.activeSong, oled.time, oled.IP, oled.date, font, hugefontaw, fontClock, fontDate, fontIP)
        oled.modal.SetPlayingIcon(oled.playState, 0)
    elif oled.state == STATE_VOLUME:
        oled.modal = VolumeScreen(oled.HEIGHT, oled.WIDTH, oled.volume, font, font2)
    elif oled.state == STATE_PLAYLIST_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.playlistoptions, rows=3, label='------ Select Playlist ------')
    elif oled.state == STATE_QUEUE_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.queue, rows=4, selected=oled.playPosition, showIndex=True)
    elif oled.state == STATE_LIBRARY_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.libraryNames, rows=3, label='------ Music Library ------')

def LoadPlaylist(playlistname):
    print ("loading playlist: " + playlistname.encode('ascii', 'ignore'))
    oled.playPosition = 0
    volumioIO.emit('playPlaylist', {'name':playlistname})
    SetState(STATE_PLAYER)

def onPushState(data):
    #print(data)
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
        
    if 'position' in data:                      # current position in queue
        oled.playPosition = data['position']    # didn't work well with volumio ver. < 2.5
        
    if 'status' in data:
        newStatus = data['status']
        
    if oled.state != STATE_VOLUME:            #get volume on startup and remote control
        try:                                  #it is either number or unicode text
            oled.volume = int(data['volume'])
        except (KeyError, ValueError):
            pass
    
    if 'disableVolumeControl' in data:
        oled.volumeControlDisabled = data['disableVolumeControl']

    print(newSong.encode('ascii', 'ignore'))
    if (newSong != oled.activeSong):    # new song
        oled.activeSong = newSong
        oled.activeArtist = newArtist
        if oled.state == STATE_PLAYER and newStatus != 'stop':
            oled.modal.UpdatePlayingInfo(newArtist, newSong)
        if oled.state == STATE_PLAYER and newStatus == 'stop':   #this is the "Standby-Screen"
            oled.modal.UpdateStandbyInfo(oled.time, oled.IP, oled.date)     #here is defined which "data" should be displayed in the class

    if newStatus != oled.playState:
        oled.playState = newStatus
        if oled.state == STATE_PLAYER:
            if oled.playState == 'play':
                iconTime = 35
            else:
                iconTime = 80
            oled.modal.SetPlayingIcon(oled.playState, iconTime)
    

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

class NowPlayingScreen():
    def __init__(self, height, width, row1, row2, row3, row4, row5, font, fontaw, fontClock, fontDate, fontIP): #this line references to oled.modal = NowPlayingScreen
        self.height = height
        self.width = width
        self.font = font
        self.fontaw = fontaw
        self.fontClock = fontClock
	self.fontDate = fontDate
	self.fontIP = fontIP
        self.playingText1 = StaticText(self.height, self.width, row1, font, center=True)
        self.playingText2 = ScrollText(self.height, self.width, row2, font)
	self.standbyText3 = StaticText(self.height, self.width, row3, fontClock, center=True)
	self.standbyText4 = StaticText(self.height, self.width, row4, fontIP)
	self.standbyText5 = StaticText(self.height, self.width, row5, fontDate)
	self.icon = {'play':'\uf04b', 'pause':'\uf04c', 'stop':'\uf04d'}
        self.playingIcon = self.icon['play']
        self.iconcountdown = 0
        self.text1Pos = (3, 6)
        self.text2Pos = (3, 37)
	self.text3Pos = (0, 0)
	self.text4Pos = (2, 48)
	self.text5Pos = (192, 48)
        self.alfaimage = Image.new('RGBA', image.size, (0, 0, 0, 0))

    def UpdatePlayingInfo(self, row1, row2):
        self.playingText1 = StaticText(self.height, self.width, row1, font, center=True)
        self.playingText2 = ScrollText(self.height, self.width, row2, font)
	
    def UpdateStandbyInfo(self, row3, row4, row5):
        self.standbyText3 = StaticText(self.height, self.width, row3, fontClock, center=True)
        self.standbyText4 = StaticText(self.height, self.width, row4, fontIP)
	self.standbyText5 = StaticText(self.height, self.width, row5, fontDate)	
	
    def DrawOn(self, image):
        if self.playingIcon != self.icon['stop']:
            self.playingText1.DrawOn(image, self.text1Pos)
            self.playingText2.DrawOn(image, self.text2Pos)
        if self.playingIcon == self.icon['stop']:
            self.standbyText3.DrawOn(image, self.text3Pos)
            self.standbyText4.DrawOn(image, self.text4Pos)
	    self.standbyText5.DrawOn(image, self.text5Pos)
           
            
        if self.iconcountdown > 0:
            compositeimage = Image.composite(self.alfaimage, image.convert('RGBA'), self.alfaimage)
            image.paste(compositeimage.convert('RGB'), (0, 0))
            self.iconcountdown -= 1
            
    def SetPlayingIcon(self, state, time=0):
        if state in self.icon:
            self.playingIcon = self.icon[state]
        self.alfaimage.paste((0, 0, 0, 0), [0, 0, image.size[0], image.size[1]])
        drawalfa = ImageDraw.Draw(self.alfaimage)
        iconwidth, iconheight = drawalfa.textsize(self.playingIcon, font=self.fontaw)
        left = (self.width - iconwidth) / 2
        drawalfa.text((left, 4), self.playingIcon, font=self.fontaw, fill=(255, 255, 255, 96))
        self.iconcountdown = time

class VolumeScreen():
    def __init__(self, height, width, volume, font, font2):
        self.height = height
        self.width = width
        self.font = font
        self.font2 = font2
        self.volumeLabel = None
        self.labelPos = (10, 5)
        self.volumeNumber = None
        self.numberPos = (10, 25)
        self.barHeight = 22
        self.barWidth = 140
        self.volumeBar = Bar(self.height, self.width, self.barHeight, self.barWidth)
        self.barPos = (85, 27)
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
        self.menuLabel = StaticText(self.height, self.width, label, self.font2, center=True)
        if label == '':
            self.hasLabel = 0
        else:
            self.hasLabel = 1
        self.labelPos = (1, 3)
        self.menuYPos = 3 + 16 * self.hasLabel
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
            self.menuText[row].DrawOn(image, (5, self.menuYPos + row*16))
        if self.totaloptions == 0:
            self.menuText[0].DrawOn(image, (15, self.menuYPos))


def LeftKnob_RotaryEvent(dir):
    global emit_volume
    if not oled.volumeControlDisabled and oled.state != STATE_PLAYLIST_MENU:
        if dir == RotaryEncoder.LEFT:
            oled.volume -= VOLUME_DT
            oled.volume = max(oled.volume, 0)
        elif dir == RotaryEncoder.RIGHT:
            oled.volume += VOLUME_DT
            oled.volume = min(oled.volume, 100)
        oled.stateTimeout = 2.0
        if oled.state != STATE_VOLUME:
            SetState(STATE_VOLUME)
        else:
            oled.modal.DisplayVolume(oled.volume)
        emit_volume = True

def LeftKnob_PushEvent(hold_time):
    global UPDATE_INTERVAL
    if hold_time < 3:
        print ('LeftKnob_PushEvent SHORT')
        if oled.state == STATE_PLAYER:
            if oled.playState == 'play':
                volumioIO.emit('stop')
            else:
                volumioIO.emit('play')
        if oled.state == STATE_PLAYLIST_MENU:
            SetState(STATE_PLAYER)
        if oled.state == STATE_LIBRARY_MENU:
            LibraryReturn()
    else:
        print ('LeftKnob_PushEvent LONG -> trying to shutdown')
        UPDATE_INTERVAL = 10 #stop updating screen
        sleep(0.1)
        show_logo("shutdown.ppm", oled)
        try:
            with open('oledconfig.json', 'w') as f:   #save current track number
                json.dump({"track": oled.playPosition}, f)
        except IOError:
            print ('Cannot save config file to current working directory')
        sleep(1.5)
        oled.cleanup()            # put display into low power mode
        volumioIO.emit('shutdown')
        sleep(60)

def RightKnob_RotaryEvent(dir):
    global emit_track
    if oled.state == STATE_PLAYLIST_MENU or oled.state == STATE_LIBRARY_MENU:
        oled.stateTimeout = 20.0
        if dir == RotaryEncoder.LEFT:
            oled.modal.PrevOption()
        elif dir == RotaryEncoder.RIGHT:
            oled.modal.NextOption()

    else:
        oled.stateTimeout = 6.0
        if oled.state != STATE_QUEUE_MENU:
            SetState(STATE_QUEUE_MENU)
        if dir == RotaryEncoder.LEFT:
            oled.modal.PrevOption()
        elif dir == RotaryEncoder.RIGHT:
            oled.modal.NextOption()
        oled.playPosition = oled.modal.SelectedOption()
        emit_track = True



def RightKnob_PushEvent(hold_time):
    if hold_time < 1:
        print ('RightKnob_PushEvent SHORT')
        if oled.state == STATE_QUEUE_MENU:
            oled.stateTimeout = 0          # return to player mode
        elif oled.state != STATE_PLAYLIST_MENU and oled.state != STATE_LIBRARY_MENU:
            volumioIO.emit('listPlaylist')
            oled.stateTimeout = 20.0
            SetState(STATE_PLAYLIST_MENU)
            print ('Entering playlist menu')
        else:
            if oled.state == STATE_PLAYLIST_MENU:
                LoadPlaylist(oled.playlistoptions[oled.modal.SelectedOption()])
            if oled.state == STATE_LIBRARY_MENU:
                oled.stateTimeout = 20.0
                EnterLibraryItem(oled.modal.SelectedOption())
    else:
        print ('RightKnob_PushEvent LONG -> Music library browse')
        oled.stateTimeout = 20.0
        volumioIO.emit('browseLibrary',{'uri':'music-library'})

LeftKnob_Push = PushButton(3, max_time=3)
LeftKnob_Push.setCallback(LeftKnob_PushEvent)
LeftKnob_Rotation = RotaryEncoder(5, 6, pulses_per_cycle=4)
LeftKnob_Rotation.setCallback(LeftKnob_RotaryEvent)

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
volumioIO.on('pushListPlaylist', onPushListPlaylist)
volumioIO.on('pushQueue', onPushQueue)
volumioIO.on('pushBrowseSources', onPushBrowseSources)
volumioIO.on('pushBrowseLibrary', onLibraryBrowse)

# get list of Playlists and initial state
volumioIO.emit('listPlaylist')
volumioIO.emit('getState')
volumioIO.emit('getQueue')
#volumioIO.emit('getBrowseSources')
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

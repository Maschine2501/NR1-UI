#!/usr/bin/python3

#___________________________________________________________________
#config for boot- and shutdown-logo
oledBootLogo = "StartScreen1322.bmp"
oledShutdownLogo = "ShutdownScreen1322.bmp"

#___________________________________________________________________
#config for Clock/Standby:
oledtext03 = 40, 5       #clock
oledtext04 = 0, 52      #IP
oledtext05 = 176, 52     #Date
oledtext09 = 244, 51   #LibraryInfoIcon

#_______'Spectrum-Center'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen2text01 = 0, -4        #Artist
Screen2text02 = 0, 16       #Title
Screen2text06 = 0, 41       #format
Screen2text07 = 159, 41     #samplerate
Screen2text08 = 220, 41     #bitdepth
Screen2text28 = 25, 41       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen2ActualPlaytimeText = 1, 54
Screen2DurationText = 210, 54

#config for Progress-Bar
Screen2barwidth = 152
Screen2barLineBorder = 'white'
Screen2barLineFill = 'black'
Screen2barLineX = 50
Screen2barLineThick1 = 61     #difference between both = thickness 
Screen2barLineThick2 = 61     # 59 and 59 = 1 Pixel thick
Screen2barBorder = 'white'
Screen2barFill = 'black'
Screen2barX = 50
Screen2barThick1 = 59         #difference between both = thickness 
Screen2barThick2 = 63         # 56 and 62 = 6 Pixel thick
Screen2barNibbleWidth = 2

#config for Spectrum
Screen2specDistance = 62
Screen2specBorder = (80, 80, 80)
Screen2specFill = (80, 80, 80)
Screen2specWide1 = 2
Screen2specWide2 = 0
Screen2specYposTag = 61
Screen2specYposNoTag = 61

#config for Spectrum2 NoProgress
Screen22specDistance = 0
Screen22specBorder = (130, 130, 130)
Screen22specFill = (130, 130, 130)
Screen22specWide1 = 4
Screen22specWide2 = 0
Screen22specYposTag = 63
Screen22specYposNoTag = 63

#_______'No-Spectrum'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen4text01 = 0, -4        #Artist
Screen4text02 = 0, 16       #Title
Screen4text06 = 132, 41       #format
Screen4text07 = 163, 41     #samplerate
Screen4text08 = 220, 41     #bitdepth
Screen4text008 = 200, 41    #Webradio Bitrate
Screen4Text0008 = 130, 41    #Weebradio Tracktype
Screen4text28 = 120, 40       #Play/Pause Indicator
Screen4text29 = 15, 41       #Volume Text
Screen4text30 = 0, 39        #VolumeOn Symbol
Screen4text31 = 0, 39        #VolumeOff Speaker symbol
Screen4text32 = 54, 38        #VolumeOff Forbidden Symbol
Screen4text33 = 88, 40           #repeat symbol
Screen4text34 = 81, 41           #repeat once one
Screen4text35 = 104, 40           #shuffle

#"No Progress"
Screen4text60 = 120, 50       #Play/Pause Indicator
Screen4Text61 = 130, 51    #Weebradio Tracktype
Screen4text62 = 200, 51    #Webradio Bitrate
Screen4text63 = 88, 50           #repeat symbol
Screen4text64 = 81, 51           #repeat once one
Screen4text65 = 104, 50           #shuffle
Screen4text66 = 0, 49        #VolumeOn Symbol
Screen4text67 = 0, 49        #VolumeOff Speaker symbol
Screen4text68 = 15, 51       #Volume Text

#configuration of the duration and playtime (textbox-) positions
Screen4ActualPlaytimeText = 1, 54
Screen4DurationText = 210, 54

#config for Progress-Bar
Screen4barwidth = 152
Screen4barLineBorder = 'white'
Screen4barLineFill = 'black'
Screen4barLineX = 50
Screen4barLineThick1 = 59     #difference between both = thickness 
Screen4barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen4barBorder = 'white'
Screen4barFill = 'black'
Screen4barX = 50
Screen4barThick1 = 57         #difference between both = thickness 
Screen4barThick2 = 61         # 56 and 62 = 6 Pixel thick
Screen4barNibbleWidth =2

#_______'Modern'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen5text01 = 0, 46        #Artist + Song
Screen5text06 = 74, 39       #format
Screen5text07 = 106, 39     #samplerate
Screen5text08 = 156, 39     #bitdepth
Screen5text28 = 96, 37       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen5ActualPlaytimeText = 1, 0
Screen5DurationText = 220, 0

#config for Progress-Bar
Screen5barwidth = 256
Screen5barLineBorder = 'white'
Screen5barLineFill = 'white'
Screen5barLineX = 0
Screen5barLineThick1 = 32     #difference between both = thickness 
Screen5barLineThick2 = 32     # 59 and 59 = 1 Pixel thick
Screen5barBorder = 'white'
Screen5barFill = 'black'
Screen5barX = 0
Screen5barThick1 = 30         #difference between both = thickness 
Screen5barThick2 = 34         # 56 and 62 = 6 Pixel thick
Screen5barNibbleWidth = 2

#config for Spectrum
Screen5specDistance = 1
Screen5specBorder = (130, 130, 130)
Screen5specFill = (130, 130, 130)
Screen5specWide1 = 4
Screen5specWide2 = 1
Screen5specYposTag = 28
Screen5specYposNoTag = 28

#config for Spectrum2 NoProgress
Screen55specDistance = 0
Screen55specBorder = (130, 130, 130)
Screen55specFill = (130, 130, 130)
Screen55specWide1 = 4
Screen55specWide2 = 1
Screen55specYposTag = 33
Screen55specYposNoTag = 33

#config for leftVU
Screen5leftVUDistance = 0
Screen5leftVUBorder = (80, 80, 80)
Screen5leftVUFill = (80, 80, 80)
Screen5leftVUWide1 = 2
Screen5leftVUWide2 = 0
Screen5leftVUYpos1 = 39
Screen5leftVUYpos2 = 45

#config for leftVU NoProgress
Screen55leftVUDistance = 0
Screen55leftVUBorder = (80, 80, 80)
Screen55leftVUFill = (80, 80, 80)
Screen55leftVUWide1 = 2
Screen55leftVUWide2 = 0
Screen55leftVUYpos1 = 39
Screen55leftVUYpos2 = 45

#config for rightVU
Screen5rightVUDistance = 255
Screen5rightVUBorder = (80, 80, 80)
Screen5rightVUFill = (80, 80, 80)
Screen5rightVUWide1 = 2
Screen5rightVUWide2 = 0
Screen5rightVUYpos1 = 39
Screen5rightVUYpos2 = 45

#config for rightVU NoProgress
Screen55rightVUDistance = 255
Screen55rightVUBorder = (80, 80, 80)
Screen55rightVUFill = (80, 80, 80)
Screen55rightVUWide1 = 2
Screen55rightVUWide2 = 0
Screen55rightVUYpos1 = 39
Screen55rightVUYpos2 = 45

#_______'VU-Meter-2'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen7text01 = 0, -2        #Artist +Titel
Screen7text06 = 86, 14       #format
#Screen7text07 = 109, 14     #samplerate
#Screen7text08 = 156, 14     #bitdepth
Screen7text28 = 74, 13       #Play/Pause Indicator

#config for VU-Meter "Hand"/"Pointer"
Screen7leftVUcoordinates = [(63, 160, 5, 59), (63, 160, 8, 57), (63, 160, 11, 55), (63, 160, 14, 53), (63, 160, 17, 52), (63, 160, 20, 51), (63, 160, 23, 49), (63, 160, 26, 47), (63, 160, 29, 46), (63, 160, 32, 45), (63, 160, 35, 44), (63, 160, 38, 43), (63, 160, 41, 43), (63, 160, 44, 42), (63, 160, 47, 42), (63, 160, 50, 41), (63, 160, 53, 40), (63, 160, 56, 40), (63, 160, 59, 40), (63, 160, 62, 40), (63, 160, 65, 41), (63, 160, 68, 41), (63, 160, 71, 41), (63, 160, 74, 41), (63, 160, 77, 42), (63, 160, 80, 42), (63, 160, 83, 43), (63, 160, 86, 43), (63, 160, 89, 44), (63, 160, 92, 44), (63, 160, 95, 45), (63, 160, 98, 45), (63, 160, 101, 46)]              
Screen7rightVUcoordinates = [(191, 160, 133, 59), (191, 160, 136, 57), (191, 160, 139, 55), (191, 160, 142, 53), (191, 160, 145, 52), (191, 160, 148, 51), (191, 160, 151, 49), (191, 160, 154, 47), (191, 160, 157, 46), (191, 160, 160, 45), (191, 160, 163, 44), (191, 160, 166, 43), (191, 160, 169, 43), (191, 160, 172, 42), (191, 160, 175, 42), (191, 160, 178, 41), (191, 160, 181, 40), (191, 160, 184, 40), (191, 160, 187, 40), (191, 160, 190, 40), (191, 160, 193, 41), (191, 160, 196, 41), (191, 160, 199, 41), (191, 160, 202, 41), (191, 160, 205, 42), (191, 160, 208, 42), (191, 160, 211, 43), (191, 160, 214, 43), (191, 160, 217, 44), (191, 160, 220, 44), (191, 160, 223, 45), (191, 160, 226, 45), (191, 160, 229, 45)]

#configuration of the duration and playtime (textbox-) positions
Screen7ActualPlaytimeText = 1, 14
Screen7DurationText = 220, 14

#config for Progress-Bar
Screen7barwidth = 256
Screen7barLineBorder = 'white'
Screen7barLineFill = 'white'
Screen7barLineX = 0
Screen7barLineThick1 = 26     #difference between both = thickness 
Screen7barLineThick2 = 26     # 59 and 59 = 1 Pixel thick
Screen7barBorder = 'white'
Screen7barFill = 'black'
Screen7barX = 0
Screen7barThick1 = 24         #difference between both = thickness 
Screen7barThick2 = 28         # 56 and 62 = 6 Pixel thick
Screen7barNibbleWidth = 2

#_______'VU-Meter-Bar'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen8text01 = 60, -4        #Artist
Screen8text02 = 60, 11       #Title
Screen8text11 = 60, -4        #Artist
Screen8text22 = 60, 14       #Title
Screen8text06 = 0, 2       #format
Screen8text07 = 10, 16     #samplerate
Screen8text08 = 22, 2     #bitdepth
Screen8text28 = 1, 14       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen8ActualPlaytimeText = 0, 29
Screen8DurationText = 219, 29

#config for Progress-Bar
Screen8barwidth = 172
Screen8barLineBorder = 'white'
Screen8barLineFill = 'white'
Screen8barLineX = 40
Screen8barLineThick1 = 34     #difference between both = thickness 
Screen8barLineThick2 = 34     # 59 and 59 = 1 Pixel thick
Screen8barBorder = 'white'
Screen8barFill = 'black'
Screen8barX = 40
Screen8barThick1 = 32         #difference between both = thickness 
Screen8barThick2 = 36         # 56 and 62 = 6 Pixel thick
Screen8barNibbleWidth = 2

#config for leftVU
Screen8leftVUDistance = 22  #startpoint oft the VU from the left side of the screen
Screen8leftVUWide1 = 7      #spacing/width of each value -> 32max value from cava * 7 = 224pixels width
Screen8leftVUWide2 = 4      #width of each Value from cava ->   Value <= Screen8leftVUWide1 -> results in Spaces between / Value >= Screen8leftVUWide1 -> continous Bar 
Screen8leftVUYpos1 = 40
Screen8leftVUYpos2 = 46

#config for rightVU
Screen8rightVUDistance = 22
Screen8rightVUWide1 = 7
Screen8rightVUWide2 = 4
Screen8rightVUYpos1 = 56
Screen8rightVUYpos2 = 62

#config for "Peak-Hold"
Screen8fallingTime = 0.3      # lower = faster drop / higher = longer hold time
Screen8PeakWidth = 2          # wdith of the peak indicator in pixels

#config for gradient color of the VU
Screen8specGradstart = 80
Screen8specGradstop = 210
Screen8specGradSamples = 32

#___________________________________________________________________
#Config TextPositions Media-Library-Info-Screen:
oledtext10 = 138, 2      #Number of Artists
oledtext11 = 138, 15     #Number of Albums
oledtext12 = 138, 28     #Number of Songs
oledtext13 = 138, 41     #Summary of duration
oledtext14 = 14, 2       #Text for Artists
oledtext15 = 14, 15      #Text for Albums
oledtext16 = 14, 28      #Text for Songs
oledtext17 = 14, 41      #Text for duration
oledtext18 = 134, 52     #Menu-Label Icon
oledtext19 = 226, 54     #LibraryInfoIcon
oledtext20 = 0, 2        #icon for Artists
oledtext21 = 0, 15       #icon for Albums
oledtext22 = 0, 28       #icon for Songs
oledtext23 = 0, 41       #icon for duration

#___________________________________________________________________
#configuration Menu-Screen:
oledListEntrys = 4
oledEmptyListText = 'no items..'
oledEmptyListTextPosition = 0, 4
oledListTextPosX = 2
oledListTextPosY = 16    #height of each Entry (4x16 = 64)

#___________________________________________________________________
#config for Text:
oledArt = 'Artist :'  #sets the Artists-text for the MediaLibrarayInfo
oledAlb = 'Albums:'        #sets the Albums-text for the MediaLibrarayInfo
oledSon = 'Songs :'        #sets the Songs-text for the MediaLibrarayInfo
oledPla = 'Playtime :'     #sets the Playtime-text for the MediaLibrarayInfo

#___________________________________________________________________
#config for Icons:
#entypo
oledlibraryInfo = '\U0001F4D6'
oledlibraryReturn = '\u2302'
oledArtistIcon = '\uF0F3'
oledAlbumIcon = '\uF2BB'
oledSongIcon = '\U0000F001'
oledPlaytimeIcon = '\U0000F1DA'
oledplayIcon = '\u25B6'
oledpauseIcon = '\u2389'

#entypo
oledrepeat = '\U0001F501'
oledshuffle = '\U0001F500'
#fa
oledblockSymbol = '\uF05E'
oledvolumeoff = '\uF026'
oledvolumeon = '\uF028'

#____________________________________________________________________
#config for Scrolling Text
ArtistScrollSpeed = 1
ArtistEndScrollMargin = 2
SongScrollSpeed = 1
SongEndScrollMargin = 2

#Menu
oledMenuHighlightColor = (255, 255, 255)
oledMenuHighlightBackGround = (0, 0, 0)
oledMenuNotSelectedColor = (80, 80, 80)
oledMenuNotSelectedBackground = (0, 0, 0)

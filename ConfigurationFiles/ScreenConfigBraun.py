#!/usr/bin/python3

#___________________________________________________________________
#config for boot- and shutdown-logo
oledBootLogo = "volumio_logo.ppm"
oledShutdownLogo = "shutdown.ppm"

#___________________________________________________________________ok
#config for Clock/Standby:
oledtext03 = 59, 4       #clock
oledtext04 = 34, 52      #IP
oledtext05 = 169, 52     #Date
oledtext09 = 236, 51     #LibraryInfoIcon

#_______'Spectrum-Center'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen2text01 = 35, -4        #Artist
Screen2text02 = 35, 16       #Title
Screen2text06 = 35, 41       #format
Screen2text07 = 151, 41     #samplerate
Screen2text08 = 212, 41     #bitdepth
Screen2text28 = 59, 41       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen2ActualPlaytimeText = 35, 54
Screen2DurationText = 205, 54

#config for Progress-Bar
Screen2barwidth = 128
Screen2barLineBorder = 'white'
Screen2barLineFill = 'black'
Screen2barLineX = 76
Screen2barLineThick1 = 61     #difference between both = thickness 
Screen2barLineThick2 = 61     # 59 and 59 = 1 Pixel thick
Screen2barBorder = 'white'
Screen2barFill = 'black'
Screen2barX = 76
Screen2barThick1 = 59         #difference between both = thickness 
Screen2barThick2 = 63         # 56 and 62 = 6 Pixel thick
Screen2barNibbleWidth = 2

#config for Spectrum
Screen2specDistance = 76
Screen2specBorder = (80, 80, 80)
Screen2specFill = (80, 80, 80)
Screen2specWide1 = 2
Screen2specWide2 = 0
Screen2specYposTag = 61
Screen2specYposNoTag = 61

#config for Spectrum2 NoProgress
Screen22specDistance = 34
Screen22specBorder = (130, 130, 130)
Screen22specFill = (130, 130, 130)
Screen22specWide1 = 3
Screen22specWide2 = 0
Screen22specYposTag = 63
Screen22specYposNoTag = 63

#_______'No-Spectrum'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen4text01 = 34, 2        #Artist
Screen4text02 = 34, 22       #Title
Screen4text06 = 45, 41       #format
Screen4text07 = 80, 41     #samplerate
Screen4text08 = 210, 41     #bitdepth
Screen4text28 = 35, 41       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen4ActualPlaytimeText = 35, 54
Screen4DurationText = 205, 54

#config for Progress-Bar
Screen4barwidth = 128
Screen4barLineBorder = 'white'
Screen4barLineFill = 'black'
Screen4barLineX = 76
Screen4barLineThick1 = 59     #difference between both = thickness 
Screen4barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen4barBorder = 'white'
Screen4barFill = 'black'
Screen4barX = 76
Screen4barThick1 = 57         #difference between both = thickness 
Screen4barThick2 = 61         # 56 and 62 = 6 Pixel thick
Screen4barNibbleWidth =2

#_______'Modern'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen5text01 = 35, 51        #Artist
Screen5text02 = 35, 51       #Title
Screen5text012 = 35, 0       #Artist
Screen5text022 = 35, 19       #Title
Screen5text06 = 91, 39       #format
Screen5text07 = 123, 39     #samplerate
Screen5text08 = 163, 39     #bitdepth
Screen5text28 = 113, 37       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen5ActualPlaytimeText = 35, 0
Screen5DurationText = 207, 0

#config for Progress-Bar
Screen5barwidth = 208
Screen5barLineBorder = 'white'
Screen5barLineFill = 'white'
Screen5barLineX = 34
Screen5barLineThick1 = 32     #difference between both = thickness 
Screen5barLineThick2 = 32     # 59 and 59 = 1 Pixel thick
Screen5barBorder = 'white'
Screen5barFill = 'black'
Screen5barX = 34
Screen5barThick1 = 30         #difference between both = thickness 
Screen5barThick2 = 34         # 56 and 62 = 6 Pixel thick
Screen5barNibbleWidth = 2

#config for Spectrum
Screen5specDistance = 34
Screen5specBorder = (130, 130, 130)
Screen5specFill = (130, 130, 130)
Screen5specWide1 = 3.3
Screen5specWide2 = 0
Screen5specYposTag = 28
Screen5specYposNoTag = 28

#config for Spectrum2 NoProgress
Screen55specDistance = 35
Screen55specBorder = (130, 130, 130)
Screen55specFill = (130, 130, 130)
Screen55specWide1 = 3.5
Screen55specWide2 = 1
Screen55specYposTag = 33
Screen55specYposNoTag = 33

#config for leftVU
Screen5leftVUDistance = 35
Screen5leftVUBorder = (80, 80, 80)
Screen5leftVUFill = (80, 80, 80)
Screen5leftVUWide1 = 1.5
Screen5leftVUWide2 = 0
Screen5leftVUYpos1 = 38
Screen5leftVUYpos2 = 45

#config for leftVU NoProgress
Screen55leftVUDistance = 35
Screen55leftVUBorder = (80, 80, 80)
Screen55leftVUFill = (80, 80, 80)
Screen55leftVUWide1 = 1.5
Screen55leftVUWide2 = 0
Screen55leftVUYpos1 = 38
Screen55leftVUYpos2 = 45

#config for rightVU
Screen5rightVUDistance = 241
Screen5rightVUBorder = (80, 80, 80)
Screen5rightVUFill = (80, 80, 80)
Screen5rightVUWide1 = 1.5
Screen5rightVUWide2 = 0
Screen5rightVUYpos1 = 38
Screen5rightVUYpos2 = 45

#config for rightVU NoProgress
Screen55rightVUDistance = 241
Screen55rightVUBorder = (80, 80, 80)
Screen55rightVUFill = (80, 80, 80)
Screen55rightVUWide1 = 1.5
Screen55rightVUWide2 = 0
Screen55rightVUYpos1 = 38
Screen55rightVUYpos2 = 45

#_______'VU-Meter-2'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen7text01 = 35, 0        #Artist
Screen7text02 = 35, 14       #Title
Screen7text012 = 35, 0       #Artist
Screen7text022 = 35, 19       #Title
Screen7text06 = 78, 14       #format
Screen7text07 = 101, 14     #samplerate
Screen7text08 = 148, 14     #bitdepth
Screen7text28 = 66, 13       #Play/Pause Indicator

#config for VU-Meter "Hand"/"Pointer"
Screen7leftVUcoordinates = [(105, 160, 5, 59), (105, 160, 8, 57), (105, 160, 11, 55), (105, 160, 14, 53), (105, 160, 17, 52), (105, 160, 20, 51), (105, 160, 23, 49), (105, 160, 26, 47), (105, 160, 29, 46), (105, 160, 32, 45), (105, 160, 35, 44), (105, 160, 38, 43), (105, 160, 41, 43), (105, 160, 44, 42), (105, 160, 47, 42), (105, 160, 50, 41), (105, 160, 53, 40), (105, 160, 56, 40), (105, 160, 59, 40), (105, 160, 62, 40), (105, 160, 65, 41), (105, 160, 68, 41), (105, 160, 71, 41), (105, 160, 74, 41), (105, 160, 77, 42), (105, 160, 80, 42), (105, 160, 83, 43), (105, 160, 86, 43), (105, 160, 89, 44), (105, 160, 92, 44), (105, 160, 95, 45), (105, 160, 98, 45), (105, 160, 101, 46)]              
Screen7rightVUcoordinates = [(191, 160, 133, 59), (191, 160, 136, 57), (191, 160, 139, 55), (191, 160, 142, 53), (191, 160, 145, 52), (191, 160, 148, 51), (191, 160, 151, 49), (191, 160, 154, 47), (191, 160, 157, 46), (191, 160, 160, 45), (191, 160, 1105, 44), (191, 160, 166, 43), (191, 160, 169, 43), (191, 160, 172, 42), (191, 160, 175, 42), (191, 160, 178, 41), (191, 160, 181, 40), (191, 160, 184, 40), (191, 160, 187, 40), (191, 160, 190, 40), (191, 160, 193, 41), (191, 160, 196, 41), (191, 160, 199, 41), (191, 160, 202, 41), (191, 160, 205, 42), (191, 160, 208, 42), (191, 160, 211, 43), (191, 160, 214, 43), (191, 160, 217, 44), (191, 160, 220, 44), (191, 160, 223, 45), (191, 160, 226, 45), (191, 160, 229, 45)]

#configuration of the duration and playtime (textbox-) positions
Screen7ActualPlaytimeText = 35, 14
Screen7DurationText = 207, 14

#config for Progress-Bar
Screen7barwidth = 208
Screen7barLineBorder = 'white'
Screen7barLineFill = 'white'
Screen7barLineX = 34
Screen7barLineThick1 = 26     #difference between both = thickness 
Screen7barLineThick2 = 26     # 59 and 59 = 1 Pixel thick
Screen7barBorder = 'white'
Screen7barFill = 'black'
Screen7barX = 34
Screen7barThick1 = 24         #difference between both = thickness 
Screen7barThick2 = 28         # 56 and 62 = 6 Pixel thick
Screen7barNibbleWidth = 2

#_______'VU-Meter-Bar'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen8text01 = 96, 0        #Artist
Screen8text02 = 96, 16       #Title
Screen8text012 = 35, 0       #Artist
Screen8text022 = 35, 19       #Title
Screen8text06 = 35, 2       #format
Screen8text07 = 44, 16     #samplerate
Screen8text08 = 56, 2     #bitdepth
Screen8text28 = 35, 14       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen8ActualPlaytimeText = 35, 29
Screen8DurationText = 207, 29

#config for Progress-Bar
Screen8barwidth = 130
Screen8barLineBorder = 'white'
Screen8barLineFill = 'white'
Screen8barLineX = 82
Screen8barLineThick1 = 34     #difference between both = thickness 
Screen8barLineThick2 = 34     # 59 and 59 = 1 Pixel thick
Screen8barBorder = 'white'
Screen8barFill = 'black'
Screen8barX = 82
Screen8barThick1 = 32         #difference between both = thickness 
Screen8barThick2 = 36         # 56 and 62 = 6 Pixel thick
Screen8barNibbleWidth = 2

#config for leftVU
Screen8leftVUDistance = 64  #startpoint oft the VU from the left side of the screen
Screen8leftVUWide1 = 6.7      #spacing/width of each value -> 32max value from cava * 7 = 224pixels width
Screen8leftVUWide2 = 4      #width of each Value from cava ->   Value <= Screen8leftVUWide1 -> results in Spaces between / Value >= Screen8leftVUWide1 -> continous Bar 
Screen8leftVUYpos1 = 40
Screen8leftVUYpos2 = 46

#config for rightVU
Screen8rightVUDistance = 64
Screen8rightVUWide1 = 6.7
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
oledtext10 = 180, 2      #Number of Artists
oledtext11 = 180, 15     #Number of Albums
oledtext12 = 180, 28     #Number of Songs
oledtext13 = 180, 41     #Summary of duration
oledtext14 = 56, 2       #Text for Artists
oledtext15 = 56, 15      #Text for Albums
oledtext16 = 56, 28      #Text for Songs
oledtext17 = 56, 41      #Text for duration
oledtext18 = 176, 52     #Menu-Label Icon
oledtext19 = 237, 54     #LibraryInfoIcon
oledtext20 = 42, 2        #icon for Artists
oledtext21 = 42, 15       #icon for Albums
oledtext22 = 42, 28       #icon for Songs
oledtext23 = 42, 41       #icon for duration

#___________________________________________________________________
#configuration Menu-Screen:
oledListEntrys = 4
oledEmptyListText = 'no items..'
oledEmptyListTextPosition = 42, 4
oledListTextPosX = 44
oledListTextPosY = 16    #height of each Entry (4x16 = 64)

#___________________________________________________________________
#config for Text:
oledArt = 'Interpreten :'  #sets the Artists-text for the MediaLibrarayInfo
oledAlb = 'Alben :'        #sets the Albums-text for the MediaLibrarayInfo
oledSon = 'Songs :'        #sets the Songs-text for the MediaLibrarayInfo
oledPla = 'Playtime :'     #sets the Playtime-text for the MediaLibrarayInfo

#___________________________________________________________________
#config for Icons:
oledlibraryInfo = '\U0001F4D6'
oledlibraryReturn = '\u2302'
oledArtistIcon = '\uF0F3'
oledAlbumIcon = '\uF2BB'
oledSongIcon = '\U0000F001'
oledPlaytimeIcon = '\U0000F1DA'
oledplayIcon = '\u25B6'
oledpauseIcon = '\u2389'

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

#Menu
oledMenuHighlightColor = (255, 255, 255)
oledMenuHighlightBackGround = (0, 0, 0)
oledMenuNotSelectedColor = (80, 80, 80)
oledMenuNotSelectedBackground = (0, 0, 0)
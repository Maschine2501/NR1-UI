#!/usr/bin/python3

#___________________________________________________________________
#config for boot- and shutdown-logo
oledBootLogo = "1322boot.bmp"
oledShutdownLogo = "1322shutdown.bmp"

#___________________________________________________________________
#config for Clock/Standby:
oledtext03 = 47, 4       #clock
oledtext04 = 0, 52      #IP
oledtext05 = 176, 52     #Date
oledtext09 = 244, 51   #LibraryInfoIcon

#_______Screen1_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen1text01 = 0, 0        #Artist
Screen1text02 = 0, 19       #Title
Screen1text06 = 76, 41       #format
Screen1text07 = 159, 41     #samplerate
Screen1text08 = 220, 41     #bitdepth
Screen1text28 = 66, 41       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen1ActualPlaytimeText = 65, 54
Screen1DurationText = 210, 54

#config for Progress-Bar
Screen1barwidth = 88
Screen1barLineBorder = 'white'
Screen1barLineFill = 'black'
Screen1barLineX = 114
Screen1barLineThick1 = 59     #difference between both = thickness 
Screen1barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen1barBorder = 'white'
Screen1barFill = 'black'
Screen1barX = 114
Screen1barThick1 = 57         #difference between both = thickness 
Screen1barThick2 = 61         # 56 and 62 = 6 Pixel thick
Screen1barNibbleWidth = 2

#config for Spectrum
Screen1specDistance = 0
Screen1specBorder = (255, 255, 255)
Screen1specFill = (255, 255, 255)
Screen1specWide1 = 1
Screen1specWide2 = 0
Screen1specYposTag = 63
Screen1specYposNoTag = 63

#config for Spectrum2 NoProgress
Screen11specDistance = 0
Screen11specBorder = (130, 130, 130)
Screen11specFill = (130, 130, 130)
Screen11specWide1 = 4
Screen11specWide2 = 0
Screen11specYposTag = 63
Screen11specYposNoTag = 63

#_______Screen2_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen2text01 = 0, 0        #Artist
Screen2text02 = 0, 19       #Title
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

#_______Screen3_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen3text01 = 0, 0        #Artist
Screen3text02 = 0, 19       #Title
Screen3text06 = 0, 41       #format
Screen3text07 = 95, 41     #samplerate
Screen3text08 = 156, 41     #bitdepth
Screen3text28 = 25, 41       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen3ActualPlaytimeText = 1, 54
Screen3DurationText = 146, 54

#config for Progress-Bar
Screen3barwidth = 88
Screen3barLineBorder = 'white'
Screen3barLineFill = 'black'
Screen3barLineX = 50
Screen3barLineThick1 = 59    #difference between both = thickness 
Screen3barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen3barBorder = 'white'
Screen3barFill = 'black'
Screen3barX = 50
Screen3barThick1 = 56         #difference between both = thickness 
Screen3barThick2 = 62         # 56 and 62 = 6 Pixel thick
Screen3barNibbleWidth = 2

#config for Spectrum
Screen3specDistance = 255         #Inverted! 255 - 1x64 =196
Screen3specBorder = (255, 255, 255)
Screen3specFill = (255, 255, 255)
Screen3specWide1 = 1
Screen3specWide2 = 0
Screen3specYposTag = 63
Screen3specYposNoTag = 63

#config for Spectrum2 NoProgress
Screen33specDistance = 0
Screen33specBorder = (130, 130, 130)
Screen33specFill = (130, 130, 130)
Screen33specWide1 = 4
Screen33specWide2 = 0
Screen33specYposTag = 63
Screen33specYposNoTag = 63


#_______Screen4_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen4text01 = 0, 0        #Artist
Screen4text02 = 0, 19       #Title
Screen4text06 = 12, 41       #format
Screen4text07 = 159, 41     #samplerate
Screen4text08 = 220, 41     #bitdepth
Screen4text28 = 2, 41       #Play/Pause Indicator

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

#_______Screen5_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen5text01 = 0, 51        #Artist
Screen5text02 = 0, 51       #Title
Screen5text012 = 0, 0       #Artist
Screen5text022 = 0, 19       #Title
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
Screen5leftVUDistance = 1
Screen5leftVUBorder = (80, 80, 80)
Screen5leftVUFill = (80, 80, 80)
Screen5leftVUWide1 = 2
Screen5leftVUWide2 = 1
Screen5leftVUYpos1 = 38
Screen5leftVUYpos2 = 45

#config for leftVU NoProgress
Screen55leftVUDistance = 0
Screen55leftVUBorder = (80, 80, 80)
Screen55leftVUFill = (80, 80, 80)
Screen55leftVUWide1 = 2
Screen55leftVUWide2 = 1
Screen55leftVUYpos1 = 38
Screen55leftVUYpos2 = 45

#config for rightVU
Screen5rightVUDistance = 253
Screen5rightVUBorder = (80, 80, 80)
Screen5rightVUFill = (80, 80, 80)
Screen5rightVUWide1 = 2
Screen5rightVUWide2 = 0
Screen5rightVUYpos1 = 38
Screen5rightVUYpos2 = 45

#config for rightVU NoProgress
Screen55rightVUDistance = 253
Screen55rightVUBorder = (80, 80, 80)
Screen55rightVUFill = (80, 80, 80)
Screen55rightVUWide1 = 2
Screen55rightVUWide2 = 0
Screen55rightVUYpos1 = 38
Screen55rightVUYpos2 = 45

#_______Screen6_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen6text01 = 0, 2        #Artist
Screen6text28 = 1, 14       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen6ActualPlaytimeText = 1, 0
Screen6DurationText = 220, 0

#_______Screen7_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen7text01 = 0, 0        #Artist
Screen7text02 = 0, 14       #Title
Screen7text012 = 0, 0       #Artist
Screen7text022 = 0, 19       #Title
Screen7text06 = 86, 14       #format
Screen7text07 = 109, 14     #samplerate
Screen7text08 = 156, 14     #bitdepth
Screen7text28 = 74, 13       #Play/Pause Indicator

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
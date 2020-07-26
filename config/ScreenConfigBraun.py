#!/usr/bin/python3

#___________________________________________________________________
#config for boot- and shutdown-logo
oledBootLogo = "volumio_logo.ppm"
oledShutdownLogo = "shutdown.ppm"

#___________________________________________________________________
#config for Clock/Standby:
oledtext03 = 65, 10       #clock
oledtext04 = 30, 54      #IP
oledtext05 = 150, 54     #Date
oledtext09 = 226, 54     #LibraryInfoIcon

#_______Screen1_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen1text01 = 36, 2        #Artist
Screen1text02 = 36, 22       #Title
Screen1text06 = 36, 41       #format
Screen1text07 = 155, 41     #samplerate
Screen1text08 = 209, 41     #bitdepth
Screen1text28 = 65, 41       #Play/Pause Indicator

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
Screen1barThick1 = 58         #difference between both = thickness 
Screen1barThick2 = 60         # 56 and 62 = 6 Pixel thick

#config for Spectrum
Screen1specBorder = (255, 255, 255)
Screen1specFill = (255, 255, 255)
Screen1specWide1 = 1
Screen1specWide2 = 0
Screen1specYposTag = 63
Screen1specYposNoTag = 63

#_______Screen2_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen2text01 = 36, 2        #Artist
Screen2text02 = 36, 22       #Title
Screen2text06 = 36, 41       #format
Screen2text07 = 156, 41     #samplerate
Screen2text08 = 209, 41     #bitdepth
Screen2text28 = 65, 41       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen2ActualPlaytimeText = 36, 54
Screen2DurationText = 200, 54

#config for Progress-Bar
Screen2barwidth = 115
Screen2barLineBorder = 'white'
Screen2barLineFill = 'black'
Screen2barLineX = 80
Screen2barLineThick1 = 59     #difference between both = thickness 
Screen2barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen2barBorder = 'white'
Screen2barFill = 'black'
Screen2barX = 80
Screen2barThick1 = 57         #difference between both = thickness 
Screen2barThick2 = 61         # 56 and 62 = 6 Pixel thick

#config for Spectrum
Screen2specDistance = 74
Screen2specBorder = (130, 130, 130)
Screen2specFill = (130, 130, 130)
Screen2specWide1 = 2
Screen2specWide2 = 0
Screen2specYposTag = 63
Screen2specYposNoTag = 63

#config for Spectrum2 NoProgress
Screen22specDistance = 42
Screen22specBorder = (130, 130, 130)
Screen22specFill = (130, 130, 130)
Screen22specWide1 = 3
Screen22specWide2 = 0
Screen22specYposTag = 63
Screen22specYposNoTag = 63


#_______Screen3_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen3text01 = 0, 0        #Artist
Screen3text02 = 0, 19       #Title
Screen3text06 = 12, 41       #format
Screen3text07 = 95, 41     #samplerate
Screen3text08 = 156, 41     #bitdepth
Screen3text28 = 2, 41       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen3ActualPlaytimeText = 1, 54
Screen3DurationText = 146, 54

#config for Progress-Bar
Screen3barwidth = 88
Screen3barLineBorder = 'white'
Screen3barLineFill = 'black'
Screen3barLineX = 50
Screen3barLineThick1 = 59     #difference between both = thickness 
Screen3barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen3barBorder = 'white'
Screen3barFill = 80
Screen3barX = 50
Screen3barThick1 = 56         #difference between both = thickness 
Screen3barThick2 = 62         # 56 and 62 = 6 Pixel thick

#config for Spectrum
Screen3specBorder = (80, 80, 80)
Screen3specFill = (80, 80, 80)
Screen3specWide1 = 1
Screen3specWide2 = 0
Screen3specYposTag = 63
Screen3specYposNoTag = 63

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
Screen4barThick1 = 58         #difference between both = thickness 
Screen4barThick2 = 60         # 56 and 62 = 6 Pixel thick

#___________________________________________________________________
#Config TextPositions Media-Library-Info-Screen:
oledtext10 = 138, 2      #Number of Artists
oledtext11 = 138, 18     #Number of Albums
oledtext12 = 138, 34     #Number of Songs
oledtext13 = 138, 50     #Summary of duration
oledtext14 = 50, 2       #Text for Artists
oledtext15 = 50, 18      #Text for Albums
oledtext16 = 50, 34      #Text for Songs
oledtext17 = 50, 50      #Text for duration
oledtext18 = 134, 52     #Menu-Label Icon
oledtext19 = 226, 54     #LibraryInfoIcon
oledtext20 = 36, 2        #icon for Artists
oledtext21 = 36, 18       #icon for Albums
oledtext22 = 36, 34       #icon for Songs
oledtext23 = 36, 50       #icon for duration

#___________________________________________________________________
#configuration Menu-Screen:
oledListEntrys = 4
oledEmptyListText = 'no items..'
oledEmptyListTextPosition = 38, 4
oledListTextPosX = 37
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
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

#_______Spectrum-Left_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen1text01 = 34, 0        #Artist
Screen1text02 = 34, 19       #Title
Screen1text06 = 110, 41       #format
Screen1text07 = 155, 41     #samplerate
Screen1text08 = 200, 41     #bitdepth
Screen1text28 = 100, 41       #Play/Pause Indicator                  ????????????

#configuration of the duration and playtime (textbox-) positions
Screen1ActualPlaytimeText = 99, 54
Screen1DurationText = 191, 54

#config for Progress-Bar
Screen1barwidth = 48
Screen1barLineBorder = 'white'
Screen1barLineFill = 'black'
Screen1barLineX = 141
Screen1barLineThick1 = 59     #difference between both = thickness 
Screen1barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen1barBorder = 'white'
Screen1barFill = 'black'
Screen1barX = 141
Screen1barThick1 = 57         #difference between both = thickness 
Screen1barThick2 = 61         # 56 and 62 = 6 Pixel thick
Screen1barNibbleWidth = 2

#config for Spectrum
Screen1specDistance = 34
Screen1specBorder = (255, 255, 255)
Screen1specFill = (255, 255, 255)
Screen1specWide1 = 1
Screen1specWide2 = 0
Screen1specYposTag = 63
Screen1specYposNoTag = 63

#config for Spectrum2 NoProgress
Screen11specDistance = 34
Screen11specBorder = (130, 130, 130)
Screen11specFill = (130, 130, 130)
Screen11specWide1 = 4
Screen11specWide2 = 0
Screen11specYposTag = 63
Screen11specYposNoTag = 63

#_______'Spectrum-Center'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen2text01 = 35, 0        #Artist
Screen2text02 = 35, 19       #Title
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

#_______'Spectrum-Right'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen3text01 = 35, 0        #Artist
Screen3text02 = 35, 19       #Title
Screen3text06 = 35, 41       #format
Screen3text07 = 87, 41     #samplerate
Screen3text08 = 138, 41     #bitdepth
Screen3text28 = 59, 41       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen3ActualPlaytimeText = 34, 54
Screen3DurationText = 125, 54

#config for Progress-Bar
Screen3barwidth = 48
Screen3barLineBorder = 'white'
Screen3barLineFill = 'black'
Screen3barLineX = 76
Screen3barLineThick1 = 59    #difference between both = thickness 
Screen3barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen3barBorder = 'white'
Screen3barFill = 'black'
Screen3barX = 76
Screen3barThick1 = 56         #difference between both = thickness 
Screen3barThick2 = 62         # 56 and 62 = 6 Pixel thick
Screen3barNibbleWidth = 2

#config for Spectrum
Screen3specDistance = 229         #Inverted! 255 - 1x64 =196
Screen3specBorder = (255, 255, 255)
Screen3specFill = (255, 255, 255)
Screen3specWide1 = 1
Screen3specWide2 = 0
Screen3specYposTag = 63
Screen3specYposNoTag = 63

#config for Spectrum2 NoProgress
Screen33specDistance = 34
Screen33specBorder = (130, 130, 130)
Screen33specFill = (130, 130, 130)
Screen33specWide1 = 3
Screen33specWide2 = 0
Screen33specYposTag = 63
Screen33specYposNoTag = 63


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

#_______'VU-Meter-1'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen6text01 = 34, 2        #Artist
Screen6text28 = 34, 14       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen6ActualPlaytimeText = 35, 0
Screen6DurationText = 207, 0

#config for VU-Meter "Hand"/"Pointer"
Screen6leftVUcoordinates = [(105, 160, 47, 47), (105, 160, 49, 45), (105, 160, 52, 43), (105, 160, 54, 41), (105, 160, 56, 40), (105, 160, 59, 39), (105, 160, 61, 37), (105, 160, 64, 35), (105, 160, 66, 34), (105, 160, 68, 33), (105, 160, 71, 32), (105, 160, 73, 31), (105, 160, 75, 31), (105, 160, 78, 30), (105, 160, 80, 30), (105, 160, 83, 29), (105, 160, 85, 28), (105, 160, 87, 28), (105, 160, 90, 28), (105, 160, 92, 28), (105, 160, 94, 29), (105, 160, 97, 29), (105, 160, 99, 29), (105, 160, 102, 29), (105, 160, 104, 30), (105, 160, 106, 30), (105, 160, 109, 31), (105, 160, 111, 31), (105, 160, 113, 32), (105, 160, 116, 32), (105, 160, 118, 33), (105, 160, 121, 33), (105, 160, 123, 34)]
Screen6rightVUcoordinates = [(191, 160, 154, 47), (191, 160, 157, 45), (191, 160, 159, 43), (191, 160, 161, 41), (191, 160, 164, 40), (191, 160, 166, 39), (191, 160, 169, 37), (191, 160, 171, 35), (191, 160, 173, 34), (191, 160, 176, 33), (191, 160, 178, 32), (191, 160, 180, 31), (191, 160, 183, 31), (191, 160, 185, 30), (191, 160, 188, 30), (191, 160, 190, 29), (191, 160, 192, 28), (191, 160, 195, 28), (191, 160, 197, 28), (191, 160, 199, 28), (191, 160, 202, 29), (191, 160, 204, 29), (191, 160, 207, 29), (191, 160, 209, 29), (191, 160, 211, 30), (191, 160, 214, 30), (191, 160, 216, 31), (191, 160, 218, 31), (191, 160, 221, 32), (191, 160, 223, 32), (191, 160, 226, 33), (191, 160, 228, 33), (191, 160, 230, 34)]

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

#_______'Modern-simplistic'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen9text01 = 92, 53        #Artist
Screen9text02 = 92, 53       #Title
Screen9text012 = 92, 53       #Artist
Screen9text022 = 92, 53       #Title
Screen9text06 = 91, 39       #format
Screen9text07 = 123, 39     #samplerate
Screen9text08 = 163, 39     #bitdepth
Screen9text28 = 113, 37       #Play/Pause Indicator

#configuration of the duration and playtime (textbox-) positions
Screen9ActualPlaytimeText = 35, 39
Screen9DurationText = 207, 39

#config for Progress-Bar
Screen9barwidth = 128
Screen9barLineBorder = 'white'
Screen9barLineFill = 'white'
Screen9barLineX = 76
Screen9barLineThick1 = 44     #difference between both = thickness 
Screen9barLineThick2 = 44     # 59 and 59 = 1 Pixel thick
Screen9barBorder = 'white'
Screen9barFill = 'black'
Screen9barX = 76
Screen9barThick1 = 42         #difference between both = thickness 
Screen9barThick2 = 46         # 56 and 62 = 6 Pixel thick
Screen9barNibbleWidth = 2

#config for Spectrum
Screen9specDistance = 34
Screen9specBorder = (130, 130, 130)
Screen9specFill = (130, 130, 130)
Screen9specWide1 = 3.3
Screen9specWide2 = 0
Screen9specYposTag = 38
Screen9specYposNoTag = 38
Screen9specHigh = 1.5

#config for Spectrum2 NoProgress
Screen99specDistance = 35
Screen99specBorder = (130, 130, 130)
Screen99specFill = (130, 130, 130)
Screen99specWide1 = 3.5
Screen99specWide2 = 1
Screen99specYposTag = 43
Screen99specYposNoTag = 43

#config for leftVU
Screen9leftVUDistance = 35
Screen9leftVUBorder = (80, 80, 80)
Screen9leftVUFill = (80, 80, 80)
Screen9leftVUWide1 = 1.5
Screen9leftVUWide2 = 0
Screen9leftVUYpos1 = 53
Screen9leftVUYpos2 = 58

#config for leftVU NoProgress
Screen99leftVUDistance = 35
Screen99leftVUBorder = (80, 80, 80)
Screen99leftVUFill = (80, 80, 80)
Screen99leftVUWide1 = 1.5
Screen99leftVUWide2 = 0
Screen99leftVUYpos1 = 53
Screen99leftVUYpos2 = 58

#config for rightVU
Screen9rightVUDistance = 241
Screen9rightVUBorder = (80, 80, 80)
Screen9rightVUFill = (80, 80, 80)
Screen9rightVUWide1 = 1.5
Screen9rightVUWide2 = 0
Screen9rightVUYpos1 = 53
Screen9rightVUYpos2 = 58

#config for rightVU NoProgress
Screen99rightVUDistance = 241
Screen99rightVUBorder = (80, 80, 80)
Screen99rightVUFill = (80, 80, 80)
Screen99rightVUWide1 = 1.5
Screen99rightVUWide2 = 0
Screen99rightVUYpos1 = 53
Screen99rightVUYpos2 = 58

#config for gradient color of the VU
Screen9specGradstart = 80
Screen9specGradstop = 255
Screen9specGradSamples = 32

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
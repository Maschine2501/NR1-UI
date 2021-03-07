#!/usr/bin/python3

#___________________________________________________________________
#config for boot- and shutdown-logo
oledBootLogo = "StartScreen1306.bmp"
oledShutdownLogo = "ShutdownScreen1306.bmp"

#___________________________________________________________________
#config for Clock/Standby:
oledtext03 = 0, 2       #clock
oledtext04 = 39, 42      #IP
oledtext05 = 55, 29     #Date
oledtext09 = 116, 54     #LibraryInfoIcon

#_______Screen1 'Spectrum-Screen'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen1text01 = 0, 0        #Artist
Screen1text02 = 0, 18       #Title
Screen1text06 = 8, 38       #format
Screen1text07 = 32, 38     #samplerate
Screen1text08 = 85, 38     #bitdepth
Screen1text28 = 0, 38

#configuration of the duration and playtime (textbox-) positions
Screen1ActualPlaytimeText = 0, 51
Screen1DurationText = 78, 51

#config for Progress-Bar
Screen1barwidth = 28
Screen1barLineBorder = 'white'
Screen1barLineFill = 'black'
Screen1barLineX = 45
Screen1barLineThick1 = 59     #difference between both = thickness 
Screen1barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen1barBorder = 'white'
Screen1barFill = 'black'
Screen1barX = 45
Screen1barThick1 = 56         #difference between both = thickness 
Screen1barThick2 = 62         # 56 and 62 = 6 Pixel thick

#config for Spectrum
Screen1specBorder = 'white'
Screen1specFill = 'white'
Screen1specWide1 = 2
Screen1specWide2 = 0
Screen1specYposTag = 63
Screen1specYposNoTag = 63

#_______Screen2 'Essential'_____________________________________________________
Screen2text01 = 0, 24        #Artist
Screen2text02 = 0, 0       #Title
Screen2text06 = 8, 50       #format
Screen2text07 = 38, 41     #samplerate
Screen2text08 = 85, 41     #bitdepth
Screen2text28 = 0, 50

#configuration of the duration and playtime (textbox-) positions
Screen2ActualPlaytimeText = 0, 54
Screen2DurationText = 78, 54

#config for Progress-Bar
Screen2barwidth = 128
Screen2barLineBorder = 'white'
Screen2barLineFill = 'black'
Screen2barLineX = 0
Screen2barLineThick1 = 63     #difference between both = thickness 
Screen2barLineThick2 = 63     # 59 and 59 = 1 Pixel thick
Screen2barBorder = 'white'
Screen2barFill = 'white'
Screen2barX = 0
Screen2barThick1 = 63         #difference between both = thickness 
Screen2barThick2 = 63         # 56 and 62 = 6 Pixel thick

#_______Screen3 'Progress-Bar'_____________________________________________________
#Config TextPositions NowPlaying-/StandBy-Screen:
Screen4text01 = 0, 0        #Artist
Screen4text02 = 0, 18       #Title
Screen4text06 = 8, 38       #format
Screen4text07 = 32, 38     #samplerate
Screen4text08 = 85, 38     #bitdepth
Screen4text28 = 0, 38

#configuration of the duration and playtime (textbox-) positions
Screen4ActualPlaytimeText = 0, 51
Screen4DurationText = 84, 51

#config for Progress-Bar
Screen4barwidth = 32
Screen4barLineBorder = 'white'
Screen4barLineFill = 'black'
Screen4barLineX = 43
Screen4barLineThick1 = 59     #difference between both = thickness 
Screen4barLineThick2 = 59     # 59 and 59 = 1 Pixel thick
Screen4barBorder = 'white'
Screen4barFill = 'black'
Screen4barX = 43
Screen4barThick1 = 56         #difference between both = thickness 
Screen4barThick2 = 62         # 56 and 62 = 6 Pixel thick

#___________________________________________________________________
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

#___________________________________________________________________
#configuration Menu-Screen:
oledListEntrys = 4
oledEmptyListText = 'no items..'
oledEmptyListTextPosition = 0, 4
oledListTextPosX = 0
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
oledMenuHighlightColor = 'black'
oledMenuHighlightBackGround = 'white'
oledMenuNotSelectedColor = 'white'
oledMenuNotSelectedBackground = 'black'

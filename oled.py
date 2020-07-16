#! /usr/bin/python
# #-*- coding: utf-8 -*-
from luma.core.interface.serial import spi
from luma.oled.device import ssd1322
from luma.core.render import canvas
from PIL import Image
from PIL import ImageFont
import sys
import subprocess
from time import sleep

# Spectrum Config
# Rectangle(i*X1, Y1, i*X2+X2B, Y2-int(data[i]))
X1 = 2
Y1 = 44
X2 = 2
X2B = 2
Y2 = 44
dataMultiplikator = 1
Border = 'white'
Filling = 150, 150, 150

# Loudnes Bar Left
LX1 = 1
LY1 = 48
LX2 = 1
LY2 = 62
LMulti = 1.5

# Loudnes Bar Right
RX1 = 254
RY1 = 48 
RX2 = 255
RY2 = 62
RMulti = 1.5


# Text
TextAPos = 0, 29
TextA = '                        _______ '
TextBPos = 0, 47
TextB = '__________/ Volumio\_____________'

def load_font(filename, font_size):
    font = ImageFont.truetype(filename, font_size)
    return font

font1 = load_font('oxanium.ttf', 16)


try: 
   subprocess.check_output('pgrep -x cava', shell = True)
except:
   subprocess.call("cava &", shell = True)

#device = ssd1322(spi(device=0 , port=0))

interface = spi(device=0 , port=0)
device = ssd1322(interface, rotate=2) 

cava_fifo = open("/tmp/cava_fifo", 'r')
cava2_fifo = open("/tmp/cava2_fifo", 'r')
sleep(3.0)
while True:
    data = cava_fifo.readline().strip().split(';')
    data2 = cava2_fifo.readline().strip().split(';')
    print('Fifo-Data-Full: ', data)
    xyz = len(data)
    print('length of Fifo: ', xyz)
    with canvas(device) as draw:
#         draw.rectangle((LX1, LY1, LX2+int(data2[0]), LY2), outline = 'white', fill = 'white')
#         draw.rectangle((RX1-int(data2[1]), RY1, RX2, RY2), outline = 'white', fill = 'white')
         draw.text((0, 29), TextA, font=font1, fill='white')
         draw.text((0, 47), TextB, font=font1, fill='white')
         draw.rectangle((0, 47, 3, 62), outline = 'black', fill = None)
         draw.rectangle((5, 47, 7, 62), outline = 'black', fill = None)
         draw.rectangle((9, 47, 11, 62), outline = 'black', fill = None)
         draw.rectangle((13, 47, 15, 62), outline = 'black', fill = None)
         draw.rectangle((17, 47, 19, 62), outline = 'black', fill = None)
         draw.rectangle((21, 47, 23, 62), outline = 'black', fill = None)
         draw.rectangle((25, 47, 27, 62), outline = 'black', fill = None)
         draw.rectangle((29, 47, 31, 62), outline = 'black', fill = None)
         draw.rectangle((33, 47, 35, 62), outline = 'black', fill = None)
         draw.rectangle((37, 47, 39, 62), outline = 'black', fill = None)
         draw.rectangle((41, 47, 43, 62), outline = 'black', fill = None)
         draw.rectangle((45, 47, 47, 62), outline = 'black', fill = None)
         draw.rectangle((49, 47, 51, 62), outline = 'black', fill = None)
         draw.rectangle((53, 47, 55, 62), outline = 'black', fill = None)
         draw.rectangle((57, 47, 59, 62), outline = 'black', fill = None)
         draw.rectangle((253, 47, 255, 62), outline = 'black', fill = None)
         draw.rectangle((249, 47, 251, 62), outline = 'black', fill = None)
         draw.rectangle((245, 47, 247, 62), outline = 'black', fill = None)
         draw.rectangle((241, 47, 243, 62), outline = 'black', fill = None)
         draw.rectangle((237, 47, 239, 62), outline = 'black', fill = None)
         draw.rectangle((233, 47, 235, 62), outline = 'black', fill = None)
         draw.rectangle((229, 47, 231, 62), outline = 'black', fill = None)
         draw.rectangle((225, 47, 227, 62), outline = 'black', fill = None)
         draw.rectangle((221, 47, 223, 62), outline = 'black', fill = None)
         draw.rectangle((217, 47, 219, 62), outline = 'black', fill = None)
         draw.rectangle((213, 47, 215, 62), outline = 'black', fill = None)
         draw.rectangle((209, 47, 211, 62), outline = 'black', fill = None)
         draw.rectangle((205, 47, 207, 62), outline = 'black', fill = None)
         draw.rectangle((201, 47, 203, 62), outline = 'black', fill = None)
         draw.rectangle((197, 47, 199, 62), outline = 'black', fill = None)
         

         for i in range(0, len(data)-1):
#                print(i)
                 try:
                        draw.rectangle((i*X1, Y1, i*X2+X2B, Y2-(int(data[i])*dataMultiplikator)), outline = Border, fill = Filling)
                 except:
                        pass

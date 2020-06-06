#!/usr/bin/env python3

import sys, tty, termios, os, readchar, time
import psutil
from pcf8574 import PCF8574

i2c_port_num = 1
pcf_address = 0x20
pcf = PCF8574(i2c_port_num, pcf_address)

io1 = pcf.port[7] 
io2 = pcf.port[6]
io3 = pcf.port[5]
io4 = pcf.port[4]
io5 = pcf.port[3]

while True:
    CPUpercent = psutil.cpu_percent(interval=0.2, percpu=False)
    io1=io2=io3=io4=io5 = True
    if CPUpercent > 75:
        io1=io2=io3=io4=io5 = False
    elif CPUpercent > 50 :
        io1=io2=io3=io4 = False
    elif CPUpercent > 25:
        io1=io2=io3 = False
    elif CPUpercent > 10:
        io1=io2 = False
    elif CPUpercent > 2:
        io1 = False
    elif CPUpercent < 2:
        io1=io2=io3=io4=io5 = True


#!/usr/bin/env python3

import sys, tty, termios, os, readchar, time
import psutil
from pcf8574 import PCF8574

i2c_port_num = 1
pcf_address = 0x20
pcf = PCF8574(i2c_port_num, pcf_address)

while True:
    CPUpercent = psutil.cpu_percent(interval=0.2, percpu=False)
    pcf.port[7] = True
    pcf.port[6] = True
    pcf.port[5] = True
    pcf.port[4] = True
    pcf.port[3] = True
    if CPUpercent > 75:
      pcf.port[7] = False
      pcf.port[6] = False
      pcf.port[5] = False
      pcf.port[4] = False
      pcf.port[3] = False
    elif CPUpercent > 50 :
      pcf.port[7] = False
      pcf.port[6] = False
      pcf.port[5] = False
      pcf.port[4] = False
      pcf.port[3] = True
    elif CPUpercent > 25:
      pcf.port[7] = False 
      pcf.port[6] = False
      pcf.port[5] = False
      pcf.port[4] = True
      pcf.port[3] = True
    elif CPUpercent > 10:
      pcf.port[7] = False
      pcf.port[6] = False
      pcf.port[5] = True
      pcf.port[4] = True
      pcf.port[3] = True
    elif CPUpercent > 2:
      pcf.port[7] = False
      pcf.port[6] = True
      pcf.port[5] = True
      pcf.port[4] = True
      pcf.port[3] = True
    elif CPUpercent < 2:
      pcf.port[7] = True
      pcf.port[6] = True
      pcf.port[5] = True
      pcf.port[4] = True
      pcf.port[3] = True


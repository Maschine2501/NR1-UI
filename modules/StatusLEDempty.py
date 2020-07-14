#!/usr/bin//python3

import sys
import os
from time import sleep
import psutil


def SysStart():
    print('System started...)')
    sleep(0.5)

def CPUload():
   while True:
       CPUpercent = psutil.cpu_percent(interval=0.2, percpu=False)
       if CPUpercent > 75:
          print('CPU Load over 75%')
          sleep(10)
       elif CPUpercent > 50 :
          print('CPU Load between 75perc. and 50perc.%')
          sleep(10)
       elif CPUpercent > 25:
          print('CPU Load between 50perc. and 25perc.%')
          sleep(10)
       elif CPUpercent > 10:
          print('CPU Load between 25perc. and 10perc.')
          sleep(10)
       elif CPUpercent > 2:
          print('CPU Load between 10perc. and 2perc.')
          sleep(10)
       elif CPUpercent < 2:
          print('CPU Load under 2%')
          sleep(10)

def PlayLEDon():
    print('Playback started')
    
def StereoLEDon():
    print('Stereo-Signal')
    
def PlayLEDoff():
    print('Playback stoped')
    
def StereoLEDoff():
    print('No Stereo-Signal')
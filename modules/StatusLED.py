#!/usr/bin//python3
import psutil
import time
from gpiozero import LED

CPU0 = LED(14)
CPU3 = LED(15)
CPU6 = LED(12)
PlayLED = LED(16)
StereoLED = LED(13)

def SysStart():
    CPU0.off()
    CPU3.off()
    CPU6.off()
    PlayLED.off()
    StereoLED.off()
    sleep(0.1)
    CPU0.on()
    PlayLED.on()
    sleep(0.5)
    CPU3.on()
    StereoLED.on()
    sleep(0.5)
    CPU6.on()
    sleep(1.0)
    CPU6.off()
    sleep(0.5)
    CPU6.off()
    StereoLED.off()
    sleep(0.5)
    CPU0.off()
    PlayLED.off()
    
def ProcessorLED():
    while True:
        picpu = int(psutil.cpu_percent(percpu=False))
        sleep(0.5)
        if picpu < 5:
            CPU0.off()
            CPU3.off()
            CPU6.off()
            sleep(0.5)
        if picpu < 33 and picpu > 5:
            CPU0.on()
            CPU3.off()
            CPU6.off()
            sleep(0.5)
        if picpu > 33 or picpu < 66:
            CPU0.on()
            CPU3.on()
            CPU6.off()
            sleep(0.5)
        if picpu > 66:
            CPU0.on()
            CPU3.on()
            CPU6.on()
            sleep(0.5)
    
def PlayLEDon():
    PlayLED.on()
    
def StereoLEDon():
    StereoLED.on()
    
def PlayLEDoff():
    PlayLED.off()
    
def StereoLEDoff():
    StereoLED.off()

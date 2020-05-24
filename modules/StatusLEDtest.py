#!/usr/bin//python3
import psutil
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

CPU0 = 14
CPU3 = 15
CPU6 = 12
PlayLED = 16
StereoLED = 13

GPIO.setup(CPU0, GPIO.OUT)
GPIO.setup(CPU3, GPIO.OUT)
GPIO.setup(CPU6, GPIO.OUT)
GPIO.setup(PlayLED, GPIO.OUT)
GPIO.setup(StereoLED, GPIO.OUT)
    
def ProcessorLED():
    while True:
        picpu = int(psutil.cpu_percent(percpu=False))
        sleep(0.5)
        if picpu < 5:
            GPIO.output(CPU0, GPIO.LOW)
            GPIO.output(CPU3, GPIO.LOW)
            GPIO.output(CPU6, GPIO.LOW)
            sleep(0.5)
        if picpu < 33 and picpu > 5:
            GPIO.output(CPU0, GPIO.HIGH) 
            GPIO.output(CPU3, GPIO.LOW)
            GPIO.output(CPU6, GPIO.LOW)
            sleep(0.5)
        if picpu > 33 or picpu < 66:
            GPIO.output(CPU0, GPIO.HIGH) 
            GPIO.output(CPU3, GPIO.HIGH) 
            GPIO.output(CPU6, GPIO.LOW)
            sleep(0.5)
        if picpu > 66:
            GPIO.output(CPU0, GPIO.HIGH) 
            GPIO.output(CPU3, GPIO.HIGH) 
            GPIO.output(CPU6, GPIO.HIGH) 
            sleep(0.5)
    
def PlayLEDon():
    GPIO.output(PlayLED, GPIO.HIGH)
    
def StereoLEDon():
    GPIO.output(StereoLED, GPIO.HIGH)
    
def PlayLEDoff():
    GPIO.output(layLED, GPIO.LOW) 
    
def StereoLEDoff():
    GPIO.output(StereoLED, GPIO.LOW) 

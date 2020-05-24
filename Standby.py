#!/usr/bin/env python

from subprocess import call
import RPi.GPIO as GPIO
from time import sleep

Standby = 26

GPIO.setmode(GPIO.BCM) # Set pin numbering to board numbering

GPIO.setup(Standby, GPIO.IN) # Set up PinSeven as an input

while (GPIO.input(Standby) == GPIO.LOW: # While button not pressed
    GPIO.wait_for_edge(Standby, GPIO.RISING) # Wait for a rising edge on PinSeven
    sleep(0.2); # Sleep 100ms to avoid triggering a shutdown when a spike occured
    if (GPIO.input(Standby) == GPIO.HIGH:
      call('poweroff', shell = False) # Initiate OS Poweroff

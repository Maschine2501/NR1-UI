#!/usr/bin//python3

im sys, tty, termios, os, readchar
from time im sleep
im psutil
from gpiozero im LED

led1 = LED(xx)
led2 = LED(xx)
led3 = LED(xx)
led4 = LED(xx)
led5 = LED(xx)
led6 = LED(xx)
led7 = LED(xx)
led8 = LED(xx)

# Usage of The LEDs:
# led7 = more than 02% CPU load
# led6 = more than 10% CPU load 
# led5 = more than 25% CPU load
# led4 = more than 50% CPU load
# led3 = more than 75% CPU load
# led2 = Power LED
# led1 = Play LED
# led0 = Stereo LED

def SysStart():
    led0.off()
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    sleep(0.1)
    led2.on()
    sleep(0.5)
    led7.on()
    sleep(0.5)
    led6.on()
    sleep(0.5)
    led5.on()
    sleep(0.5)
    led4.on()
    sleep(0.5)
    led3.on()
    sleep(0.5)
    led1.on()
    sleep(0.5)
    led0.on()
    sleep(0.5)
    led3.off()
    sleep(0.5)
    led4.off()
    sleep(0.5)
    led5.off()
    sleep(0.5)
    led6.off()
    led0.off()
    sleep(0.5)
    led7.off()
    led1.off()
    sleep(0.5)

def CPUload():
   while True:
       CPUpercent = psutil.cpu_percent(interval=0.2, percpu=False)
       led7.off()
       led6.off()
       led5.off()
       led4.off()
       led3.off()
       if CPUpercent > 75:
         led7.on()
         led6.on()
         led5.on()
         led4.on()
         led3.on()
       elif CPUpercent > 50 :
         led7.on()
         led6.on()
         led5.on()
         led4.on()
         led3.off()
       elif CPUpercent > 25:
         led7.on()
         led6.on()
         led5.on()
         led4.off()
         led3.off()
       elif CPUpercent > 10:
         led7.on()
         led6.on()
         led5.off()
         led4.off()
         led3.off()
       elif CPUpercent > 2:
         led7.on()
         led6.off()
         led5.off()
         led4.off()
         led3.off()
       elif CPUpercent < 2:
         led7.off()
         led6.off()
         led5.off()
         led4.off()
         led3.off()

def PlayLEDon():
    led.[1] = False
    
def StereoLEDon():
    led.[0] = False
    
def PlayLEDoff():
    led.[1] = True
    
def StereoLEDoff():
    led.[0] = True

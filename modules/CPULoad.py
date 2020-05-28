#import time
import RPi.GPIO as GPIO
import psutil

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

while True:
    mytime = psutil.cpu_percent(interval=0.2, percpu=False)
    io1=io2=io3 = False
    
    if mytime > 66:
        io1=io2=io3 = True
    elif mytime > 34:
        io1=io2 = True
    elif mytime < 33:
        io1 = True

    GPIO.output(11,io1)
    GPIO.output(12,io2)
    GPIO.output(13,io3)

from time import sleep
import RPi.GPIO as GPIO

class PushButton:

    def __init__(self, gpioPin, min_time=0.1, max_time=0.1):
        self.pin = gpioPin
        self.callbackFunction = False
        self.minimum_time = min_time
        self.maximum_time = max(max_time, min_time)

        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def setCallback(self, callback_function):
        self.callbackFunction = callback_function
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.callback)

    def callback(self, channel):
        measured_time = self.minimum_time/2
        sleep(self.minimum_time/2)
        if (GPIO.input(self.pin)): # false detect
            return
        for i in range(int(self.maximum_time*50 - self.minimum_time*25 + 0.5)): # count max_time seconds when button held down
            if (GPIO.input(self.pin)): # When button is released, go on.
                break
            measured_time += 0.02
            sleep(0.02)
        if measured_time >= self.minimum_time and channel == self.pin and self.callbackFunction:
            print('PIN: '+str(self.pin)+', time: '+str(measured_time))
            return self.callbackFunction(measured_time)

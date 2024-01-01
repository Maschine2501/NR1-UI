import RPi.GPIO as GPIO

class RotaryEncoder:

    UNKNOWN = 0
    LEFT = 1
    RIGHT = 2

    def __init__(self, pinA, pinB, pulses_per_cycle=4):
        self.pinA = pinA
        self.pinB = pinB
        self.callbackFunction = False
        self.ppc = pulses_per_cycle
        self.direction = RotaryEncoder.UNKNOWN
        self.prevState = 0b11
        self.relposition = 0;

        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def setCallback(self, callback_function):
        self.callbackFunction = callback_function
        GPIO.add_event_detect(self.pinA, GPIO.BOTH, callback=self.decodeRotation)
        GPIO.add_event_detect(self.pinB, GPIO.BOTH, callback=self.decodeRotation)

    def decodeRotation(self, channel):
        self.direction = RotaryEncoder.UNKNOWN
        MSB = int(GPIO.input(self.pinA))
        LSB = int(GPIO.input(self.pinB))

        newState = (MSB << 1) | LSB
        sm = (self.prevState << 2) | newState
        self.prevState = newState

        if(sm == 0b1101 or sm == 0b0100 or sm == 0b0010 or sm == 0b1011):
            self.relposition -= 1
            if self.relposition <= -self.ppc:
                self.relposition = 0
                self.direction = RotaryEncoder.LEFT
        elif (sm == 0b1110 or sm == 0b0111 or sm == 0b0001 or sm == 0b1000):
            self.relposition += 1
            if self.relposition >= self.ppc:
                self.relposition = 0
                self.direction = RotaryEncoder.RIGHT

        if newState == 0b11:   #locking position
            self.relposition = 0 
        if self.callbackFunction and self.direction != RotaryEncoder.UNKNOWN:
            return self.callbackFunction(self.direction)

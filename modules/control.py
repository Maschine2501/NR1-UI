import smbus
import RPi.GPIO as GPIO
import time
import requests
import threading
import subprocess
import json
import os

# Constants
ROW_PINS = [4, 17, 23, 12]  # GPIO4, GPIO17, GPIO23, GPIO12
COLUMN_PINS = [27, 22]        # GPIO pins for columns
DEBOUNCE_TIME = 150

DEVICE_ADDR = 0x27
IODIRA = 0x00
GPIOA = 0x12

VOLUMIO_URL = "http://localhost:3000/api/v1/commands/?cmd="


class MCP23017:
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address

    def write_byte_data(self, reg, value):
        self.bus.write_byte_data(self.address, reg, value)

    def read_byte_data(self, reg):
        return self.bus.read_byte_data(self.address, reg)

    def set_output(self, port, pin, state):
        current_state = self.read_byte_data(port)
        new_state = (current_state & ~(1 << pin)) | (state << pin)
        self.write_byte_data(port, new_state)


last_button_press_time = 10

def button_pressed(mcp23017, row, col):
    global last_button_press_time
    last_button_press_time = time.time()
    
    led_pin = (row * len(COLUMN_PINS)) + col
    state = not mcp23017.read_byte_data(GPIOA) & (1 << led_pin)
    mcp23017.set_output(GPIOA, led_pin, state)
    print(f"Button at row {row + 1}, column {col + 1} pressed, controlling LED on pin GPA{led_pin}")
    if row == 0 and col == 0:
        if GPIO.input(4) == GPIO.LOW:
            activate_play(mcp23017)
    elif row == 0 and col == 1:
        if GPIO.input(4) == GPIO.LOW:
            activate_pause(mcp23017)
    elif row == 1 and col == 0:
        activate_back(mcp23017)
    elif row == 1 and col == 1:
        activate_forward(mcp23017)
    elif row == 2 and col == 1:
        activate_repeat(mcp23017)
    elif row == 2 and col == 0:
        activate_shuffle(mcp23017)
    elif row == 3 and col == 1:
        if GPIO.input(12) == GPIO.LOW:
            activate_button7(mcp23017)
    elif row == 3 and col == 0:
        if GPIO.input(12) == GPIO.LOW:
            activate_button8(mcp23017) 

    timer = threading.Thread(target=turn_off_leds_after_delay, args=(10, mcp23017))
    timer.start()

def read_buttons(mcp23017):
    last_press_time = [0] * (len(ROW_PINS) * len(COLUMN_PINS))

    for col, col_pin in enumerate(COLUMN_PINS):
        GPIO.setup(col_pin, GPIO.OUT)
        GPIO.output(col_pin, GPIO.LOW)

        for row, row_pin in enumerate(ROW_PINS):
            if GPIO.input(row_pin) == GPIO.LOW:
                time.sleep(DEBOUNCE_TIME / 1000)
                if GPIO.input(row_pin) == GPIO.LOW:
                    button_pressed(mcp23017, row, col)

        GPIO.setup(col_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#==============================================================================================

def setup_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in ROW_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    for pin in COLUMN_PINS:
        GPIO.setup(pin, GPIO.OUT)

#==============================================================================================

def light_up_leds(mcp23017):
    # Set GPA0-GPA7 as output
    mcp23017.write_byte_data(IODIRA, 0x00)

    # Light up LEDs in sequence
    for i in range(8):
        # Turn on the i-th LED
        mcp23017.set_output(GPIOA, i, 1)
        time.sleep(1)  # Wait for 1 second

        # Turn off the i-th LED
        mcp23017.set_output(GPIOA, i, 0)
        time.sleep(0.1)  # Wait for 0.1 second

    # Light up LED 0 to indicate that the user needs to press play to start
    mcp23017.set_output(GPIOA, 0, 1)


#==============================================================================================


# Activating Functions:

def activate_play(mcp23017):
    try:
        response = requests.get(VOLUMIO_URL + "play")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
    else:
        print("Playback started.")
        deactivate_pause(mcp23017)
        deactivate_forward(mcp23017)
        deactivate_back(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_repeat(mcp23017)        
        deactivate_button7(mcp23017)
        deactivate_button8(mcp23017)

def activate_pause(mcp23017):
    try:
        response = requests.get(VOLUMIO_URL + "pause")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
    else:
        print("Playback paused.")
        deactivate_play(mcp23017)
        deactivate_forward(mcp23017)  
        deactivate_back(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_repeat(mcp23017)        
        deactivate_button7(mcp23017)
        deactivate_button8(mcp23017)

def activate_back(mcp23017):
    try:
        response = requests.get(VOLUMIO_URL + "prev")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
    else:
        print("Track skipped back.")
        deactivate_forward(mcp23017)
        deactivate_play(mcp23017)    
        deactivate_pause(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_repeat(mcp23017)       
        deactivate_button7(mcp23017)
        deactivate_button8(mcp23017)

def activate_forward(mcp23017):
    try:
        response = requests.get(VOLUMIO_URL + "next")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
    else:
        print("Track skipped forward.")
        deactivate_back(mcp23017)
        deactivate_play(mcp23017)    
        deactivate_pause(mcp23017)   
        deactivate_shuffle(mcp23017)
        deactivate_repeat(mcp23017)
        deactivate_button7(mcp23017)
        deactivate_button8(mcp23017)

def activate_shuffle(mcp23017):
    try:
        response = requests.get(VOLUMIO_URL + "random")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
    else:
        print("Shuffle mode toggled.")
        # Deactivate other buttons if needed
        deactivate_forward(mcp23017)
        deactivate_play(mcp23017)    
        deactivate_pause(mcp23017)
        deactivate_repeat(mcp23017)  
        deactivate_button7(mcp23017)
        deactivate_button8(mcp23017)
        

def activate_repeat(mcp23017):
    try:
        response = requests.get(VOLUMIO_URL + "repeat")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
    else:
        print("Repeat mode toggled.")
        # Deactivate other buttons if needed
        deactivate_forward(mcp23017)
        deactivate_play(mcp23017)    
        deactivate_pause(mcp23017)
        deactivate_shuffle(mcp23017)   
        deactivate_button7(mcp23017)
        deactivate_button8(mcp23017)


def activate_button7(mcp23017):
    # Set the flag file to communicate with script1
    with open("/tmp/button7_pressed_flag", "w") as flag_file:
        flag_file.write("1")


def activate_button8(mcp23017):
    # Set the flag file to communicate with script1
    with open("/tmp/button8_pressed_flag", "w") as flag_file:
        flag_file.write("1")

        
#==============================================================================================
        
def get_volumio_state():
    try:
        response = requests.get("http://localhost:3000/api/v1/getState")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None
    else:
        return json.loads(response.text)
        
#==============================================================================================

def deactivate_play(mcp23017):
    mcp23017.set_output(GPIOA, 0, 0)
    print("Play button deactivated.")

def deactivate_pause(mcp23017):
    if not mcp23017.read_byte_data(GPIOA) & (1 << 1):
        return
    mcp23017.set_output(GPIOA, 1, 0)
    print("Pause button deactivated.")

def deactivate_back(mcp23017):
    mcp23017.set_output(GPIOA, 2, 0)
    print("Back button deactivated.")

def deactivate_forward(mcp23017):
    mcp23017.set_output(GPIOA, 3, 0)
    print("Forward button deactivated.")

def deactivate_shuffle(mcp23017):
    mcp23017.set_output(GPIOA, 4, 0)
    print("Shuffle deactivated.")

def deactivate_repeat(mcp23017):
    mcp23017.set_output(GPIOA, 5, 0)
    print("Repeat deactivated.")

def deactivate_button7(mcp23017):
    mcp23017.set_output(GPIOA, 6, 0)
    print("Button7 deactivated.")

def deactivate_button8(mcp23017):
    mcp23017.set_output(GPIOA, 7, 0)
    print("Button8 deactivated.")

#=====================================================================================

def turn_off_leds_after_delay(delay, mcp23017):
    global last_button_press_time
    time.sleep(delay)
    current_time = time.time()
    if current_time - last_button_press_time >= delay:
        deactivate_play(mcp23017)
        deactivate_pause(mcp23017)
        deactivate_back(mcp23017)
        deactivate_forward(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_repeat(mcp23017)
        deactivate_button7(mcp23017)
        deactivate_button8(mcp23017)
        
#=====================================================================================
        
def monitor_volumio_state(mcp23017):
    while True:
        volumio_state = get_volumio_state()
        if volumio_state:
            if volumio_state["status"] == "play":
                mcp23017.set_output(GPIOA, 0, 1)
            else:
                mcp23017.set_output(GPIOA, 0, 0)

            if volumio_state["status"] == "pause":
                mcp23017.set_output(GPIOA, 1, 1)
            else:
                mcp23017.set_output(GPIOA, 1, 0)
                
            if volumio_state["status"] == "play":
                if "disablePrev" in volumio_state and not volumio_state["disablePrev"]:
                    mcp23017.set_output(GPIOA, 2, 1)
                else:
                    mcp23017.set_output(GPIOA, 2, 0)
                    
                if "disableNext" in volumio_state and not volumio_state["disableNext"]:
                    mcp23017.set_output(GPIOA, 3, 1)
                else:
                    mcp23017.set_output(GPIOA, 3, 0)

        time.sleep(1)  # Sleep for 1 second before checking again

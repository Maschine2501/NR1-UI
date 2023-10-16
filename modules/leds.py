#!/usr/bin/python3

import requests
import subprocess
import json
import time
from modules.mcp23017 import MCP23017, DEVICE_ADDR, IODIRA, GPIOA

delay = 0.5

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
    print("Back button deactivated.")

def deactivate_repeat(mcp23017):
    mcp23017.set_output(GPIOA, 5, 0)
    print("Forward button deactivated.")    

def deactivate_favourites(mcp23017):
    mcp23017.set_output(GPIOA, 6, 0)
    print("Favourites deactivated.")

def deactivate_ButtonC(mcp23017):
    mcp23017.set_output(GPIOA, 7, 0)
    print("ButtonC deactivated.")

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


#=====================================================================================
def turn_off_leds_after_delay(mcp23017, delay, last_press_times):
    time.sleep(delay)
    current_time = time.time()

    for led_pin in range(1, 8):  # Skip 0, the play button LED
        if current_time - last_press_times[led_pin] >= delay:
            mcp23017.set_output(GPIOA, led_pin, 0)
            print(f"LED on pin GPA{led_pin} deactivated.")


#!/usr/bin/python3

import time
import requests
import json
from socketIO_client import SocketIO
from modules.leds import turn_off_leds_after_delay, deactivate_favourites, deactivate_play, deactivate_pause, deactivate_back, deactivate_forward, deactivate_shuffle, deactivate_repeat, deactivate_ButtonC
from modules.mcp23017 import MCP23017, DEVICE_ADDR, IODIRA, GPIOA
from modules.button_functions import ButtonC_PushEvent

VOLUMIO_URL = "http://localhost:3000/api/v1/commands/?cmd="


volumioIO = SocketIO('localhost', 3000)


def activate_play(mcp23017):
    try:
        volumioIO.emit('play')
    except Exception as e:
        print("Error: ", e)
    else:
        print("Playback started.")
        deactivate_pause(mcp23017)
        deactivate_forward(mcp23017)
        deactivate_back(mcp23017)
        deactivate_repeat(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_favourites(mcp23017)
        deactivate_ButtonC(mcp23017)
        mcp23017.set_output(GPIOA, 0, 1)
        print("Play button activated.")      

def activate_pause(mcp23017):
    try:
        volumioIO.emit('pause')
    except Exception as e:
        print("Error: ", e)
    else:
        print("Playback paused.")
        deactivate_play(mcp23017)
        deactivate_forward(mcp23017)
        deactivate_back(mcp23017)
        deactivate_repeat(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_favourites(mcp23017)
        deactivate_ButtonC(mcp23017)
        mcp23017.set_output(GPIOA, 0, 0)
        print("Play button deactivated.")


def activate_back(mcp23017):
    try:
        volumioIO.emit('prev')
    except Exception as e:
        print("Error: ", e)
    else:
        print("Track skipped back.")
        deactivate_play(mcp23017)
        deactivate_pause(mcp23017)
        deactivate_forward(mcp23017)
        deactivate_repeat(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_favourites(mcp23017)
        deactivate_ButtonC(mcp23017)


def activate_forward(mcp23017):
    try:
        volumioIO.emit('next')
    except Exception as e:
        print("Error: ", e)
    else:
        print("Track skipped forward.")
        deactivate_play(mcp23017)
        deactivate_pause(mcp23017)
        deactivate_back(mcp23017)
        deactivate_repeat(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_favourites(mcp23017)
        deactivate_ButtonC(mcp23017)


def activate_shuffle(mcp23017):
    try:
        volumio_state = get_volumio_state()
        if volumio_state and "random" in volumio_state:
            current_random = volumio_state["random"]
            new_random_mode = not current_random
            volumioIO.emit('setRandom', {'value': new_random_mode})
    except Exception as e:
        print("Error: ", e)
    else:
        print("Random mode toggled.")
        deactivate_play(mcp23017)
        deactivate_pause(mcp23017)
        deactivate_forward(mcp23017)
        deactivate_back(mcp23017)
        deactivate_repeat(mcp23017)
        deactivate_favourites(mcp23017)
        deactivate_ButtonC(mcp23017)



def activate_repeat(mcp23017):
    try:
        volumio_state = get_volumio_state()
        if volumio_state and "repeat" in volumio_state:
            current_repeat = volumio_state["repeat"]
            new_repeat_mode = not current_repeat
            volumioIO.emit('setRepeat', {'value': new_repeat_mode})
    except Exception as e:
        print('Error:', e)
    else:
        print('Repeat mode toggled.')
        deactivate_play(mcp23017)
        deactivate_pause(mcp23017)
        deactivate_forward(mcp23017)
        deactivate_back(mcp23017)
        deactivate_shuffle(mcp23017)
        deactivate_favourites(mcp23017)
        deactivate_ButtonC(mcp23017)



def activate_favourites(mcp23017):
    try:
        volumioIO.emit('playPlaylist', {'name': 'favourites'})
    except Exception as e:
        print("Error: ", e)
    else:
        print("Favourites playlist loaded.")
        deactivate_play(mcp23017)
        deactivate_pause(mcp23017)
        deactivate_forward(mcp23017)
        deactivate_back(mcp23017)
        deactivate_repeat(mcp23017)
        deactivate_shuffle(mcp23017)


def activate_ButtonC(mcp23017):
    print("ButtonC pressed.")
    deactivate_play(mcp23017)
    deactivate_pause(mcp23017)
    deactivate_forward(mcp23017)
    deactivate_back(mcp23017)
    deactivate_repeat(mcp23017)
    deactivate_shuffle(mcp23017)
    deactivate_favourites(mcp23017)
    ButtonC_PushEvent()
    
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


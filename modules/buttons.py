#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import threading
from modules.mcp23017 import MCP23017, DEVICE_ADDR, IODIRA, GPIOA
from modules.volumiosocket import activate_play, activate_pause, activate_back, activate_forward, activate_shuffle, activate_repeat
from modules.leds import delay, turn_off_leds_after_delay, deactivate_play, deactivate_pause, deactivate_back, deactivate_forward, deactivate_shuffle, deactivate_repeat

ROW_PINS = [4, 17, 23, 12]  # GPIO4, GPIO17, GPIO23, GPIO12
COLUMN_PINS = [22, 27]        # GPIO pins for columns
DEBOUNCE_TIME = 200

last_press_time = [0] * (len(ROW_PINS) * len(COLUMN_PINS))
last_button_press_time = 3

def setup_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in ROW_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    for pin in COLUMN_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def button_pressed(mcp23017, row, col, volumioIO, button_action_map):
    global last_button_press_time
    last_button_press_time = time.time()

    led_pin = (row * len(COLUMN_PINS)) + col
    state = not mcp23017.read_byte_data(GPIOA) & (1 << led_pin)
    mcp23017.set_output(GPIOA, led_pin, state)
    print(f"Button at row {row + 1}, column {col + 1} pressed, controlling LED on pin GPA{led_pin}")

    button_actions = {
        (0, 0): activate_play,
        (0, 1): activate_pause,
        (1, 0): activate_back,
        (1, 1): activate_forward,
        (2, 0): activate_shuffle,
        (2, 1): activate_repeat,
        (3, 0): 'ButtonD',
        (3, 1): 'ButtonC'
    }

    action = button_actions.get((row, col), None)
    if action is not None:
        if isinstance(action, str):
            button_action_map[action]()
        else:
            action(mcp23017)
            volumioIO.emit('button_pressed', action)

    timer = threading.Thread(target=turn_off_leds_after_delay, args=(mcp23017, delay, last_press_time))
    timer.start()



def read_buttons(mcp23017, volumioIO, button_action_map):
    global last_press_time

    for col, col_pin in enumerate(COLUMN_PINS):
        GPIO.setup(col_pin, GPIO.OUT)
        GPIO.output(col_pin, GPIO.LOW)

        for row, row_pin in enumerate(ROW_PINS):
            if GPIO.input(row_pin) == GPIO.LOW:
                time.sleep(DEBOUNCE_TIME / 1000)
                if GPIO.input(row_pin) == GPIO.LOW:
                    button_pressed(mcp23017, row, col, volumioIO, button_action_map)
                    last_press_time[(row * len(COLUMN_PINS)) + col] = time.monotonic()
                    timer = threading.Thread(target=turn_off_leds_after_delay, args=(mcp23017, delay, last_press_time))
                    timer.start()
        GPIO.setup(col_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Import required libraries
import smbus
import time
import subprocess
import requests
import json
from socketIO_client import SocketIO

# MCP23017 register definitions
MCP23017_IODIRA = 0x00  # I/O direction register for Port A
MCP23017_IODIRB = 0x01  # I/O direction register for Port B
MCP23017_GPIOA = 0x12   # Register for outputs on Port A
MCP23017_GPIOB = 0x13   # Register for outputs on Port B
MCP23017_GPPUA = 0x0C   # Pull-up resistors configuration for Port A
MCP23017_GPPUB = 0x0D   # Pull-up resistors configuration for Port B
MCP23017_ADDRESS = 0x27

# Initial configuration
print("Configuring MCP23017 I/O expander.")
bus = smbus.SMBus(1)  # Initialize SMBus
print("SMBus initialized.")

# Configure Port B: PB0 and PB1 as output, PB2-PB5 as input with pull-up resistors
bus.write_byte_data(MCP23017_ADDRESS, MCP23017_IODIRB, 0x3C)
bus.write_byte_data(MCP23017_ADDRESS, MCP23017_GPPUB, 0x3C)

# Configure Port A as outputs for LEDs
bus.write_byte_data(MCP23017_ADDRESS, MCP23017_IODIRA, 0x00)
print("MCP23017 ports configured.")

# Define button matrix mapping (4 rows, 2 columns)
button_map = [
    [2, 1],  # Row 1
    [4, 3],  # Row 2
    [6, 5],  # Row 3
    [8, 7]   # Row 4
]

# Function to read button matrix state
def read_button_matrix():
    button_matrix_state = [[0] * 2 for _ in range(4)]

    for column in range(2):
        bus.write_byte_data(MCP23017_ADDRESS, MCP23017_GPIOB, ~(1 << column) & 0x03)
        row_state = bus.read_byte_data(MCP23017_ADDRESS, MCP23017_GPIOB) & 0x3C

        for row in range(4):
            button_matrix_state[row][column] = (row_state >> (row + 2)) & 1

    return button_matrix_state

# Function to control LEDs
def control_leds(led_state):
    print(f"Setting LED state to {led_state}.")
    bus.write_byte_data(MCP23017_ADDRESS, MCP23017_GPIOA, led_state)

# Function to check buttons and update LED states
def check_buttons_and_update_leds():
    global prev_button_state  # Use the global variable prev_button_state

    button_matrix = read_button_matrix()
    for row in range(4):  # Assuming 4 rows
        for col in range(2):  # Assuming 2 columns
            button_id = button_map[row][col]
            current_button_state = button_matrix[row][col]

            # Check for rising edge (button press)
            if current_button_state == 0 and prev_button_state[row][col] != current_button_state:
                print(f"Button {button_id} pressed")
                led_state = 1 << (button_id - 1)
                control_leds(led_state)

            # Update the previous button state
            prev_button_state[row][col] = current_button_state

    time.sleep(0.1)  # Debounce delay

# Initialize prev_button_state
prev_button_state = [[1] * 2 for _ in range(4)]

# Main loop
while True:
    check_buttons_and_update_leds()

import smbus
import time

MCP23017_ADDRESS = 0x27  # Adjust as per your setup
MCP23017_IODIRA = 0x00   # I/O direction register for Port A
MCP23017_GPIOA = 0x12    # Register for outputs on Port A

# Initialize SMBus
bus = smbus.SMBus(1)

# Set Port A as outputs for LEDs
bus.write_byte_data(MCP23017_ADDRESS, MCP23017_IODIRA, 0x00)  # Outputs: PA0-PA7

# Turn on the last LED (PA7)
bus.write_byte_data(MCP23017_ADDRESS, MCP23017_GPIOA, 0x80)  # 0x80 in binary is 10000000, which turns on PA7

# Keep the LED on for a certain time (e.g., 10 seconds)
time.sleep(45)

# Turn off all LEDs before exiting the script
bus.write_byte_data(MCP23017_ADDRESS, MCP23017_GPIOA, 0x00)

import smbus

DEVICE_ADDR = 0x27
IODIRA = 0x00
GPIOA = 0x12

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


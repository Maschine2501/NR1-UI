import time
from PIL import Image

# Set the path to your boot logo GIF
gif_path = "/home/volumio/NR1-UI/img/bootlogo.gif"

def show_boot_logo(oled):
    try:
        # Open the GIF file
        gif = Image.open(gif_path)
        while True:
            oled.display(gif)
            oled.show()
            time.sleep(0.1)  # Adjust the delay as needed
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Initialize your OLED display and call show_boot_logo function
    # This is where you set up your OLED and call show_boot_logo


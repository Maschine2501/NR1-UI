import time
from PIL import Image, ImageSequence

def show_loading_gif(oled, gif_path, display_time=45):
    start_time = time.time()

    # Load the GIF
    gif = Image.open(gif_path)

    while time.time() - start_time < display_time:
        for frame in ImageSequence.Iterator(gif):
            # Convert the frame to RGB mode
            image = frame.convert("RGB")
            try:
                oled.display(image)
                oled.show()
            except AssertionError as e:
                print(f"AssertionError: {e}")
                print(f"Image mode: {image.mode}, OLED mode: {oled.mode}")
            time.sleep(0.05)


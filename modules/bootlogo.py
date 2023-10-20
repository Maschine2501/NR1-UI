import time
from PIL import Image, ImageSequence

def show_boot_logo_gif(oled, gif_path, display_time=10, frame_duration=0.1):
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
            time.sleep(frame_duration)  # Adjust the sleep time to control the animation speed


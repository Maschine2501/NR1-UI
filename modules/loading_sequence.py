import time
from PIL import Image

def show_loading_sequence(oled, path_to_images, display_time=45):
    start_time = time.time()
    
    while time.time() - start_time < display_time:
        for i in range(1, 5):
            image_path = f"{path_to_images}/dot{i}.bmp"
            image = Image.open(image_path).convert("RGB")  # Convert to RGB mode
            try:
                oled.display(image)
                oled.show()
            except AssertionError as e:
                print(f"AssertionError: {e}")
                print(f"Image mode: {image.mode}, OLED mode: {oled.mode}")
            time.sleep(0.5)


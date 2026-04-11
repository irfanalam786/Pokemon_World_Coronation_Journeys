import os
from PIL import Image

class ImageManager:
    def __init__(self):
        self.base_path = "assets/images"

    def show(self, image_name):
        path = os.path.join(self.base_path, image_name)

        if not os.path.exists(path):
            print(f"[Image Missing] {image_name}")
            return

        try:
            img = Image.open(path)
            img.show()
        except Exception as e:
            print(f"[Error displaying image]: {e}")
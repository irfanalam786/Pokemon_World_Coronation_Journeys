import requests
from PIL import Image
from io import BytesIO

class ImageManager:
    def show(self, image_url):
        try:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img.show()
        except Exception as e:
            print(f"[Image Error]: {e}")
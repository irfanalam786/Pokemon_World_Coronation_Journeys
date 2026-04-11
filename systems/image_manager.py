import webbrowser

class ImageManager:
    def show(self, image_url):
        try:
            webbrowser.open(image_url)
        except Exception as e:
            print(f"[Image Error]: {e}")
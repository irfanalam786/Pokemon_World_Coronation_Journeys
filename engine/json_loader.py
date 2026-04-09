import json
import os

class JSONLoader:
    def __init__(self, base_path="data"):
        self.base_path = base_path

    def load(self, filename):
        path = os.path.join(self.base_path, filename)
        try:
            with open(path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"[ERROR] File not found: {filename}")
            return []
import json
import time

class StoryManager:
    def __init__(self):
        with open("data/story.json", "r") as f:
            self.story = json.load(f)

    def play_scene(self, scene):
        if scene not in self.story:
            return

        for line in self.story[scene]:
            self.type_text(f"{line['speaker']}: {line['text']}")
            time.sleep(0.5)

    def type_text(self, text, speed=0.02):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(speed)
        print()
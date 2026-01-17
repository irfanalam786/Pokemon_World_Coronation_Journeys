import json
from typing import Dict, List

class StoryManager:
    def __init__(self):
        self.story: Dict[str, List[str]] = {}

        with open("story/wcs_story.json", "r") as file:
            self.story = json.load(file)

    def show_story_path(self):
        print("\nWorld Coronation Series Path:")
        for rank, events in self.story.items():
            print(f"- {rank}: {events}")

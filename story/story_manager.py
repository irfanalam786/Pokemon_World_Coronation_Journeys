class StoryManager:
    def __init__(self):
        self.stages = ["Normal Class", "Great Class", "Ultra Class", "Master Class"]

    def get_next_stage(self, current):
        if current in self.stages:
            idx = self.stages.index(current)
            if idx + 1 < len(self.stages):
                return self.stages[idx + 1]
        return None

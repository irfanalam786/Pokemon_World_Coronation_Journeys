# decision_system/player_choices.py

class PlayerChoices:
    def __init__(self):
        self.starter = None
        self.path = None

    def choose_starter(self, choice):
        starters = {
            "1": ("Pikachu", 100, 55, 40, 90, "Electric"),
            "2": ("Charmander", 100, 52, 43, 65, "Fire"),
            "3": ("Squirtle", 110, 48, 65, 43, "Water")
        }

        if choice not in starters:
            print("Invalid starter choice. Try again.")
            return None

        self.starter = starters[choice]
        return starters[choice]

    def choose_path(self, choice):
        paths = {
            "1": "Battle Path",
            "2": "Exploration Path",
            "3": "Strategy Path"
        }

        if choice not in paths:
            print("Invalid path choice. Try again.")
            return None

        self.path = paths[choice]
        return paths[choice]

    def __str__(self):
        return f"Starter: {self.starter[0] if self.starter else None} | Path: {self.path}"
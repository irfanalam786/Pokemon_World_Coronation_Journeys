import json
import os

class SaveManager:
    def __init__(self, path="save/player_save.json"):
        self.path = path

    def save_game(self, player):
        data = {
            "name": player.name,
            "team": []
        }

        for p in player.team:
            pokemon_data = {
                "name": p.name,
                "hp": p.hp,
                "max_hp": p.max_hp,
                "level": p.level,
                "bond": p.bond
            }
            data["team"].append(pokemon_data)

        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)

        print("\n💾 Game Saved!")

    def load_game(self):
        if not os.path.exists(self.path):
            print("No save file found.")
            return None

        with open(self.path, "r") as file:
            data = json.load(file)

        print("\n📂 Save Loaded!")
        return data
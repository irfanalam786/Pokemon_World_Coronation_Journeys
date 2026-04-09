from engine.json_loader import JSONLoader

class Game:
    def __init__(self):
        self.loader = JSONLoader()

        # Load all data
        self.pokemon_data = self.loader.load("pokemon.json")
        self.moves_data = self.loader.load("moves.json")
        self.items_data = self.loader.load("items.json")
        self.trainers_data = self.loader.load("trainers.json")

    def start(self):
        print("🎮 Pokémon Anime RPG Started")
        print("\nLoaded Pokémon:")
        for p in self.pokemon_data:
            print(f"- {p['name']} (Level {p['level']})")

        print("\nLoaded Trainers:")
        for t in self.trainers_data:
            print(f"- {t['name']} ({t['personality']})")
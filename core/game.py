from engine.json_loader import JSONLoader
from models.pokemon import Pokemon
from models.trainer import Trainer

class Game:
    def __init__(self):
        self.loader = JSONLoader()

        # Load raw data
        self.pokemon_data = self.loader.load("pokemon.json")
        self.trainers_data = self.loader.load("trainers.json")

        # Convert to objects
        self.pokemon_objects = self.create_pokemon_objects()
        self.trainers = self.create_trainers()

    def create_pokemon_objects(self):
        return [Pokemon(p) for p in self.pokemon_data]

    def create_trainers(self):
        return [Trainer(t, self.pokemon_data) for t in self.trainers_data]

    def start(self):
        print("🎮 Game Started\n")

        print("=== Pokémon List ===")
        for p in self.pokemon_objects:
            print(p)

        print("\n=== Trainers ===")
        for t in self.trainers:
            print(t)
            for p in t.team:
                print(f"  -> {p}")
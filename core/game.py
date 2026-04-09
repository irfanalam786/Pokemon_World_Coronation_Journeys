from engine.json_loader import JSONLoader
from models.pokemon import Pokemon
from models.trainer import Trainer

class Game:
    def __init__(self):
        self.loader = JSONLoader()

        # Load raw data from JSON
        self.pokemon_data = self.loader.load("pokemon.json")
        self.trainers_data = self.loader.load("trainers.json")

        # Convert JSON → Objects
        self.pokemon_objects = self.create_pokemon_objects()
        self.trainers = self.create_trainers()

    # ----------------------------
    # OBJECT CREATION
    # ----------------------------

    def create_pokemon_objects(self):
        return [Pokemon(p) for p in self.pokemon_data]

    def create_trainers(self):
        return [Trainer(t, self.pokemon_data) for t in self.trainers_data]

    # ----------------------------
    # GAME START (DAY 3 TEST)
    # ----------------------------

    def start(self):
        print("🎮 Pokémon Anime RPG Started\n")

        # Select first Pokémon for testing
        pokemon = self.pokemon_objects[0]

        print("=== BEFORE EXP ===")
        print(pokemon)

        # Simulate battle result
        base_exp = 10
        opponent_level = 5

        exp_gain = base_exp * opponent_level

        print("\n--- Battle Finished ---")
        pokemon.gain_exp(exp_gain)

        print("\n=== AFTER EXP ===")
        print(pokemon)

        # Show trainers (for verification)
        print("\n=== TRAINERS ===")
        for t in self.trainers:
            print(t)
            for p in t.team:
                print(f"  -> {p}")
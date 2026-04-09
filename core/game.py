from engine.json_loader import JSONLoader
from models.pokemon import Pokemon
from models.trainer import Trainer
from models.item import Item

class Game:
    def __init__(self):
        self.loader = JSONLoader()

        # Load data
        self.pokemon_data = self.loader.load("pokemon.json")
        self.trainers_data = self.loader.load("trainers.json")
        self.items_data = self.loader.load("items.json")

        # Convert to objects
        self.pokemon_objects = self.create_pokemon_objects()
        self.trainers = self.create_trainers()
        self.items = self.create_items()

    def create_pokemon_objects(self):
        return [Pokemon(p) for p in self.pokemon_data]

    def create_trainers(self):
        return [Trainer(t, self.pokemon_data) for t in self.trainers_data]

    def create_items(self):
        return [Item(i) for i in self.items_data]

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def start(self):
        print("🎮 Pokémon Anime RPG Started\n")

        pokemon = self.pokemon_objects[0]

        print("=== INITIAL STATE ===")
        print(pokemon)

        # Get items
        potion = self.get_item_by_name("Potion")
        rare_candy = self.get_item_by_name("Rare Candy")

        # Damage Pokémon first
        print("\n--- Simulating Damage ---")
        pokemon.take_damage(20)
        print(pokemon)

        # Use Potion
        potion.use(pokemon)
        print(pokemon)

        # Use Rare Candy multiple times
        print("\n--- Using Rare Candy ---")
        for i in range(7):
            print(f"\nAttempt {i+1}")
            rare_candy.use(pokemon)

        print("\n=== FINAL STATE ===")
        print(pokemon)
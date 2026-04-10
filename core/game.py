from engine.json_loader import JSONLoader
from models.pokemon import Pokemon
from models.trainer import Trainer
from models.item import Item
from engine.battle_engine import BattleEngine

class Game:
    def __init__(self):
        self.loader = JSONLoader()

        # Load data
        self.pokemon_data = self.loader.load("pokemon.json")
        self.trainers_data = self.loader.load("trainers.json")
        self.items_data = self.loader.load("items.json")

        # Create objects
        self.pokemon_objects = self.create_pokemon_objects()
        self.trainers = self.create_trainers()
        self.items = self.create_items()

    def create_pokemon_objects(self):
        return [Pokemon(p) for p in self.pokemon_data]

    def create_trainers(self):
        return [Trainer(t, self.pokemon_data) for t in self.trainers_data]

    def create_items(self):
        return [Item(i) for i in self.items_data]

    def start(self):
        print("🎮 Pokémon Anime RPG Started\n")

        # Create player manually
        player_data = {
            "name": "Player",
            "personality": "calm",
            "team": ["Pikachu"]
        }

        player = Trainer(player_data, self.pokemon_data)
        opponent = self.trainers[0]

        # Start battle
        battle = BattleEngine(player, opponent)
        battle.start_battle()
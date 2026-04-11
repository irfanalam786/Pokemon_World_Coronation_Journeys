from engine.json_loader import JSONLoader
from models.trainer import Trainer
from engine.battle_engine import BattleEngine
from systems.inventory_manager import InventoryManager

class Game:
    def __init__(self):
        self.loader = JSONLoader()
        self.inventory = InventoryManager()

        self.pokemon_data = self.loader.load("pokemon.json")
        self.trainers_data = self.loader.load("trainers.json")
        self.moves_data = self.loader.load("moves.json")

        self.player = Trainer({
            "name": "Player",
            "team": ["Pikachu"]
        }, self.pokemon_data)

        self.opponent = Trainer(self.trainers_data[0], self.pokemon_data)

        self.battle = BattleEngine(self.player, self.opponent, self.moves_data, self.inventory)

    def attack(self):
        return self.battle.player_turn_ui()

    def opponent_turn(self):
        return self.battle.opponent_turn_ui()

    def get_state(self):
        return {
            "player": str(self.battle.player_pokemon),
            "opponent": str(self.battle.opponent_pokemon),
            "player_img": self.battle.player_pokemon.image,
            "opponent_img": self.battle.opponent_pokemon.image
        }
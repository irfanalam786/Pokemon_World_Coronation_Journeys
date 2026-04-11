from engine.json_loader import JSONLoader
from models.trainer import Trainer
from engine.battle_engine import BattleEngine
from systems.save_manager import SaveManager
from systems.difficulty_manager import DifficultyManager
from systems.inventory_manager import InventoryManager

class Game:
    def __init__(self):
        self.loader = JSONLoader()
        self.save_manager = SaveManager()
        self.difficulty = DifficultyManager()
        self.inventory = InventoryManager()

        self.pokemon_data = self.loader.load("pokemon.json")
        self.trainers_data = self.loader.load("trainers.json")
        self.moves_data = self.loader.load("moves.json")

        self.trainers = self.create_trainers()

    def create_trainers(self):
        return [Trainer(t, self.pokemon_data) for t in self.trainers_data]

    def create_player(self):
        return Trainer({
            "name": "Player",
            "personality": "calm",
            "team": ["Pikachu"]
        }, self.pokemon_data)

    def load_or_create_player(self):
        save_data = self.save_manager.load_game()

        if save_data:
            player = Trainer({
                "name": save_data["name"],
                "personality": "calm",
                "team": []
            }, self.pokemon_data)

            player.team = []

            from models.pokemon import Pokemon

            for p_data in save_data["team"]:
                for base in self.pokemon_data:
                    if base["name"] == p_data["name"] or \
                       (base.get("evolution") and base["evolution"]["name"] == p_data["name"]):

                        p = Pokemon(base)

                        p.hp = p_data["hp"]
                        p.max_hp = p_data["max_hp"]
                        p.level = p_data["level"]
                        p.bond = p_data["bond"]

                        if base.get("evolution") and base["evolution"]["name"] == p_data["name"]:
                            p.name = p_data["name"]
                            p.evolution = None

                        if p.hp <= 0:
                            p.hp = p.max_hp

                        player.team.append(p)

            return player

        return self.create_player()

    def start(self):
        print("🎮 Pokémon Anime RPG Started\n")

        player = self.load_or_create_player()
        opponent = self.trainers[0]

        for p in opponent.team:
            self.difficulty.adjust_pokemon(p)

        battle = BattleEngine(player, opponent, self.moves_data, self.inventory)
        battle.start_battle()

        self.difficulty.increase_difficulty()
        self.save_manager.save_game(player)
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

        self.trainers = [Trainer(t, self.pokemon_data) for t in self.trainers_data]

        self.badges = []

    def create_player(self):
        return Trainer({
            "name": "Player",
            "personality": "calm",
            "team": ["Pikachu"]
        }, self.pokemon_data)

    def start(self):
        print("🎮 Pokémon Anime RPG Started\n")

        player = self.create_player()

        # 🔥 FIRST BATTLE (RIVAL)
        rival = self.trainers[0]
        battle = BattleEngine(player, rival, self.moves_data, self.inventory)
        battle.start_battle()

        # 🔥 GYM BATTLE
        gym_leader = self.trainers[1]

        print(f"\n🏆 Gym Leader {gym_leader.name} challenges you!")
        gym_leader.apply_gym_boost()

        battle = BattleEngine(player, gym_leader, self.moves_data, self.inventory)
        battle.start_battle()

        # 🎖️ REWARD
        if player.has_pokemon_left():
            print(f"\n🎖️ You earned the {gym_leader.badge}!")
            self.badges.append(gym_leader.badge)

        print(f"\n🏅 Badges: {self.badges}")
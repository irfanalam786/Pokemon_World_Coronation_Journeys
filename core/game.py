from engine.json_loader import JSONLoader
from models.trainer import Trainer
from engine.battle_engine import BattleEngine
from systems.inventory_manager import InventoryManager
from systems.story_manager import StoryManager

class Game:
    def __init__(self):
        self.loader = JSONLoader()
        self.inventory = InventoryManager()
        self.story = StoryManager()

        self.pokemon_data = self.loader.load("pokemon.json")
        self.trainers_data = self.loader.load("trainers.json")
        self.moves_data = self.loader.load("moves.json")

        self.trainers = [Trainer(t, self.pokemon_data) for t in self.trainers_data]

        self.badges = []

    def create_player(self):
        return Trainer({
            "name": "Player",
            "team": ["Pikachu"]
        }, self.pokemon_data)

    def start(self):
        print("🎮 Pokémon Anime RPG Started\n")

        player = self.create_player()

        # 🎬 INTRO
        self.story.play_scene("intro")

        # 🔥 RIVAL BATTLE
        rival = self.trainers[0]

        self.story.play_scene("rival_before")

        battle = BattleEngine(player, rival, self.moves_data, self.inventory)
        battle.start_battle()

        if player.has_pokemon_left():
            self.story.play_scene("rival_after_win")

        # 🔥 GYM BATTLE
        gym = self.trainers[1]

        print(f"\n🏆 Gym Leader {gym.name} challenges you!")
        gym.apply_gym_boost()

        self.story.play_scene("gym_before")

        battle = BattleEngine(player, gym, self.moves_data, self.inventory)
        battle.start_battle()

        if player.has_pokemon_left():
            self.story.play_scene("gym_after_win")
            print(f"\n🎖️ You earned the {gym.badge}!")
            self.badges.append(gym.badge)

        print(f"\n🏅 Badges: {self.badges}")
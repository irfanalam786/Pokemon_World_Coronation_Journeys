from engine.json_loader import JSONLoader
from models.pokemon import Pokemon
from models.trainer import Trainer
from engine.battle_engine import BattleEngine
from systems.save_manager import SaveManager

class Game:
    def __init__(self):
        self.loader = JSONLoader()
        self.save_manager = SaveManager()

        self.pokemon_data = self.loader.load("pokemon.json")
        self.trainers_data = self.loader.load("trainers.json")

        self.trainers = self.create_trainers()

    def create_trainers(self):
        return [Trainer(t, self.pokemon_data) for t in self.trainers_data]

    def create_player(self):
        player_data = {
            "name": "Player",
            "personality": "calm",
            "team": ["Pikachu"]
        }
        return Trainer(player_data, self.pokemon_data)

    def load_or_create_player(self):
        save_data = self.save_manager.load_game()

        if save_data:
            player = Trainer({
                "name": save_data["name"],
                "personality": "calm",
                "team": []
            }, self.pokemon_data)

            player.team = []

            for p_data in save_data["team"]:

                # 🔥 HANDLE OLD SAVE (STRING FORMAT)
                if isinstance(p_data, str):
                    for base in self.pokemon_data:
                        if base["name"] == p_data:
                            player.team.append(Pokemon(base))

                # ✅ HANDLE NEW SAVE (DICT FORMAT)
                else:
                    for base in self.pokemon_data:
                        if base["name"] == p_data["name"]:
                            p = Pokemon(base)
                            p.hp = p_data["hp"]
                            p.max_hp = p_data["max_hp"]
                            p.level = p_data["level"]
                            p.bond = p_data["bond"]
                            player.team.append(p)

            return player

        return self.create_player()

    def start(self):
        print("🎮 Pokémon Anime RPG Started\n")

        player = self.load_or_create_player()
        opponent = self.trainers[0]

        battle = BattleEngine(player, opponent)
        battle.start_battle()

        self.save_manager.save_game(player)
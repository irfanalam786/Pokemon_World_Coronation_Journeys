# core/save_manager.py

import json
from models.pokemon import Pokemon
from models.trainer import Trainer


class SaveManager:
    def save_game(self, trainer, choices, filename="save.json"):
        try:
            data = {
                "trainer": {
                    "name": trainer.get_name(),
                    "rank": trainer.get_rank(),
                    "points": trainer.get_points(),
                    "team": []
                },
                "choices": {
                    "starter": choices.starter,
                    "path": choices.path
                }
            }

            # 🔥 FULL POKEMON STATE SAVE
            for p in trainer.get_team():
                data["trainer"]["team"].append({
                    "name": p.get_name(),
                    "type": p.get_type(),
                    "role": p.get_role(),
                    "level": p.get_level(),
                    "exp": p.get_exp(),
                    "hp": p.get_hp(),
                    "status": p.get_status()
                })

            with open(filename, "w") as f:
                json.dump(data, f, indent=4)

            print("Game saved successfully!")

        except Exception as e:
            print("Error saving game:", e)

    def load_game(self, filename="save.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            trainer_data = data["trainer"]
            trainer = Trainer(trainer_data["name"])

            trainer.set_rank(trainer_data["rank"])
            trainer.set_points(trainer_data["points"])

            # 🔥 FULL RESTORE
            for p_data in trainer_data["team"]:
                p = Pokemon(
                    p_data["name"],
                    100, 50, 50, 50,  # base placeholder
                    p_data["type"],
                    p_data["role"]
                )

                p.set_level(p_data["level"])
                p.gain_exp(p_data["exp"])
                p.set_hp(p_data["hp"])

                if p_data["status"]:
                    p.apply_status(p_data["status"])

                trainer.add_pokemon(p)

            print("Game loaded successfully!")
            return trainer, data["choices"]

        except FileNotFoundError:
            print("No save file found.")
            return None, None

        except Exception as e:
            print("Error loading game:", e)
            return None, None
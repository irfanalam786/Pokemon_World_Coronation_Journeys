# core/difficulty_system.py

class DifficultySystem:
    def __init__(self, difficulty="Normal"):
        self.difficulty = difficulty

        self.settings = {
            "Easy": {
                "enemy_damage_multiplier": 0.8,
                "enemy_hp_multiplier": 0.9,
                "ai_aggression": 0.7
            },
            "Normal": {
                "enemy_damage_multiplier": 1.0,
                "enemy_hp_multiplier": 1.0,
                "ai_aggression": 1.0
            },
            "Hard": {
                "enemy_damage_multiplier": 1.3,
                "enemy_hp_multiplier": 1.2,
                "ai_aggression": 1.3
            }
        }

    def get_setting(self, key):
        return self.settings[self.difficulty][key]
# ai_system/basic_ai.py

import random


class BasicAI:
    def choose_action(self, attacker, defender, battle_engine):
        """
        Basic AI:
        - Always attack (for now)
        - Uses damage calculation to simulate intelligence
        - Adds slight randomness later
        """

        damage, _ = battle_engine.calculate_damage(attacker, defender)

        # Random factor (±10%)
        variation = random.uniform(0.9, 1.1)
        damage = int(damage * variation)

        return damage
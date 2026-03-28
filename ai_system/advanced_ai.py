# ai_system/advanced_ai.py

import random


class AdvancedAI:
    def choose_action(self, attacker, defender, trainer, battle_engine):
        """
        Returns:
        - ("attack", damage)
        - ("switch", index)
        """

        decisions = []

        # ---------------- DAMAGE EVALUATION ----------------
        # ✅ FIX: unpack 3 values now
        damage, multiplier, _ = battle_engine.calculate_damage(attacker, defender)

        defender_hp = defender.get_hp()

        # KO priority
        if damage >= defender_hp:
            decisions.append(("attack", damage, 100))

        # Type advantage
        if multiplier > 1:
            decisions.append(("attack", damage, 80))
        elif multiplier < 1:
            decisions.append(("attack", damage, 40))

        # HP safety
        hp_ratio = attacker.get_hp() / attacker._Pokemon__max_hp

        if hp_ratio < 0.3:
            for i, p in enumerate(trainer.get_team()):
                if not p.is_fainted() and p != attacker:
                    decisions.append(("switch", i, 90))

        # Switch advantage
        for i, p in enumerate(trainer.get_team()):
            if not p.is_fainted() and p != attacker:
                better_multiplier = battle_engine.get_type_multiplier(
                    p.get_type(), defender.get_type()
                )
                if better_multiplier > multiplier:
                    decisions.append(("switch", i, 70))

        # Default attack
        decisions.append(("attack", damage, 50))

        # Select best
        best = max(decisions, key=lambda x: x[2])
        action, value, _ = best

        # Small randomness
        if action == "attack":
            value = int(value * random.uniform(0.95, 1.05))

        return action, value
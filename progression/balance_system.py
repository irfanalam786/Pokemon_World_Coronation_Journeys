# progression/balance_system.py

class BalanceSystem:
    def __init__(self):
        self.max_damage_cap = 999
        self.min_damage = 1

        self.exp_multiplier = 1.0

    # ---------------- DAMAGE BALANCE ----------------
    def balance_damage(self, damage):
        if damage > self.max_damage_cap:
            return self.max_damage_cap
        if damage < self.min_damage:
            return self.min_damage
        return damage

    # ---------------- EXP BALANCE ----------------
    def calculate_exp_gain(self, winner_level, loser_level):
        base_exp = 50

        # Level difference scaling
        level_diff = loser_level - winner_level

        if level_diff > 0:
            bonus = level_diff * 5
        else:
            bonus = 0

        exp = (base_exp + bonus) * self.exp_multiplier
        return int(exp)
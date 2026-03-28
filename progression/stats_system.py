# progression/stats_system.py


class StatsSystem:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.total_battles = 0
        self.total_damage = 0

    # ---------------- UPDATE METHODS ----------------
    def record_win(self):
        self.wins += 1
        self.total_battles += 1

    def record_loss(self):
        self.losses += 1
        self.total_battles += 1

    def add_damage(self, amount):
        self.total_damage += amount

    # ---------------- DISPLAY ----------------
    def show_stats(self):
        print("\n=== 📊 PLAYER STATS ===")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Total Battles: {self.total_battles}")
        print(f"Total Damage Dealt: {self.total_damage}")
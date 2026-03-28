# progression/achievement_system.py


class AchievementSystem:
    def __init__(self):
        self.unlocked = set()

    def check_achievements(self, trainer):
        stats = trainer.stats

        # First Win
        if stats.wins >= 1 and "First Win" not in self.unlocked:
            self.unlock("First Win")

        # 5 Wins
        if stats.wins >= 5 and "5 Wins" not in self.unlocked:
            self.unlock("5 Wins")

        # Damage Milestone
        if stats.total_damage >= 500 and "Damage Dealer" not in self.unlocked:
            self.unlock("Damage Dealer")

        # Rank Up
        if trainer.get_rank() != "Normal" and "Rank Up" not in self.unlocked:
            self.unlock("Rank Up")

    def unlock(self, name):
        self.unlocked.add(name)
        print(f"🏆 Achievement Unlocked: {name}!")

    def show_achievements(self):
        print("\n=== 🏆 ACHIEVEMENTS ===")
        if not self.unlocked:
            print("No achievements yet.")
        else:
            for a in self.unlocked:
                print(f"- {a}")
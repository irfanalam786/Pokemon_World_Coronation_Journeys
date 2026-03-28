# ranking/leaderboard_system.py

import json


class LeaderboardSystem:
    def __init__(self, file="leaderboard.json"):
        self.file = file

    # ---------------- LOAD ----------------
    def load_leaderboard(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return []

    # ---------------- SAVE ----------------
    def save_leaderboard(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    # ---------------- UPDATE ----------------
    def update_leaderboard(self, trainer):
        data = self.load_leaderboard()

        entry = {
            "name": trainer.get_name(),
            "points": trainer.get_points(),
            "wins": trainer.stats.wins
        }

        data.append(entry)

        # Sort by points, then wins
        data.sort(key=lambda x: (x["points"], x["wins"]), reverse=True)

        self.save_leaderboard(data)

    # ---------------- DISPLAY ----------------
    def show_leaderboard(self):
        data = self.load_leaderboard()

        print("\n=== 🏆 LEADERBOARD ===")

        if not data:
            print("No records yet.")
            return

        for i, player in enumerate(data[:10], start=1):
            print(f"{i}. {player['name']} | Points: {player['points']} | Wins: {player['wins']}")
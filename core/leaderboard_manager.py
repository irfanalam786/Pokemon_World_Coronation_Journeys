# ==============================
# Leaderboard Manager System
# ==============================

# Import JSON module
import json

# Define leaderboard file name
LEADERBOARD_FILE = "leaderboard.json"

# Define LeaderboardManager class
class LeaderboardManager:

    # Load leaderboard data
    @staticmethod
    def load_leaderboard():
        try:
            # Open leaderboard file
            with open(LEADERBOARD_FILE, "r") as file:
                # Return loaded JSON data
                return json.load(file)
        except:
            # If file does not exist, return empty list
            return []

    # Save leaderboard data
    @staticmethod
    def save_leaderboard(data):
        # Open file in write mode
        with open(LEADERBOARD_FILE, "w") as file:
            # Write formatted JSON
            json.dump(data, file, indent=4)

    # Add new score to leaderboard
    @staticmethod
    def add_score(trainer_name, wins):

        # Load existing leaderboard
        leaderboard = LeaderboardManager.load_leaderboard()

        # Append new entry
        leaderboard.append({
            "trainer": trainer_name,
            "wins": wins
        })

        # Sort leaderboard by wins descending
        leaderboard.sort(key=lambda x: x["wins"], reverse=True)

        # Save updated leaderboard
        LeaderboardManager.save_leaderboard(leaderboard)

    # Display leaderboard
    @staticmethod
    def show_leaderboard():

        # Load leaderboard data
        leaderboard = LeaderboardManager.load_leaderboard()

        # Print header
        print("\n=== LEADERBOARD ===")

        # If empty
        if not leaderboard:
            print("No records yet.")
            return

        # Display top entries
        for i, entry in enumerate(leaderboard[:5], 1):
            print(f"{i}. {entry['trainer']} - Wins: {entry['wins']}")
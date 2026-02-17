# ==============================
# Game Statistics Manager
# ==============================

# Import JSON module
import json

# Define stats file name
STATS_FILE = "game_stats.json"

# Default statistics structure
DEFAULT_STATS = {
    "total_battles": 0,
    "wins": 0,
    "losses": 0,
    "total_damage_dealt": 0
}

# Define StatsManager class
class StatsManager:

    # Load statistics from file
    @staticmethod
    def load_stats():
        try:
            # Open stats file
            with open(STATS_FILE, "r") as file:
                # Load JSON data
                return json.load(file)
        except:
            # If file missing, create default
            StatsManager.save_stats(DEFAULT_STATS)
            return DEFAULT_STATS.copy()

    # Save statistics to file
    @staticmethod
    def save_stats(stats):
        # Open file in write mode
        with open(STATS_FILE, "w") as file:
            # Write formatted JSON
            json.dump(stats, file, indent=4)

    # Update battle result
    @staticmethod
    def record_battle(win):
        # Load current stats
        stats = StatsManager.load_stats()

        # Increment total battles
        stats["total_battles"] += 1

        # Update win/loss count
        if win:
            stats["wins"] += 1
        else:
            stats["losses"] += 1

        # Save updated stats
        StatsManager.save_stats(stats)

    # Record damage dealt
    @staticmethod
    def record_damage(amount):
        # Load stats
        stats = StatsManager.load_stats()

        # Add damage
        stats["total_damage_dealt"] += amount

        # Save stats
        StatsManager.save_stats(stats)

        # Check for Damage Master achievement
        from core.achievement_manager import AchievementManager

        if stats["total_damage_dealt"] >= 1000:
            AchievementManager.unlock("Damage Master")

    # Reset statistics
    @staticmethod
    def reset_stats():
        StatsManager.save_stats(DEFAULT_STATS.copy())
    
    # Reset statistics safely
    @staticmethod
    def safe_reset():
        StatsManager.reset_stats()
        print("Statistics reset successfully.")
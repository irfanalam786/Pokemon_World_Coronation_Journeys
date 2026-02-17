# ==============================
# Achievement Manager System
# ==============================

# Import JSON module
import json

# Define achievement file name
ACHIEVEMENT_FILE = "achievements.json"

# Default achievement structure
DEFAULT_ACHIEVEMENTS = {
    "First Victory": False,
    "Champion": False,
    "Damage Master": False
}

# Define AchievementManager class
class AchievementManager:

    # Load achievements
    @staticmethod
    def load_achievements():
        try:
            # Open file
            with open(ACHIEVEMENT_FILE, "r") as file:
                # Load JSON
                return json.load(file)
        except:
            # If file not found, create default
            AchievementManager.save_achievements(DEFAULT_ACHIEVEMENTS)
            return DEFAULT_ACHIEVEMENTS.copy()

    # Save achievements
    @staticmethod
    def save_achievements(data):
        with open(ACHIEVEMENT_FILE, "w") as file:
            json.dump(data, file, indent=4)

    # Unlock achievement
    @staticmethod
    def unlock(name):
        # Load achievements
        achievements = AchievementManager.load_achievements()

        # If not already unlocked
        if not achievements.get(name, False):
            achievements[name] = True
            AchievementManager.save_achievements(achievements)
            print(f"🏆 Achievement Unlocked: {name}")

    # Reset achievements
    @staticmethod
    def reset():
        AchievementManager.save_achievements(DEFAULT_ACHIEVEMENTS.copy())
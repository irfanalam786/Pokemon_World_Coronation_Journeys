# Import json module
import json

# Define settings file name
SETTINGS_FILE = "settings.json"

# Default settings dictionary
DEFAULT_SETTINGS = {
    "difficulty": "Normal"
}

# SettingsManager class
class SettingsManager:

    # Load settings safely
    @staticmethod
    def load_settings():
        try:
            # Open file
            with open(SETTINGS_FILE, "r") as file:
                # Load JSON
                settings = json.load(file)
                return settings
        except:
            # If file missing or corrupted, reset
            SettingsManager.save_settings(DEFAULT_SETTINGS)
            return DEFAULT_SETTINGS

    # Save settings to file
    @staticmethod
    def save_settings(settings):
        with open(SETTINGS_FILE, "w") as file:
            json.dump(settings, file, indent=4)

    # Set difficulty level
    @staticmethod
    def set_difficulty(level):
        settings = SettingsManager.load_settings()
        settings["difficulty"] = level
        SettingsManager.save_settings(settings)

    # Reset settings to default
    @staticmethod
    def reset_settings():
        SettingsManager.save_settings(DEFAULT_SETTINGS)
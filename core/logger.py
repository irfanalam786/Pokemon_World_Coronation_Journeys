# Import datetime module to record time
from datetime import datetime

# Define log file name
LOG_FILE = "game_log.txt"

# Logger class to handle logging
class GameLogger:

    # Static method so no object is needed
    @staticmethod
    def log(message):
        # Get current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Open log file in append mode
        with open(LOG_FILE, "a") as file:
            # Write timestamp and message
            file.write(f"[{timestamp}] {message}\n")

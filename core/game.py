# ==============================
# Game Controller - Final Release
# ==============================

# Import main menu
from ui.menu import MainMenu

# Import logger
from core.logger import GameLogger

# Import leaderboard manager
from core.leaderboard_manager import LeaderboardManager

# Import stats manager
from core.stats_manager import StatsManager

# Import version info
from config.version import VERSION, BUILD_NAME, RELEASE_STATUS

# Define Game class
class Game:

    # Constructor
    def __init__(self):

        # Create menu instance
        self.menu = MainMenu()

    # Start game
    def start(self):

        # Print game title
        print("Pokemon World: Coronation Journeys")

        # Print version information
        print(f"Version: {VERSION} | Build: {BUILD_NAME} | Status: {RELEASE_STATUS}")
        print("-----------------------------------")

        # Log game start
        GameLogger.log(f"Game started - Version {VERSION}")

        # Show main menu
        self.menu.show()

        # Log game exit
        GameLogger.log("Game exited")

        # Show summary before closing
        self.show_summary()

        # Print exit message
        print("\nGame closed successfully.")

    # Show final summary
    def show_summary(self):

        # Load statistics
        stats = StatsManager.load_stats()

        # Print summary header
        print("\n=== FINAL GAME SUMMARY ===")

        # Display statistics
        print(f"Total Battles: {stats['total_battles']}")
        print(f"Wins: {stats['wins']}")
        print(f"Losses: {stats['losses']}")
        print(f"Total Damage Dealt: {stats['total_damage_dealt']}")

        # Add to leaderboard if player won battles
        if stats["wins"] > 0:
            LeaderboardManager.add_score("Player", stats["wins"])

        # Show leaderboard
        LeaderboardManager.show_leaderboard()
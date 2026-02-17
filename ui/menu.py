# ==============================
# Main Menu System (Safe Exit Version)
# ==============================

# Import character selection screen
from ui.character_select import CharacterSelect

# Import save/load manager
from core.save_load import SaveLoadManager

# Import settings manager
from config.settings_manager import SettingsManager

# Define MainMenu class
class MainMenu:

    # Method to display main menu
    def show(self):

        # Infinite loop until user chooses to exit
        while True:

            # Display menu options
            print("\n1. Start New Game")
            print("2. Load Game")
            print("3. Settings")
            print("4. Exit")

            # Take user input
            choice = input("Enter choice: ").strip()

            # If user selects New Game
            if choice == "1":

                # Create character selector
                selector = CharacterSelect()

                # Start new game
                selector.select()

                # After game ends, return to menu automatically
                continue

            # If user selects Load Game
            elif choice == "2":

                # Attempt to load saved trainer
                trainer = SaveLoadManager.load_game()

                # If load successful
                if trainer:
                    selector = CharacterSelect()
                    selector.resume(trainer)

                # Return to menu
                continue

            # If user selects Settings
            elif choice == "3":

                # Open settings menu
                self.settings_menu()

                # Return to main menu
                continue

            # If user selects Exit
            elif choice == "4":

                # Print exit message
                print("Exiting game safely.")

                # Break loop cleanly
                break

            # If input invalid
            else:
                print("Invalid choice. Please enter 1, 2, 3 or 4.")

    # Settings menu method
    def settings_menu(self):

        # Display difficulty options
        print("\n1. Easy")
        print("2. Normal")
        print("3. Hard")
        print("4. Reset to Default")

        # Take user input
        choice = input("Enter choice: ").strip()

        # Easy mode
        if choice == "1":
            SettingsManager.set_difficulty("Easy")
            print("Difficulty set to Easy.")

        # Normal mode
        elif choice == "2":
            SettingsManager.set_difficulty("Normal")
            print("Difficulty set to Normal.")

        # Hard mode
        elif choice == "3":
            SettingsManager.set_difficulty("Hard")
            print("Difficulty set to Hard.")

        # Reset settings
        elif choice == "4":
            SettingsManager.reset_settings()
            print("Settings reset to default.")

        # Invalid input
        else:
            print("Invalid selection.")
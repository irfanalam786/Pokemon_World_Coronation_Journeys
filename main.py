# Import the main Game controller class
from core.game import Game

# Main function – program execution starts here
def main():
    # Create a Game object
    game = Game()
    # Start the game
    game.start()

# Ensures this file runs only when executed directly
if __name__ == "__main__":
    main()

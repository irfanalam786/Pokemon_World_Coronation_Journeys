# core/game_manager.py

from core.save_manager import SaveManager
from decision_system.player_choices import PlayerChoices
from models.pokemon import Pokemon
from models.trainer import Trainer


class GameManager:
    def __init__(self):
        self.save_manager = SaveManager()
        self.choices = PlayerChoices()
        self.player = None

    # ---------------- NEW GAME ----------------
    def setup_new_game(self):
        print("\n=== NEW GAME SETUP ===")

        starter = None
        while starter is None:
            choice = input("Choose starter (1-Pikachu, 2-Charmander, 3-Squirtle): ")
            starter = self.choices.choose_starter(choice)

        pokemon = Pokemon(*starter)

        self.player = Trainer("Ash")
        self.player.add_pokemon(pokemon)

        print("\nGame Started!")

    # ---------------- SAVE ----------------
    def save_game(self):
        if self.player:
            self.save_manager.save_game(self.player, self.choices)
        else:
            print("No game to save.")

    # ---------------- LOAD (FIXED) ----------------
    def load_game(self):
        trainer, choices = self.save_manager.load_game()

        if trainer:
            self.player = trainer

            # ✅ SAFE CHECK (fixes error)
            if choices is not None:
                self.choices.starter = choices.get("starter")
                self.choices.path = choices.get("path")

            print("Game loaded successfully!")
        else:
            print("Failed to load game.")

    # ---------------- EXIT ----------------
    def exit_game(self):
        print("\nSaving before exit...")
        self.save_game()
        print("Game saved. Exiting.")
        exit()
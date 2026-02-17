# ==============================
# File: character_select.py
# Purpose: Game flow with save/load support
# ==============================

from characters.ash import Ash
from characters.goh import Goh
from characters.chloe import Chloe
from battle.battle_engine import BattleEngine
from story.story_manager import StoryManager
from battle.opponent_factory import OpponentFactory
from core.save_load import SaveLoadManager
import time
from core.achievement_manager import AchievementManager

# Unlock Champion achievement
AchievementManager.unlock("Champion")

class CharacterSelect:
    def select(self):
        """
        Starts a new game
        """
        print("\nChoose your character:")
        print("1. Ash Ketchum")
        print("2. Goh")
        print("3. Chloe Cerise")

        choice = input("Enter choice: ")

        if choice == "1":
            trainer = Ash()
        elif choice == "2":
            trainer = Goh()
        elif choice == "3":
            trainer = Chloe()
        else:
            print("Invalid choice")
            return

        self.play_game(trainer)

    def resume(self, trainer):
        """
        Resumes a loaded game
        """
        self.play_game(trainer)

    def play_game(self, trainer):
        """
        Core game loop (new or loaded)
        """
        print(f"\nTrainer: {trainer.name}")
        print(f"Current Rank: {trainer.rank}")
        trainer.show_team()

        story = StoryManager()

        # Pre-Master Classes
        while trainer.rank != "Master Class":
            opponent = OpponentFactory.create_opponent(trainer.rank)
            battle = BattleEngine(trainer, opponent)
            battle.start_battle()

            SaveLoadManager.save_game(trainer)

            old_rank = trainer.rank
            trainer.promote_rank()
            print(f"Rank Progressed: {old_rank} → {trainer.rank}")

        # Masters Eight
        print("\n🏆 Masters Eight Tournament Begins!")
        time.sleep(1)

        for stage in range(3):
            opponent = OpponentFactory.create_opponent("Master Class", stage)
            battle = BattleEngine(trainer, opponent)
            battle.start_battle()
            SaveLoadManager.save_game(trainer)

        print("\n🌟 WORLD CHAMPION 🌟")




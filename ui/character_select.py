from characters.ash import Ash
from characters.goh import Goh
from characters.chloe import Chloe
from story.story_manager import StoryManager
from battle.battle_engine import BattleEngine
from battle.ai import AITrainer

class CharacterSelect:
    def select(self):
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
            print("Invalid choice.")
            return

        print(f"\nTrainer Selected: {trainer.name}")
        print("Starter Pokémon:")
        trainer.show_team()

        story = StoryManager()
        story.show_story_path()

        opponent = AITrainer()
        battle = BattleEngine(trainer, opponent)
        battle.start_battle()

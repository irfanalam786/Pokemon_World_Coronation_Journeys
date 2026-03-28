# main.py

from models.pokemon import Pokemon
from models.trainer import Trainer
from engine.battle_engine import BattleEngine
from core.save_manager import SaveManager


def main():
    print("=== 🔥 FINAL SYSTEM TEST – PHASE 1 ===\n")

    # ---------------- SETUP ----------------
    pikachu = Pokemon("Pikachu", 100, 55, 40, 90, "Electric", "speed")
    charizard = Pokemon("Charizard", 120, 80, 60, 85, "Fire", "attacker")
    blastoise = Pokemon("Blastoise", 130, 60, 80, 50, "Water", "tank")

    pikachu.set_level(10)
    charizard.set_level(10)
    blastoise.set_level(10)

    player = Trainer("Ash")
    opponent = Trainer("AI")

    player.add_pokemon(pikachu)

    opponent.add_pokemon(charizard)
    opponent.add_pokemon(blastoise)

    # ---------------- BATTLE ----------------
    engine = BattleEngine(difficulty="Normal")
    engine.start_battle(player, opponent)

    # ---------------- SAVE TEST ----------------
    print("\n💾 Testing Save System...")
    save = SaveManager()
    save.save_game(player, type("obj", (), {"starter": None, "path": None})())

    # ---------------- LOAD TEST ----------------
    print("\n📂 Testing Load System...")
    loaded_trainer, _ = save.load_game()

    if loaded_trainer:
        print("✔ Load successful:", loaded_trainer)
    else:
        print("❌ Load failed")

    print("\n=== ✅ PHASE 1 TEST COMPLETE ===")


if __name__ == "__main__":
    main()
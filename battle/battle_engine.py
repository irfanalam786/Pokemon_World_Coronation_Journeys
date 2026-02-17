# ==============================
# Battle Engine - Final Clean Version
# ==============================

# Import type effectiveness table
from config.constants import TYPE_EFFECTIVENESS
from core.stats_manager import StatsManager
from core.achievement_manager import AchievementManager

# Import logger
from core.logger import GameLogger

# Define BattleEngine class
class BattleEngine:

    # Constructor method
    def __init__(self, trainer, opponent):

        # Store trainer reference
        self.trainer = trainer

        # Store opponent reference
        self.opponent = opponent

        # Get first available Pokemon from trainer
        self.player = trainer.get_next_pokemon()

        # Get first available Pokemon from opponent
        self.enemy = opponent.get_next_pokemon()

    # Start battle method
    def start_battle(self):

        # Print battle start message
        from core.animation import type_text
        type_text("\n=== BATTLE START ===", 0.03)
        
        # Log battle start
        GameLogger.log(f"Battle started: {self.trainer.name} vs {self.opponent.name}")

        # Continue while both sides have Pokemon
        while self.player and self.enemy:

            # Display matchup
            print(f"\n{self.player.name} vs {self.enemy.name}")

            # Decide turn order based on speed
            if self.player.speed >= self.enemy.speed:
                self.player_attack()
                if not self.enemy.is_fainted():
                    self.enemy_attack()
            else:
                self.enemy_attack()
                if not self.player.is_fainted():
                    self.player_attack()

            # Handle player faint
            if self.player.is_fainted():
                print(f"{self.player.name} fainted!")
                GameLogger.log(f"{self.player.name} fainted")
                self.player = self.trainer.get_next_pokemon()

            # Handle enemy faint
            if self.enemy.is_fainted():
                print(f"{self.enemy.name} fainted!")
                GameLogger.log(f"{self.enemy.name} fainted")
                self.enemy = self.opponent.get_next_pokemon()

        # End battle
        self.end_battle()

    # Player attack method
    def player_attack(self):

        # Show available moves
        print("\nChoose a move:")
        for i, move in enumerate(self.player.moves, 1):
            print(f"{i}. {move.name}")

        # Loop until valid input
        while True:
            choice = input("Enter move number: ")

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.player.moves):
                    move = self.player.moves[index]
                    break

            print("Invalid input.")

        # Log move
        GameLogger.log(f"{self.player.name} used {move.name}")

        # Apply damage
        self.apply_damage(self.player, self.enemy, move)

    # Enemy attack method with smart move selection
    def enemy_attack(self):

        # Import type effectiveness table
        from config.constants import TYPE_EFFECTIVENESS

        # Initialize best move as first move
        best_move = self.enemy.moves[0]

        # Initialize best predicted damage as 0
        best_damage = 0

        # Loop through all enemy moves
        for move in self.enemy.moves:

            # Get type multiplier for this move
            multiplier = TYPE_EFFECTIVENESS.get((move.type, self.player.type), 1.0)

            # Predict base damage (without modifying actual HP)
            predicted_damage = (move.power + self.enemy.attack - self.player.defense) * multiplier

            # If predicted damage is higher than previous best
            if predicted_damage > best_damage:

                # Update best damage
                best_damage = predicted_damage

                # Update best move
                best_move = move

        # Log chosen move
        GameLogger.log(f"{self.enemy.name} selected {best_move.name} strategically")

        # Apply damage using best move
        self.apply_damage(self.enemy, self.player, best_move)

        # Apply damage with animation and effectiveness messages
    def apply_damage(self, attacker, defender, move):

        # Import settings manager
        from config.settings_manager import SettingsManager

        # Import animation utility
        from core.animation import type_text

        # Load settings
        settings = SettingsManager.load_settings()

        # Get difficulty
        difficulty = settings["difficulty"]

        # Get type effectiveness multiplier
        multiplier = TYPE_EFFECTIVENESS.get((move.type, defender.type), 1.0)

        # Calculate base damage
        base_damage = move.power + attacker.attack - defender.defense

        # Apply difficulty scaling if attacker is enemy
        if attacker == self.enemy:
            if difficulty == "Easy":
                base_damage *= 0.75
            elif difficulty == "Hard":
                base_damage *= 1.25

        # Calculate final damage
        damage = max(1, int(base_damage * multiplier))

        # Apply damage
        defender.hp -= damage

        # Prevent negative HP display
        if defender.hp < 0:
            defender.hp = 0

        # Animated attack message
        type_text(f"{attacker.name} used {move.name}!")

        # Show effectiveness messages
        if multiplier > 1:
            type_text("It's super effective!")
        elif multiplier < 1:
            type_text("It's not very effective...")

        # Random critical hit simulation
        import random
        if random.randint(1, 10) == 1:
            type_text("A critical hit!")
            damage = int(damage * 1.5)

        # Record damage for statistics
        StatsManager.record_damage(damage)

        # Print damage result
        type_text(f"Damage dealt: {damage}")

        # Display remaining HP
        type_text(f"{defender.name} HP: {defender.hp}/{defender.max_hp}")

    # End battle method
    def end_battle(self):

        # Import SaveLoadManager inside method
        from core.save_load import SaveLoadManager

        # Print battle end message
        print("\n--- BATTLE END ---")

        # Determine winner and update stats
        if self.trainer.get_next_pokemon():
            print(f"{self.trainer.name} wins!")

            # Record win
            StatsManager.record_battle(True)

            # Unlock First Victory achievement
            AchievementManager.unlock("First Victory")

        else:
            print(f"{self.opponent.name} wins!")

            # Record loss
            StatsManager.record_battle(False)

        # Save game after battle
        SaveLoadManager.save_game(self.trainer)

        # Reset HP for next battle
        for pokemon in self.trainer.team:
            pokemon.reset_hp()

        for pokemon in self.opponent.team:
            pokemon.reset_hp()
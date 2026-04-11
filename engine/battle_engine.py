import random
from systems.dialogue_manager import DialogueManager
from engine.json_loader import JSONLoader
from systems.type_chart import get_effectiveness

class BattleEngine:
    def __init__(self, player, opponent, moves_data=None):
        self.player = player
        self.opponent = opponent

        if moves_data:
            self.moves_data = {m["name"]: m for m in moves_data}
        else:
            # Fallback for backward compatibility
            self.loader = JSONLoader()
            self.moves_data = {m["name"]: m for m in self.loader.load("moves.json")}

        self.dialogue = DialogueManager(speed=0.005)

        self.player_pokemon = player.get_active_pokemon()
        self.opponent_pokemon = opponent.get_active_pokemon()

        # 🔥 FIX: store opponent level safely
        self.last_opponent_level = self.opponent_pokemon.level if self.opponent_pokemon else 5

    def start_battle(self):
        print(f"\n⚔️ Battle Start: {self.player.name} vs {self.opponent.name}\n")

        turn = 1

        while self.player.has_pokemon_left() and self.opponent.has_pokemon_left():
            print(f"\n--- Turn {turn} ---")

            self.player_turn()
            self.check_faint()

            if not self.opponent.has_pokemon_left():
                break

            self.opponent_turn()
            self.check_faint()

            if not self.player.has_pokemon_left():
                break

            turn += 1

        self.end_battle()

    # ----------------------------
    def player_turn(self):
        print(f"\nYour active Pokémon: {self.player_pokemon}")

        move_name = self.player_pokemon.choose_move()
        move = self.moves_data.get(move_name, {"power": 40, "type": "Normal"})

        effectiveness = get_effectiveness(move["type"], self.opponent_pokemon.type)

        damage = self.calculate_damage(
            self.player_pokemon,
            self.opponent_pokemon,
            move["power"],
            effectiveness
        )

        self.print_effectiveness(effectiveness)

        if self.player_pokemon.trigger_clutch():
            self.dialogue.speak(self.player.name, "Final move!")
            damage *= 1.5

        self.opponent_pokemon.take_damage(int(damage))

        print(f"{self.player_pokemon.name} used {move_name}!")
        print(f"Damage: {int(damage)}")
        print(self.opponent_pokemon)

    # ----------------------------
    def opponent_turn(self):
        if self.opponent_pokemon is None:
            return

        move_name = random.choice(self.opponent_pokemon.moves)
        move = self.moves_data.get(move_name, {"power": 40, "type": "Normal"})

        effectiveness = get_effectiveness(move["type"], self.player_pokemon.type)

        damage = self.calculate_damage(
            self.opponent_pokemon,
            self.player_pokemon,
            move["power"],
            effectiveness
        )

        self.print_effectiveness(effectiveness)

        if self.opponent_pokemon.trigger_clutch():
            self.dialogue.speak(self.opponent.name, "I won't lose!")
            damage *= 1.5

        self.player_pokemon.take_damage(int(damage))

        print(f"{self.opponent_pokemon.name} used {move_name}!")
        print(f"Damage: {int(damage)}")
        print(self.player_pokemon)

    # ----------------------------
    def check_faint(self):
        # Player faint
        if self.player_pokemon and not self.player_pokemon.is_alive():
            print(f"💀 {self.player_pokemon.name} fainted!")
            self.player_pokemon = self.player.switch_next()

        # Opponent faint
        if self.opponent_pokemon and not self.opponent_pokemon.is_alive():
            print(f"💀 {self.opponent_pokemon.name} fainted!")

            # 🔥 SAVE LAST LEVEL BEFORE REMOVING
            self.last_opponent_level = self.opponent_pokemon.level

            self.opponent_pokemon = self.opponent.switch_next()

    # ----------------------------
    def calculate_damage(self, attacker, defender, power, effectiveness):
        base = attacker.attack * attacker.get_attack_multiplier()
        return max(1, int((base * power / defender.defense) / 10 * effectiveness))

    # ----------------------------
    def print_effectiveness(self, value):
        if value > 1:
            print("🔥 It's super effective!")
        elif value < 1:
            print("🛡️ It's not very effective...")

    # ----------------------------
    def end_battle(self):
        print("\n⚔️ Battle End!")

        if self.player.has_pokemon_left():
            print(f"🏆 {self.player.name} wins!")

            # 🔥 SAFE EXP SYSTEM
            for p in self.player.team:
                if p.is_alive():
                    p.gain_exp(self.last_opponent_level)

        else:
            print(f"💀 {self.opponent.name} wins!")
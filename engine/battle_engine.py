import random
from systems.dialogue_manager import DialogueManager

class BattleEngine:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

        self.dialogue = DialogueManager(speed=0.005)

        self.player_pokemon = player.get_active_pokemon()
        self.opponent_pokemon = opponent.get_active_pokemon()

    def start_battle(self):
        print(f"\n⚔️ Battle Start: {self.player.name} vs {self.opponent.name}\n")

        self.dialogue.speak(self.player.name, "Let's win this battle!")
        self.dialogue.speak(self.opponent.name, "You don't stand a chance!")

        turn = 1

        while self.player_pokemon.is_alive() and self.opponent_pokemon.is_alive():
            print(f"\n--- Turn {turn} ---")

            self.player_turn()
            if not self.opponent_pokemon.is_alive():
                break

            self.opponent_turn()
            if not self.player_pokemon.is_alive():
                break

            turn += 1

        self.end_battle()

    # ----------------------------
    def player_turn(self):
        print(f"{self.player_pokemon.name}'s turn!")
        self.dialogue.speak(self.player.name, f"{self.player_pokemon.name}, attack!")

        damage = self.calculate_damage(self.player_pokemon, self.opponent_pokemon, self.player.personality, True)

        if self.player_pokemon.trigger_comeback():
            self.dialogue.speak(self.player.name, "Don't give up!")
            damage *= 1.2

        self.opponent_pokemon.take_damage(int(damage))

        print(f"{self.player_pokemon.name} dealt {int(damage)} damage!")
        print(self.opponent_pokemon)

    # ----------------------------
    def opponent_turn(self):
        print(f"{self.opponent_pokemon.name}'s turn!")
        self.dialogue.speak(self.opponent.name, f"{self.opponent_pokemon.name}, finish it!")

        damage = self.calculate_damage(self.opponent_pokemon, self.player_pokemon, self.opponent.personality)

        if self.opponent_pokemon.trigger_comeback():
            self.dialogue.speak(self.opponent.name, "I won't lose!")
            damage *= 1.2

        self.player_pokemon.take_damage(int(damage))

        print(f"{self.opponent_pokemon.name} dealt {int(damage)} damage!")
        print(self.player_pokemon)

    # ----------------------------
    def calculate_damage(self, attacker, defender, personality, is_player=False):
        base = attacker.attack * attacker.get_attack_multiplier()
        defense = defender.defense

        damage = (base / defense) * 10

        if personality == "aggressive":
            damage *= 1.15
        elif personality == "defensive":
            damage *= 0.9
        elif personality == "emotional":
            damage *= random.uniform(0.9, 1.2)

        if is_player:
            damage *= 1.1

        return max(1, int(damage))

    # ----------------------------
    def end_battle(self):
        print("\n⚔️ Battle End!")

        if self.player_pokemon.is_alive():
            self.dialogue.speak(self.player.name, "We did it!")
            print(f"🏆 {self.player.name} wins!")
        else:
            self.dialogue.speak(self.opponent.name, "Too easy!")
            print(f"💀 {self.opponent.name} wins!")
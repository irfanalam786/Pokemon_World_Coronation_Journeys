import random
from systems.dialogue_manager import DialogueManager
from systems.type_chart import get_effectiveness

class BattleEngine:
    def __init__(self, player, opponent, moves_data, inventory):
        self.player = player
        self.opponent = opponent
        self.inventory = inventory

        self.moves_data = {m["name"]: m for m in moves_data}

        self.dialogue = DialogueManager(speed=0.005)

        self.player_pokemon = player.get_active_pokemon()
        self.opponent_pokemon = opponent.get_active_pokemon()

        self.last_opponent_level = self.opponent_pokemon.level if self.opponent_pokemon else 5

    def start_battle(self):
        print(f"\n⚔️ Battle Start: {self.player.name} vs {self.opponent.name}\n")

        self.player_pokemon.show_image()
        self.opponent_pokemon.show_image()

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

            # 🔥 APPLY STATUS EFFECTS
            self.player_pokemon.process_status()
            self.opponent_pokemon.process_status()

            turn += 1

        self.end_battle()

    def player_turn(self):
        if self.player_pokemon.is_paralyzed():
            return

        print(f"\nYour Pokémon: {self.player_pokemon}")

        print("\nChoose action:")
        print("1. Attack")
        print("2. Switch")
        print("3. Use Item 🎒")

        choice = input("Enter choice: ")

        if choice == "2":
            self.player_pokemon = self.player.manual_switch()
            return

        if choice == "3":
            self.inventory.show_items()
            item_choice = int(input("Choose item: ")) - 1

            used = self.inventory.use_item(item_choice, self.player_pokemon)
            if used:
                return

        move_name = self.player_pokemon.choose_move()
        move = self.moves_data.get(move_name, {"power": 40, "type": "Normal"})

        self.player_pokemon.sound.play_attack()

        effectiveness = get_effectiveness(move["type"], self.opponent_pokemon.type)

        damage = self.calculate_damage(
            self.player_pokemon,
            self.opponent_pokemon,
            move["power"],
            effectiveness
        )

        # 🔥 APPLY STATUS
        if "status" in move and random.random() < move.get("chance", 0):
            self.opponent_pokemon.apply_status(move["status"])

        self.print_effectiveness(effectiveness)

        if self.player_pokemon.trigger_clutch():
            self.dialogue.speak(self.player.name, "Final move!")
            damage *= 1.5

        self.opponent_pokemon.take_damage(int(damage))

        print(f"{self.player_pokemon.name} used {move_name}!")
        print(f"Damage: {int(damage)}")
        print(self.opponent_pokemon)

    def opponent_turn(self):
        if self.opponent_pokemon is None or self.opponent_pokemon.is_paralyzed():
            return

        move_name = random.choice(self.opponent_pokemon.moves)
        move = self.moves_data.get(move_name, {"power": 40, "type": "Normal"})

        self.opponent_pokemon.sound.play_attack()

        effectiveness = get_effectiveness(move["type"], self.player_pokemon.type)

        damage = self.calculate_damage(
            self.opponent_pokemon,
            self.player_pokemon,
            move["power"],
            effectiveness
        )

        if "status" in move and random.random() < move.get("chance", 0):
            self.player_pokemon.apply_status(move["status"])

        self.print_effectiveness(effectiveness)

        if self.opponent_pokemon.trigger_clutch():
            self.dialogue.speak(self.opponent.name, "I won't lose!")
            damage *= 1.5

        self.player_pokemon.take_damage(int(damage))

        print(f"{self.opponent_pokemon.name} used {move_name}!")
        print(f"Damage: {int(damage)}")
        print(self.player_pokemon)

    def check_faint(self):
        if self.player_pokemon and not self.player_pokemon.is_alive():
            print(f"💀 {self.player_pokemon.name} fainted!")
            self.player_pokemon = self.player.switch_next()

        if self.opponent_pokemon and not self.opponent_pokemon.is_alive():
            print(f"💀 {self.opponent_pokemon.name} fainted!")
            self.last_opponent_level = self.opponent_pokemon.level
            self.opponent_pokemon = self.opponent.switch_next()

    def calculate_damage(self, attacker, defender, power, effectiveness):
        base = attacker.attack * attacker.get_attack_multiplier()
        return max(1, int((base * power / defender.defense) / 10 * effectiveness))

    def print_effectiveness(self, value):
        if value > 1:
            print("🔥 It's super effective!")
        elif value < 1:
            print("🛡️ It's not very effective...")

    def end_battle(self):
        print("\n⚔️ Battle End!")

        if self.player.has_pokemon_left():
            print(f"🏆 {self.player.name} wins!")

            for p in self.player.team:
                if p.is_alive():
                    p.gain_exp(self.last_opponent_level)

        else:
            print(f"💀 {self.opponent.name} wins!")
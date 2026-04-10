class BattleEngine:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

        self.player_pokemon = player.get_active_pokemon()
        self.opponent_pokemon = opponent.get_active_pokemon()

    def start_battle(self):
        print(f"\n⚔️ Battle Start: {self.player.name} vs {self.opponent.name}\n")

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
    # PLAYER TURN
    # ----------------------------
    def player_turn(self):
        print(f"{self.player_pokemon.name}'s turn!")

        damage = self.calculate_damage(self.player_pokemon, self.opponent_pokemon)
        self.opponent_pokemon.take_damage(damage)

        print(f"{self.player_pokemon.name} dealt {damage} damage!")
        print(self.opponent_pokemon)

    # ----------------------------
    # OPPONENT TURN (SCRIPT LOGIC)
    # ----------------------------
    def opponent_turn(self):
        print(f"{self.opponent_pokemon.name}'s turn!")

        damage = self.calculate_damage(self.opponent_pokemon, self.player_pokemon)
        self.player_pokemon.take_damage(damage)

        print(f"{self.opponent_pokemon.name} dealt {damage} damage!")
        print(self.player_pokemon)

    # ----------------------------
    # DAMAGE CALCULATION
    # ----------------------------
    def calculate_damage(self, attacker, defender):
        base = attacker.attack
        defense = defender.defense

        damage = int((base / defense) * 10)

        if damage < 1:
            damage = 1

        return damage

    # ----------------------------
    # END BATTLE
    # ----------------------------
    def end_battle(self):
        print("\n⚔️ Battle End!")

        if self.player_pokemon.is_alive():
            print(f"🏆 {self.player.name} wins!")
        else:
            print(f"💀 {self.opponent.name} wins!")
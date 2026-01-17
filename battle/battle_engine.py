from config.constants import TYPE_EFFECTIVENESS

class BattleEngine:
    def __init__(self, trainer, opponent):
        self.trainer = trainer
        self.opponent = opponent
        self.player_pokemon = trainer.team[0]
        self.enemy_pokemon = opponent.team[0]

    def start_battle(self):
        print("\n--- BATTLE START ---")
        print(f"{self.player_pokemon.name} vs {self.enemy_pokemon.name}")

        while not self.player_pokemon.is_fainted() and not self.enemy_pokemon.is_fainted():
            self.execute_turn()

        self.end_battle()

    def execute_turn(self):
        if self.player_pokemon.speed >= self.enemy_pokemon.speed:
            self.attack(self.player_pokemon, self.enemy_pokemon)
            if not self.enemy_pokemon.is_fainted():
                self.attack(self.enemy_pokemon, self.player_pokemon)
        else:
            self.attack(self.enemy_pokemon, self.player_pokemon)
            if not self.player_pokemon.is_fainted():
                self.attack(self.player_pokemon, self.enemy_pokemon)

    def attack(self, attacker, defender):
        move = attacker.moves[0]

        multiplier = TYPE_EFFECTIVENESS.get(
            (move.type, defender.type), 1.0
        )

        base_damage = max(1, move.power + attacker.attack - defender.defense)
        damage = int(base_damage * multiplier)

        defender.hp -= damage

        print(
            f"{attacker.name} used {move.name}! "
            f"Damage: {damage} (x{multiplier})"
        )

    def end_battle(self):
        print("\n--- BATTLE END ---")
        if not self.player_pokemon.is_fainted():
            print(f"{self.trainer.name} wins!")
        else:
            print(f"{self.opponent.name} wins!")

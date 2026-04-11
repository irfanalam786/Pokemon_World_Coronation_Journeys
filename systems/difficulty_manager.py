class DifficultyManager:
    def __init__(self):
        self.level = 1  # story progression

    def increase_difficulty(self):
        self.level += 1
        print(f"\n📈 Difficulty increased to {self.level}!")

    def get_multiplier(self):
        if self.level <= 2:
            return 0.9  # easy
        elif self.level <= 4:
            return 1.0  # normal
        else:
            return 1.2  # hard

    def adjust_pokemon(self, pokemon):
        multiplier = self.get_multiplier()

        pokemon.attack = int(pokemon.attack * multiplier)
        pokemon.defense = int(pokemon.defense * multiplier)
        pokemon.max_hp = int(pokemon.max_hp * multiplier)
        pokemon.hp = pokemon.max_hp
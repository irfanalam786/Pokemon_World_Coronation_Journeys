def start(self):
    print("🎮 Game Started\n")

    # Take first Pokémon
    pokemon = self.pokemon_objects[0]

    print("Before EXP:")
    print(pokemon)

    # Simulate battle EXP
    base_exp = 10
    opponent_level = 5

    exp_gain = base_exp * opponent_level

    print("\n--- Battle Finished ---")
    pokemon.gain_exp(exp_gain)

    print("\nAfter EXP:")
    print(pokemon)
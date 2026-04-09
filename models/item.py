class Item:
    def __init__(self, data):
        self.name = data.get("name")
        self.type = data.get("type")
        self.value = data.get("value")
        self.restricted = data.get("restricted", False)

    def use(self, pokemon):
        print(f"\nUsing {self.name} on {pokemon.name}")

        if self.type == "heal":
            pokemon.heal(self.value)
            print(f"{pokemon.name} healed by {self.value} HP!")

        elif self.type == "level_up":
            return self.use_rare_candy(pokemon)

    def use_rare_candy(self, pokemon):
        # Check level cap
        if pokemon.level >= pokemon.level_cap:
            print(f"⚠️ Cannot use Rare Candy! {pokemon.name} reached level cap ({pokemon.level_cap})")
            return False

        # Apply level up
        pokemon.level += 1
        pokemon.increase_stats()

        print(f"🍬 {pokemon.name} leveled up instantly to {pokemon.level}!")
        return True

    def __str__(self):
        return f"{self.name} ({self.type})"
# Trainer base class
class Trainer:
    def __init__(self, name, age):
        # Store trainer name
        self.name = name
        # Store trainer age
        self.age = age
        # List to store Pokémon
        self.team = []
        # Initial World Coronation rank
        self.rank = "Normal Class"

    # Add Pokémon to team
    def add_pokemon(self, pokemon):
        self.team.append(pokemon)

    # Display trainer's Pokémon
    def show_team(self):
        for p in self.team:
            print(p.name)

    # Promote trainer rank
    def promote_rank(self):
        if self.rank == "Normal Class":
            self.rank = "Great Class"
        elif self.rank == "Great Class":
            self.rank = "Ultra Class"
        elif self.rank == "Ultra Class":
            self.rank = "Master Class"

    # Get next available Pokémon
    def get_next_pokemon(self):
        for pokemon in self.team:
            if not pokemon.is_fainted():
                return pokemon
        return None

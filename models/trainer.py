from models.pokemon import Pokemon

class Trainer:
    def __init__(self, data, pokemon_data):
        self.name = data.get("name")
        self.personality = data.get("personality")
        self.team_names = data.get("team", [])

        # Convert Pokémon names → actual objects
        self.team = self.build_team(pokemon_data)

        # Future systems
        self.memory = {}
        self.bond_with_player = 0

    def build_team(self, pokemon_data):
        team = []
        for name in self.team_names:
            for p in pokemon_data:
                if p["name"] == name:
                    team.append(Pokemon(p))
        return team

    def get_active_pokemon(self):
        for p in self.team:
            if p.is_alive():
                return p
        return None

    def __str__(self):
        return f"{self.name} ({self.personality})"
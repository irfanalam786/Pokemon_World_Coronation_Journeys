from models.pokemon import Pokemon

class Trainer:
    def __init__(self, data, pokemon_data):
        self.name = data.get("name")
        self.personality = data.get("personality")
        self.team_names = data.get("team", [])

        self.team = self.build_team(pokemon_data)
        self.active_index = 0

    def build_team(self, pokemon_data):
        team = []
        for name in self.team_names:
            for p in pokemon_data:
                if p["name"] == name:
                    team.append(Pokemon(p))
        return team

    def get_active_pokemon(self):
        if self.active_index < len(self.team):
            return self.team[self.active_index]
        return None

    # ----------------------------
    # 🔄 MANUAL SWITCH
    # ----------------------------
    def manual_switch(self):
        print("\nChoose Pokémon:")

        for i, p in enumerate(self.team):
            status = " (Fainted)" if not p.is_alive() else ""
            print(f"{i + 1}. {p.name} {status}")

        choice = int(input("Enter choice: ")) - 1

        if 0 <= choice < len(self.team) and self.team[choice].is_alive():
            self.active_index = choice
            print(f"\n🔄 {self.name} switched to {self.team[choice].name}!")
            return self.team[choice]

        print("❌ Invalid choice!")
        return self.get_active_pokemon()

    def switch_next(self):
        for i, p in enumerate(self.team):
            if p.is_alive():
                self.active_index = i
                print(f"\n🔄 {self.name} sends out {p.name}!")
                return p
        return None

    def has_pokemon_left(self):
        return any(p.is_alive() for p in self.team)
from models.pokemon import Pokemon

class Trainer:
    def __init__(self, data, pokemon_data):
        self.name = data["name"]
        self.type = data.get("type", "normal")
        self.badge = data.get("badge")

        self.team = []
        self.active_index = 0

        for pname in data["team"]:
            for p in pokemon_data:
                if p["name"] == pname:
                    self.team.append(Pokemon(p))

    def get_active_pokemon(self):
        if self.active_index < len(self.team):
            return self.team[self.active_index]
        return None

    def switch_next(self):
        for i, p in enumerate(self.team):
            if p.is_alive():
                self.active_index = i
                return p
        return None

    def has_pokemon_left(self):
        return any(p.is_alive() for p in self.team)

    # 🔥 BOSS BOOST
    def apply_gym_boost(self):
        if self.type == "gym":
            for p in self.team:
                p.max_hp += 20
                p.attack += 5
                p.defense += 5
                p.hp = p.max_hp
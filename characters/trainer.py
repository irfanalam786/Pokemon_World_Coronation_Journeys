class Trainer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.team = []
        self.rank = "Normal Class"

    def add_pokemon(self, pokemon):
        self.team.append(pokemon)

    def show_team(self):
        for p in self.team:
            print(p.name)

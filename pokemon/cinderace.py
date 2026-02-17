from pokemon.pokemon import Pokemon
from battle.move import Move

class Cinderace(Pokemon):
    def __init__(self):
        super().__init__("Cinderace", 80, 116, 75, 119, "Fire")
        self.add_move(Move("Ember", 40, "Fire"))
        self.add_move(Move("Quick Attack", 30, "Normal"))

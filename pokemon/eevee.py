from pokemon.pokemon import Pokemon
from battle.move import Move

class Eevee(Pokemon):
    def __init__(self):
        super().__init__("Eevee", 55, 55, 50, 55, "Normal")
        self.add_move(Move("Tackle", 40, "Normal"))
        self.add_move(Move("Quick Attack", 30, "Normal"))

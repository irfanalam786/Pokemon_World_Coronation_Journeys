from pokemon.pokemon import Pokemon
from battle.move import Move

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 35, 55, 40, 90, "Electric")
        self.add_move(Move("Thunder Shock", 40, "Electric"))
        self.add_move(Move("Quick Attack", 30, "Normal"))

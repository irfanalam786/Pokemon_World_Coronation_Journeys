from pokemon.pokemon import Pokemon
from battle.move import Move

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(
            name="Pikachu",
            hp=35,
            attack=55,
            defense=40,
            speed=90,
            p_type="Electric"
        )

        self.add_move(Move("Thunder Shock", 40, "Electric"))

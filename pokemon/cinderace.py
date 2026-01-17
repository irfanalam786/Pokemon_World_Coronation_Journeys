from pokemon.pokemon import Pokemon
from battle.move import Move

class Cinderace(Pokemon):
    def __init__(self):
        super().__init__(
            name="Cinderace",
            hp=80,
            attack=116,
            defense=75,
            speed=119,
            p_type="Fire"
        )

        self.add_move(Move("Ember", 40, "Fire"))

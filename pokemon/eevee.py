from pokemon.pokemon import Pokemon
from battle.move import Move

class Eevee(Pokemon):
    def __init__(self):
        super().__init__(
            name="Eevee",
            hp=55,
            attack=55,
            defense=50,
            speed=55,
            p_type="Normal"
        )

        self.add_move(Move("Tackle", 40, "Normal"))

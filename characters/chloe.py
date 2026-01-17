from characters.trainer import Trainer
from pokemon.eevee import Eevee

class Chloe(Trainer):
    def __init__(self):
        super().__init__("Chloe", 10)
        self.add_pokemon(Eevee())
        # You can add more Pokemon to Chloe's team here
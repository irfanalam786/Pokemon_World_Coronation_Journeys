from characters.trainer import Trainer
from pokemon.eevee import Eevee

class Chloe(Trainer):
    def __init__(self):
        super().__init__("Chloe Cerise", 10)
        self.add_pokemon(Eevee())

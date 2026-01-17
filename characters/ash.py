from characters.trainer import Trainer
from pokemon.pikachu import Pikachu

class Ash(Trainer):
    def __init__(self):
        super().__init__("Ash Ketchum", 10)
        self.add_pokemon(Pikachu())
        # You can add more Pokemon to Ash's team here
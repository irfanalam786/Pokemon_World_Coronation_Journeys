from characters.trainer import Trainer
from pokemon.cinderace import Cinderace

class Goh(Trainer):
    def __init__(self):
        super().__init__("Goh", 10)
        self.add_pokemon(Cinderace())
        # You can add more Pokemon to Goh's team here
# Import base trainer
from characters.trainer import Trainer
# Import Pikachu
from pokemon.pikachu import Pikachu

# Ash Ketchum class
class Ash(Trainer):
    def __init__(self):
        # Call parent constructor
        super().__init__("Ash Ketchum", 10)
        # Add Pikachu to team
        self.add_pokemon(Pikachu())

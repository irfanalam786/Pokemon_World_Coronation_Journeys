# ==============================
# File: champions.py
# Purpose: Defines Masters Eight Champion trainers
# ==============================

from characters.trainer import Trainer
from pokemon.pokemon import Pokemon
from battle.move import Move

class StevenStone(Trainer):
    """
    Hoenn Champion – Steel specialist
    """
    def __init__(self):
        super().__init__("Steven Stone", 30)

        metagross = Pokemon("Metagross", 150, 135, 130, 70, "Steel")
        metagross.add_move(Move("Meteor Mash", 90, "Steel"))

        self.add_pokemon(metagross)


class Cynthia(Trainer):
    """
    Sinnoh Champion – Balanced powerhouse
    """
    def __init__(self):
        super().__init__("Cynthia", 32)

        garchomp = Pokemon("Garchomp", 160, 140, 120, 102, "Dragon")
        garchomp.add_move(Move("Dragon Claw", 80, "Dragon"))

        self.add_pokemon(garchomp)


class Leon(Trainer):
    """
    World Champion – Final Boss
    """
    def __init__(self):
        super().__init__("Leon", 28)

        charizard = Pokemon("Charizard", 180, 150, 130, 120, "Fire")
        charizard.add_move(Move("G-Max Wildfire", 100, "Fire"))

        self.add_pokemon(charizard)

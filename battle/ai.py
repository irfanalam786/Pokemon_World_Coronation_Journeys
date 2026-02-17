# ==============================
# File: ai.py
# Purpose: AI Trainer logic
# ==============================

from characters.trainer import Trainer
from pokemon.pokemon import Pokemon
from battle.move import Move

class AITrainer(Trainer):
    def __init__(self):
        super().__init__("Normal Class Trainer", 18)

        pokemon = Pokemon("Rookidee", 40, 45, 35, 60, "Flying")
        pokemon.add_move(Move("Peck", 35, "Flying"))

        self.add_pokemon(pokemon)

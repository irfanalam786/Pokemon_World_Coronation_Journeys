# ==============================
# File: opponent_factory.py
# Purpose: Creates opponents including champions
# ==============================

from characters.trainer import Trainer
from pokemon.pokemon import Pokemon
from battle.move import Move
from battle.champions import StevenStone, Cynthia, Leon

class OpponentFactory:
    @staticmethod
    def create_opponent(rank, stage=0):
        """
        Creates AI opponent based on rank and stage
        """
        # Masters Eight logic
        if rank == "Master Class":
            if stage == 0:
                return StevenStone()
            elif stage == 1:
                return Cynthia()
            else:
                return Leon()

        # Pre-Master opponents
        opponent = Trainer("World Trainer", 18)

        if rank == "Normal Class":
            p = Pokemon("Rookidee", 40, 45, 35, 60, "Flying")
            p.add_move(Move("Peck", 35, "Flying"))
            opponent.add_pokemon(p)

        elif rank == "Great Class":
            p = Pokemon("Corvisquire", 60, 60, 55, 75, "Flying")
            p.add_move(Move("Drill Peck", 45, "Flying"))
            opponent.add_pokemon(p)

        elif rank == "Ultra Class":
            p = Pokemon("Corviknight", 90, 85, 85, 70, "Steel")
            p.add_move(Move("Steel Wing", 60, "Steel"))
            opponent.add_pokemon(p)

        return opponent

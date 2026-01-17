from characters.trainer import Trainer
from pokemon.pokemon import Pokemon
from battle.move import Move

class AITrainer(Trainer):
    def __init__(self, name="Normal Class Trainer"):
        super().__init__(name, age=18)

        pokemon = Pokemon(
            name="Rookidee",
            hp=40,
            attack=45,
            defense=35,
            speed=60,
            p_type="Flying"
        )

        pokemon.add_move(Move("Peck", 35, "Flying"))
        self.add_pokemon(pokemon)

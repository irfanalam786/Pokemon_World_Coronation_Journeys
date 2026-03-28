# ranking/rank_system.py

class RankSystem:
    def __init__(self):
        self.ranks = ["Normal", "Great", "Ultra", "Master"]

        self.level_caps = {
            "Normal": 20,
            "Great": 40,
            "Ultra": 70,
            "Master": 100
        }

    def get_level_cap(self, trainer):
        return self.level_caps.get(trainer.get_rank(), 20)

    def update_points(self, winner, loser):
        winner.set_points(winner.get_points() + 20)
        loser.set_points(max(0, loser.get_points() - 10))

        print(f"{winner.get_name()} +20 points")
        print(f"{loser.get_name()} -10 points")

    def update_rank(self, trainer):
        points = trainer.get_points()

        if points >= 200:
            trainer.set_rank("Master")
        elif points >= 150:
            trainer.set_rank("Ultra")
        elif points >= 100:
            trainer.set_rank("Great")
        else:
            trainer.set_rank("Normal")
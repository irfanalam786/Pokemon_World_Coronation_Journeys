# models/trainer.py

from progression.stats_system import StatsSystem
from progression.achievement_system import AchievementSystem


class Trainer:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__money = 1000
        self.__rank = "Normal"
        self.__points = 0

        self.stats = StatsSystem()
        self.achievements = AchievementSystem()

    # ✅ CORRECT: method outside __init__
    def add_points(self, amount):
        self.__points += amount

    def get_name(self): return self.__name
    def get_team(self): return self.__team
    def get_rank(self): return self.__rank
    def get_points(self): return self.__points

    def set_points(self, pts): self.__points = pts
    def set_rank(self, rank): self.__rank = rank

    def add_pokemon(self, pokemon):
        if len(self.__team) < 6:
            self.__team.append(pokemon)

    def get_active_pokemon(self):
        for p in self.__team:
            if not p.is_fainted():
                return p
        return None

    def reset_team(self):
        for p in self.__team:
            p.heal_full()

    def switch_pokemon(self, index):
        if index < 0 or index >= len(self.__team):
            print("Invalid choice!")
            return None

        selected = self.__team[index]

        if selected.is_fainted():
            print("Cannot switch to fainted Pokémon!")
            return None

        self.__team.insert(0, self.__team.pop(index))
        print(f"{self.__name} switched to {selected.get_name()}!")
        return selected

    def __str__(self):
        names = [p.get_name() for p in self.__team]
        return f"{self.__name} | Team: {names} | Rank: {self.__rank} | Points: {self.__points}"
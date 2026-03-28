# models/pokemon.py

import random


class Pokemon:
    def __init__(self, name, hp, attack, defense, speed, p_type, role="balanced"):
        self.__name = name
        self.__type = p_type
        self.__role = role

        self.__base_hp = hp
        self.__base_attack = attack
        self.__base_defense = defense
        self.__base_speed = speed

        # IVs
        self.__iv_hp = random.randint(0, 10)
        self.__iv_attack = random.randint(0, 10)
        self.__iv_defense = random.randint(0, 10)
        self.__iv_speed = random.randint(0, 10)

        self.__level = 1
        self.__exp = 0

        # Status
        self.__status = None
        self.__poison_counter = 0

        # Evolution
        self.__evolution_map = {
            "Pikachu": ("Raichu", 120, 90, 70, 110, "Electric", 16),
            "Charmander": ("Charmeleon", 130, 80, 65, 80, "Fire", 16),
        }

        self.recalculate_stats()

    # ---------------- GETTERS ----------------
    def get_name(self): return self.__name
    def get_type(self): return self.__type
    def get_role(self): return self.__role
    def get_hp(self): return self.__hp
    def get_attack(self): return self.__attack
    def get_defense(self): return self.__defense
    def get_speed(self): return self.__speed
    def get_status(self): return self.__status
    def get_level(self): return self.__level
    def get_exp(self): return self.__exp

    # ---------------- STATUS ----------------
    def apply_status(self, status):
        if self.__status is None:
            self.__status = status
            print(f"{self.__name} is now {status}!")

    def process_status(self):
        if self.is_fainted():
            return False

        if self.__status == "burn":
            damage = int(self.__max_hp * 0.05)
            self.take_damage(damage)
            print(f"{self.__name} is hurt by burn! (-{damage} HP)")

        elif self.__status == "poison":
            self.__poison_counter += 1
            damage = int(self.__max_hp * 0.03 * self.__poison_counter)
            self.take_damage(damage)
            print(f"{self.__name} is hurt by poison! (-{damage} HP)")

        elif self.__status == "paralysis":
            if random.random() < 0.25:
                print(f"{self.__name} is paralyzed and can't move!")
                return False

        return True

    # ---------------- EXP ----------------
    def exp_needed(self):
        return int(50 * (self.__level ** 1.5))

    def gain_exp(self, amount):
        print(f"{self.__name} gained {amount} EXP!")
        self.__exp += amount

        while self.__exp >= self.exp_needed():
            self.__exp -= self.exp_needed()
            self.level_up()

    def level_up(self):
        self.__level += 1
        print(f"{self.__name} leveled up to Level {self.__level}!")
        self.check_evolution()
        self.recalculate_stats()

    # ---------------- EVOLUTION ----------------
    def check_evolution(self):
        if self.__name in self.__evolution_map:
            evo = self.__evolution_map[self.__name]
            if self.__level >= evo[6]:
                self.evolve(*evo[:-1])

    def evolve(self, new_name, hp, atk, defn, spd, new_type):
        print(f"{self.__name} evolved into {new_name}!")
        self.__name = new_name
        self.__type = new_type
        self.__base_hp = hp
        self.__base_attack = atk
        self.__base_defense = defn
        self.__base_speed = spd

    # ---------------- LEVEL ----------------
    def set_level(self, level):
        self.__level = max(1, min(100, level))
        self.__exp = 0
        self.check_evolution()
        self.recalculate_stats()

    # ---------------- STATS ----------------
    def recalculate_stats(self):
        hp = (self.__base_hp + self.__iv_hp)
        atk = (self.__base_attack + self.__iv_attack)
        defn = (self.__base_defense + self.__iv_defense)
        spd = (self.__base_speed + self.__iv_speed)

        if self.__role == "attacker":
            atk *= 1.2
        elif self.__role == "tank":
            defn *= 1.3
            hp *= 1.2
        elif self.__role == "speed":
            spd *= 1.3
        elif self.__role == "support":
            hp *= 1.1
            defn *= 1.1

        self.__max_hp = int(hp * (1 + 0.1 * self.__level))
        self.__attack = int(atk * (1 + 0.1 * self.__level))
        self.__defense = int(defn * (1 + 0.1 * self.__level))
        self.__speed = int(spd * (1 + 0.1 * self.__level))

        self.__hp = self.__max_hp

    # ---------------- HP SYSTEM FIX ----------------
    def set_hp(self, value):
        # Clamp HP between 0 and max
        self.__hp = max(0, min(self.__max_hp, value))

    def take_damage(self, dmg):
        if self.is_fainted():
            return
        self.set_hp(self.__hp - dmg)

    def heal_full(self):
        self.__hp = self.__max_hp
        self.__status = None
        self.__poison_counter = 0

    def is_fainted(self):
        return self.__hp <= 0

    def __str__(self):
        return f"{self.__name} | LVL: {self.__level} | HP: {self.__hp}/{self.__max_hp} | Status: {self.__status}"
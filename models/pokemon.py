class Pokemon:
    def __init__(self, data):
        self.name = data.get("name")
        self.type = data.get("type")
        self.role = data.get("role", "attacker")

        self.max_hp = data.get("hp")
        self.hp = self.max_hp
        self.attack = data.get("attack")
        self.defense = data.get("defense")

        self.level = data.get("level", 5)
        self.exp = 0

        self.moves = data.get("moves", [])

        # 🧬 Evolution data
        self.evolution = data.get("evolution")

        self.bond = 50
        self.clutch_used = False
        self.survival_used = False

    # ----------------------------
    # EXP SYSTEM
    # ----------------------------
    def gain_exp(self, opponent_level):
        # 🔥 EXP based on opponent strength
        exp_gain = 20 + (opponent_level * 10)

        print(f"✨ {self.name} gained {exp_gain} EXP!")
        self.exp += exp_gain

        while self.exp >= self.exp_to_next_level():
            self.exp -= self.exp_to_next_level()
            self.level_up()


    def exp_to_next_level(self):
        # 🔥 Different EXP requirements for each level
        # This creates a more natural level progression like Ash Gray.
        level_requirements = {
            1: 20,
            2: 25,
            3: 30,
            4: 35,
            5: 40,
            6: 50,
            7: 60,
            8: 70,
            9: 80,
            10: 95,
            11: 110,
            12: 125,
            13: 145,
            14: 165,
            15: 190,
            16: 215,
            17: 245,
            18: 275,
            19: 310,
            20: 350,
            21: 395,
            22: 445,
            23: 500,
            24: 565,
            25: 635,
            26: 710,
            27: 790,
            28: 875,
            29: 965,
            30: 1060,
        }
        return level_requirements.get(
            self.level,
            int(1060 + ((self.level - 30) * 125))
        )

    def level_up(self):
        self.level += 1

        print(f"🔥 {self.name} leveled up to {self.level}!")

        # Stat growth
        self.max_hp += 5
        self.attack += 2
        self.defense += 2
        self.hp = self.max_hp

        # 🔥 FORCE EVOLUTION CHECK (IMPORTANT)
        self.check_evolution()

    # ----------------------------
    # EVOLUTION SYSTEM
    # ----------------------------
    def check_evolution(self):
        if not self.evolution:
            return

        evo_level = self.evolution.get("level")

        # 🔥 STRICT CHECK
        if self.level >= evo_level:
            print(f"\n✨ {self.name} is evolving...")

            old_name = self.name

            self.name = self.evolution["name"]
            self.max_hp = self.evolution["hp"]
            self.attack = self.evolution["attack"]
            self.defense = self.evolution["defense"]

            self.hp = self.max_hp

            print(f"🧬 {old_name} evolved into {self.name}!")

            # 🔥 REMOVE EVOLUTION (prevent repeat)
            self.evolution = None

    # ----------------------------
    def choose_move(self):
        print("\nChoose move:")
        for i, move in enumerate(self.moves):
            print(f"{i + 1}. {move}")

        choice = int(input("Enter move: ")) - 1

        if 0 <= choice < len(self.moves):
            return self.moves[choice]

        return self.moves[0]

    def is_low_hp(self):
        return self.hp <= (0.3 * self.max_hp)

    def trigger_clutch(self):
        if not self.clutch_used and self.is_low_hp():
            self.clutch_used = True
            print(f"💥 {self.name} enters CLUTCH MODE!")
            return True
        return False

    def get_attack_multiplier(self):
        multiplier = 1.0

        if self.bond >= 70:
            multiplier *= 1.3
        elif self.bond >= 30:
            multiplier *= 1.1

        return multiplier

    def take_damage(self, damage):
        if damage >= self.hp and self.bond >= 70 and not self.survival_used:
            self.survival_used = True
            self.hp = 1
            print(f"💖 {self.name} survived!")
            return

        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def increase_bond(self, amount):
        self.bond = min(100, self.bond + amount)

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} Lv:{self.level} HP:{self.hp}/{self.max_hp}"
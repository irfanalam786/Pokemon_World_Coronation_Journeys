class Pokemon:
    def __init__(self, data):
        # Base data
        self.name = data.get("name")
        self.type = data.get("type")

        # Stats
        self.max_hp = data.get("hp")
        self.hp = self.max_hp
        self.attack = data.get("attack")
        self.defense = data.get("defense")
        self.speed = data.get("speed")

        # Progression
        self.level = data.get("level", 1)
        self.exp = 0

        # Future systems
        self.bond = 0
        self.status = None

    # ----------------------------
    # EXP SYSTEM
    # ----------------------------

    def gain_exp(self, amount):
        print(f"{self.name} gained {amount} EXP!")
        self.exp += amount

        # Check level up
        while self.exp >= self.exp_to_next_level():
            self.level_up()

    def exp_to_next_level(self):
        # Balanced curve
        return int(50 * (self.level ** 1.5))

    def level_up(self):
        self.exp -= self.exp_to_next_level()
        self.level += 1

        print(f"🔥 {self.name} leveled up to {self.level}!")

        self.increase_stats()

    def increase_stats(self):
        # Simple scaling (will improve later)
        self.max_hp += 5
        self.attack += 2
        self.defense += 2
        self.speed += 1

        # Heal on level up
        self.hp = self.max_hp

    # ----------------------------
    # BASIC METHODS
    # ----------------------------

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def __str__(self):
        return f"{self.name} (Lv {self.level}) EXP: {self.exp} HP: {self.hp}/{self.max_hp}"
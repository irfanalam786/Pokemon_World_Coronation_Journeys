class Pokemon:
    def __init__(self, data):
        self.name = data.get("name")
        self.type = data.get("type")

        self.max_hp = data.get("hp")
        self.hp = self.max_hp
        self.attack = data.get("attack")
        self.defense = data.get("defense")
        self.speed = data.get("speed")

        self.level = data.get("level", 1)
        self.exp = 0

        self.level_cap = 10

        # 🔥 NEW: Event flags
        self.comeback_used = False

        # Future systems
        self.bond = 0
        self.status = None

    # ----------------------------
    # EXP SYSTEM
    # ----------------------------

    def gain_exp(self, amount):
        print(f"{self.name} gained {amount} EXP!")
        self.exp += amount

        while self.exp >= self.exp_to_next_level():
            if self.level >= self.level_cap:
                print(f"⚠️ {self.name} reached level cap ({self.level_cap})!")
                self.exp = self.exp_to_next_level() - 1
                break

            self.level_up()

    def exp_to_next_level(self):
        return int(50 * (self.level ** 1.5))

    def level_up(self):
        self.exp -= self.exp_to_next_level()
        self.level += 1

        print(f"🔥 {self.name} leveled up to {self.level}!")
        self.increase_stats()

    def increase_stats(self):
        self.max_hp += 5
        self.attack += 2
        self.defense += 2
        self.speed += 1
        self.hp = self.max_hp

    # ----------------------------
    # DAMAGE + EVENTS
    # ----------------------------

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

    def is_low_hp(self):
        return self.hp <= (0.3 * self.max_hp)

    def trigger_comeback(self):
        if not self.comeback_used and self.is_low_hp():
            self.comeback_used = True
            print(f"🔥 {self.name} refuses to give up! (COMEBACK TRIGGERED)")
            return True
        return False

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def __str__(self):
        return f"{self.name} (Lv {self.level}) EXP: {self.exp}/{self.exp_to_next_level()} HP: {self.hp}/{self.max_hp}"
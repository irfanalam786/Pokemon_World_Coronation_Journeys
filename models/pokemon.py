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
        self.signature_move = data.get("signature_move")

        # ❤️ Bond system
        self.bond = 50

        # Emotion system
        self.comeback_used = False
        self.rage_active = False
        self.survival_used = False

    # ----------------------------
    # DAMAGE + SYSTEMS
    # ----------------------------
    def take_damage(self, damage):
        # Bond survival
        if damage >= self.hp:
            if self.bond >= 70 and not self.survival_used:
                self.survival_used = True
                self.hp = 1
                print(f"💖 {self.name} endured the hit because of strong bond!")
                return

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        # Rage trigger
        if self.is_low_hp() and not self.rage_active:
            self.rage_active = True
            print(f"😡 {self.name} entered RAGE MODE!")

    def is_low_hp(self):
        return self.hp <= (0.3 * self.max_hp)

    def trigger_comeback(self):
        if not self.comeback_used and self.is_low_hp():
            self.comeback_used = True
            print(f"🔥 {self.name} refuses to give up!")
            return True
        return False

    def increase_bond(self, amount):
        self.bond += amount
        if self.bond > 100:
            self.bond = 100

    def get_attack_multiplier(self):
        multiplier = 1.0

        if self.rage_active:
            multiplier *= 1.2

        if self.bond >= 70:
            multiplier *= 1.3
        elif self.bond >= 30:
            multiplier *= 1.1

        return multiplier

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (Lv {self.level}) HP: {self.hp}/{self.max_hp} Bond: {self.bond}"
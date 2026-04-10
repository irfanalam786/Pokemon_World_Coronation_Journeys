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

        # ❤️ Bond
        self.bond = 50

        # Emotion
        self.comeback_used = False
        self.rage_active = False
        self.survival_used = False

        # ☠️ STATUS SYSTEM
        self.status = None
        self.poison_counter = 1

    # ----------------------------
    # DAMAGE + STATUS
    # ----------------------------
    def take_damage(self, damage):
        if damage >= self.hp:
            if self.bond >= 70 and not self.survival_used:
                self.survival_used = True
                self.hp = 1
                print(f"💖 {self.name} endured the hit because of strong bond!")
                return

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        if self.is_low_hp() and not self.rage_active:
            self.rage_active = True
            print(f"😡 {self.name} entered RAGE MODE!")

    # ----------------------------
    # STATUS APPLY
    # ----------------------------
    def apply_status(self, status):
        if self.status is None:
            self.status = status
            print(f"⚠️ {self.name} is now {status.upper()}!")

    # ----------------------------
    # STATUS EFFECT EACH TURN
    # ----------------------------
    def apply_status_effect(self):
        if self.status == "burn":
            damage = int(self.max_hp * 0.05)
            self.hp -= damage
            print(f"🔥 {self.name} is hurt by burn! (-{damage})")

        elif self.status == "poison":
            damage = int(self.max_hp * 0.05 * self.poison_counter)
            self.hp -= damage
            self.poison_counter += 1
            print(f"☠️ {self.name} is hurt by poison! (-{damage})")

        if self.hp < 0:
            self.hp = 0

    def is_paralyzed(self):
        if self.status == "paralysis":
            import random
            if random.random() < 0.3:
                print(f"⚡ {self.name} is paralyzed and can't move!")
                return True
        return False

    # ----------------------------
    def is_low_hp(self):
        return self.hp <= (0.3 * self.max_hp)

    def trigger_comeback(self):
        if not self.comeback_used and self.is_low_hp():
            self.comeback_used = True
            print(f"🔥 {self.name} refuses to give up!")
            return True
        return False

    def increase_bond(self, amount):
        self.bond = min(100, self.bond + amount)

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
        return f"{self.name} HP: {self.hp}/{self.max_hp} Status: {self.status}"
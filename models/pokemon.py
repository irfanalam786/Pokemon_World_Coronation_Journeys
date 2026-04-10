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

        # 🔥 Signature Move
        self.signature_move = data.get("signature_move")

        # Emotion system
        self.comeback_used = False
        self.rage_active = False
        self.survival_used = False

    def take_damage(self, damage):
        if damage >= self.hp and not self.survival_used:
            self.survival_used = True
            self.hp = 1
            print(f"💖 {self.name} held on with 1 HP!")
            return

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

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

    def get_attack_multiplier(self):
        return 1.2 if self.rage_active else 1.0

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (Lv {self.level}) HP: {self.hp}/{self.max_hp}"
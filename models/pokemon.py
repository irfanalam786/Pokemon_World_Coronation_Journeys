class Pokemon:
    def __init__(self, data):
        # Load from JSON dynamically
        self.name = data.get("name")
        self.type = data.get("type")
        self.hp = data.get("hp")
        self.max_hp = data.get("hp")
        self.attack = data.get("attack")
        self.defense = data.get("defense")
        self.speed = data.get("speed")
        self.level = data.get("level", 1)

        # Future systems placeholders
        self.exp = 0
        self.bond = 0
        self.status = None

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
        return f"{self.name} (Lv {self.level}) HP: {self.hp}/{self.max_hp}"
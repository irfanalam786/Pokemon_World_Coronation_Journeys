class Pokemon:
    def __init__(self, name, hp, attack, defense, speed, p_type):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.type = p_type
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)

    def is_fainted(self):
        return self.hp <= 0

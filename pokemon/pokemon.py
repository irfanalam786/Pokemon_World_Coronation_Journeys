# ==============================
# Base Pokemon Class
# ==============================

# Define Pokemon base class
class Pokemon:

    # Constructor method
    def __init__(self, name, hp, attack, defense, speed, p_type):

        # Store Pokemon name
        self.name = name

        # Store maximum HP for reset
        self.max_hp = hp

        # Current HP starts at maximum
        self.hp = hp

        # Store attack stat
        self.attack = attack

        # Store defense stat
        self.defense = defense

        # Store speed stat
        self.speed = speed

        # Store Pokemon type
        self.type = p_type

        # Create empty move list
        self.moves = []

    # Add move to Pokemon
    def add_move(self, move):
        self.moves.append(move)

    # Check if Pokemon fainted
    def is_fainted(self):
        return self.hp <= 0

    # Reset HP after battle
    def reset_hp(self):
        self.hp = self.max_hp
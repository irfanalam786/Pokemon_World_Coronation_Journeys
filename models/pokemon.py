from systems.image_manager import ImageManager
from systems.sound_manager import SoundManager
import random

class Pokemon:
    def __init__(self, data):
        self.name = data.get("name")
        self.type = data.get("type")

        self.max_hp = data.get("hp")
        self.hp = self.max_hp
        self.attack = data.get("attack")
        self.defense = data.get("defense")

        self.level = data.get("level", 5)
        self.exp = 0

        self.moves = data.get("moves", [])

        self.image = data.get("image")
        self.evolution = data.get("evolution")

        self.image_manager = ImageManager()
        self.sound = SoundManager()

        self.status = None
        self.poison_counter = 1

        self.bond = 50
        self.clutch_used = False
        self.survival_used = False

    # ----------------------------
    def apply_status(self, status):
        if self.status is None:
            self.status = status
            print(f"⚠️ {self.name} is now {status.upper()}!")

    def process_status(self):
        if self.status == "burn":
            dmg = int(self.max_hp * 0.05)
            self.hp -= dmg
            print(f"🔥 Burn damage: {dmg}")

        elif self.status == "poison":
            dmg = int(self.max_hp * 0.05 * self.poison_counter)
            self.hp -= dmg
            self.poison_counter += 1
            print(f"☠️ Poison damage: {dmg}")

        if self.hp < 0:
            self.hp = 0

    def is_paralyzed(self):
        if self.status == "paralysis":
            if random.random() < 0.3:
                print(f"⚡ {self.name} is paralyzed! Can't move!")
                return True
        return False

    # ----------------------------
    def show_image(self):
        if self.image:
            self.image_manager.show(self.image)

    # ----------------------------
    def gain_exp(self, opponent_level):
        exp_gain = 20 + (opponent_level * 10)
        print(f"✨ {self.name} gained {exp_gain} EXP!")
        self.exp += exp_gain

        while self.exp >= self.exp_to_next_level():
            self.exp -= self.exp_to_next_level()
            self.level_up()

    def exp_to_next_level(self):
        return 40 + (self.level * 25)

    def level_up(self):
        self.level += 1
        print(f"🔥 {self.name} leveled up to {self.level}!")

        self.max_hp += 5
        self.attack += 2
        self.defense += 2
        self.hp = self.max_hp

        self.check_evolution()

    def check_evolution(self):
        if not self.evolution:
            return

        if self.level >= self.evolution["level"]:
            print(f"\n✨ {self.name} is evolving...")
            self.sound.play_evolution()

            old_name = self.name

            self.name = self.evolution["name"]
            self.max_hp = self.evolution["hp"]
            self.attack = self.evolution["attack"]
            self.defense = self.evolution["defense"]
            self.image = self.evolution.get("image")

            self.hp = self.max_hp

            print(f"🧬 {old_name} evolved into {self.name}!")
            self.show_image()

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
            self.sound.play_clutch()
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

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} HP:{self.hp}/{self.max_hp} Status:{self.status}"
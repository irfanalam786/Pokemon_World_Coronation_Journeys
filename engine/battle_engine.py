# engine/battle_engine.py

from ai_system.advanced_ai import AdvancedAI
from core.difficulty_system import DifficultySystem
from progression.balance_system import BalanceSystem
from ranking.leaderboard_system import LeaderboardSystem
import random


class BattleEngine:
    def __init__(self, difficulty="Normal"):
        self.power = 20
        self.ai = AdvancedAI()
        self.difficulty = DifficultySystem(difficulty)
        self.balance = BalanceSystem()
        self.leaderboard = LeaderboardSystem()

        self.type_chart = {
            "Fire": {"Grass": 2.0, "Water": 0.5},
            "Water": {"Fire": 2.0, "Electric": 0.5},
            "Electric": {"Water": 2.0},
            "Grass": {"Water": 2.0, "Fire": 0.5},
        }

        self.crit_chance = 0.1
        self.crit_multiplier = 2

    def print_turn(self, turn):
        print("\n" + "=" * 40)
        print(f"🔥 TURN {turn}")
        print("=" * 40)

    def print_action(self, msg):
        print(f"➡️ {msg}")

    def print_hp(self, p):
        print(f"❤️ {p.get_name()} HP: {p.get_hp()}")

    def get_type_multiplier(self, atk_type, def_type):
        return self.type_chart.get(atk_type, {}).get(def_type, 1.0)

    def calculate_damage(self, attacker, defender, is_enemy=False):
        base = (attacker.get_attack() / defender.get_defense()) * self.power
        multiplier = self.get_type_multiplier(attacker.get_type(), defender.get_type())

        damage = base * multiplier

        if attacker.get_role() == "attacker":
            damage *= 1.1
        if defender.get_role() == "tank":
            damage *= 0.8

        if is_enemy:
            damage *= self.difficulty.get_setting("enemy_damage_multiplier")

        crit = False
        if random.random() < self.crit_chance:
            damage *= self.crit_multiplier
            crit = True

        damage = self.balance.balance_damage(int(damage))

        return damage, multiplier, crit

    def perform_attack(self, attacker, defender, trainer_owner, is_enemy=False):
        if attacker.is_fainted():
            return

        if not attacker.process_status():
            self.print_action(f"{attacker.get_name()} couldn't move!")
            return

        damage, multiplier, crit = self.calculate_damage(attacker, defender, is_enemy)

        self.print_action(f"{attacker.get_name()} attacks {defender.get_name()}")

        if multiplier > 1:
            print("💥 Super effective!")
        elif multiplier < 1:
            print("⚠️ Not very effective...")

        if crit:
            print("🔥 CRITICAL HIT!")

        defender.take_damage(damage)
        self.print_hp(defender)

        trainer_owner.stats.add_damage(damage)

    def decide_turn_order(self, p1, p2):
        s1, s2 = p1.get_speed(), p2.get_speed()

        if p1.get_role() == "speed": s1 *= 1.1
        if p2.get_role() == "speed": s2 *= 1.1

        return (p1, p2) if s1 >= s2 else (p2, p1)

    def start_battle(self, trainer1, trainer2):
        print("\n=== ⚔️ BATTLE START ===")

        turn = 1

        while True:
            p1 = trainer1.get_active_pokemon()
            p2 = trainer2.get_active_pokemon()

            if not p1 or not p2:
                break

            self.print_turn(turn)

            first, second = self.decide_turn_order(p1, p2)

            self.perform_attack(first, second, trainer1)
            if second.is_fainted():
                self.print_action(f"{second.get_name()} fainted!")
                continue

            action, value = self.ai.choose_action(second, first, trainer2, self)

            if action == "attack":
                self.perform_attack(second, first, trainer2, is_enemy=True)
            elif action == "switch":
                trainer2.switch_pokemon(value)
                self.print_action("AI switched Pokémon!")

            if first.is_fainted():
                self.print_action(f"{first.get_name()} fainted!")

            turn += 1

        print("\n" + "=" * 40)

        # ---------------- RESULT ----------------
        if trainer1.get_active_pokemon():
            print("🏆 Player Wins!")
            trainer1.stats.record_win()
            trainer2.stats.record_loss()
            trainer1.add_points(20)
        else:
            print("💀 AI Wins!")
            trainer1.stats.record_loss()
            trainer2.stats.record_win()
            trainer1.add_points(-10)

        print("=" * 40)

        # ---------------- SYSTEMS ----------------
        trainer1.achievements.check_achievements(trainer1)
        trainer1.stats.show_stats()
        trainer1.achievements.show_achievements()

        # 🔥 UPDATE LEADERBOARD
        self.leaderboard.update_leaderboard(trainer1)
        self.leaderboard.show_leaderboard()

        trainer1.reset_team()
        trainer2.reset_team()
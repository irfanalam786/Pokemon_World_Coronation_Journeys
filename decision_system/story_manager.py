# decision_system/story_manager.py

class StoryManager:
    def __init__(self, player_choices):
        self.choices = player_choices
        self.flags = {
            "met_eclipse": False,
            "route_selected": self.choices.path
        }

    def start_story(self):
        print("\n=== STORY START ===")

        self.intro_event()
        self.route_event()

    def intro_event(self):
        print("\nYou begin your journey as a Pokémon Trainer...")

        if self.choices.starter:
            starter_name = self.choices.starter[0]
            print(f"You chose {starter_name} as your partner.")

    def route_event(self):
        print("\n=== ROUTE EVENT ===")

        if self.flags["route_selected"] == "Battle Path":
            self.battle_route()

        elif self.flags["route_selected"] == "Exploration Path":
            self.exploration_route()

        elif self.flags["route_selected"] == "Strategy Path":
            self.strategy_route()

    # ---------------- ROUTES ----------------
    def battle_route(self):
        print("You enter a battle-focused route full of trainers.")
        print("A mysterious trainer watches you from afar...")

        self.team_eclipse_hint()

    def exploration_route(self):
        print("You explore wild areas and discover hidden paths.")
        print("You find strange markings on the ground...")

        self.team_eclipse_hint()

    def strategy_route(self):
        print("You study battle tactics and meet experienced trainers.")
        print("You overhear a suspicious conversation...")

        self.team_eclipse_hint()

    # ---------------- TEAM ECLIPSE ----------------
    def team_eclipse_hint(self):
        print("\n⚠ A shadowy figure appears briefly...")
        print("They whisper: 'The Eclipse is coming...'")

        self.flags["met_eclipse"] = True
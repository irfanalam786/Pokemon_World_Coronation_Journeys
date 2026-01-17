from ui.menu import MainMenu

class Game:
    def __init__(self):
        self.running = True
        self.menu = MainMenu()

    def start(self):
        print("Pokemon World: Coronation Journeys!")
        print("-----------------------------------")
        self.menu.show()
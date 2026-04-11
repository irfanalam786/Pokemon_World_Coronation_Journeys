import winsound

class SoundManager:
    def play_attack(self):
        winsound.Beep(800, 200)

    def play_clutch(self):
        winsound.Beep(1200, 300)

    def play_evolution(self):
        winsound.Beep(600, 500)
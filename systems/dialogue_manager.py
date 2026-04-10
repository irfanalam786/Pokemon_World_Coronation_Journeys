import time
import sys

class DialogueManager:
    def __init__(self, speed=0.005):  # 🔥 Faster speed
        self.speed = speed

    def type_text(self, text):
        try:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(self.speed)
            print()
        except KeyboardInterrupt:
            # 🔥 If user interrupts → instantly print full text
            print("\n[Skipped Dialogue]")
            print(text)

    def speak(self, speaker, text):
        self.type_text(f"{speaker}: {text}")
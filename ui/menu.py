from ui.character_select import CharacterSelect

class MainMenu:
    def show(self):
        print("\n1. Start Game")
        print("2. Exit")

        choice=input("Enter choice:")

        if choice == '1':
            selector = CharacterSelect()
            selector.select()
        else:
            print("Exiting game.")
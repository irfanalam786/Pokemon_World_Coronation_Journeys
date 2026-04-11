import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from core.game import Game

class GameUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokémon Anime RPG")
        self.root.geometry("800x600")

        self.game = Game()

        # ----------------------------
        self.top_frame = tk.Frame(self.root, height=300, bg="lightblue")
        self.top_frame.pack(fill="both")

        self.player_label = tk.Label(self.top_frame, bg="lightblue")
        self.player_label.pack(side="left", padx=50)

        self.opponent_label = tk.Label(self.top_frame, bg="lightblue")
        self.opponent_label.pack(side="right", padx=50)

        # ----------------------------
        self.text_box = tk.Text(self.root, height=8)
        self.text_box.pack(fill="both")

        # ----------------------------
        self.attack_btn = tk.Button(self.root, text="Attack", command=self.attack)
        self.attack_btn.pack()

        self.update_ui()

    # ----------------------------
    def load_img(self, url):
        img = Image.open(BytesIO(requests.get(url).content))
        img = img.resize((150, 150))
        return ImageTk.PhotoImage(img)

    def update_ui(self):
        state = self.game.get_state()

        p_img = self.load_img(state["player_img"])
        o_img = self.load_img(state["opponent_img"])

        self.player_label.config(image=p_img)
        self.player_label.image = p_img

        self.opponent_label.config(image=o_img)
        self.opponent_label.image = o_img

        self.text_box.insert(tk.END, f"\n{state['player']} vs {state['opponent']}")

    # ----------------------------
    def attack(self):
        result = self.game.attack()
        self.text_box.insert(tk.END, f"\n{result}")

        opp = self.game.opponent_turn()
        self.text_box.insert(tk.END, f"\n{opp}")

        self.update_ui()

    def run(self):
        self.root.mainloop()
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class GameUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokémon Anime RPG")
        self.root.geometry("800x600")

        # ----------------------------
        # TOP FRAME (Battle Area)
        # ----------------------------
        self.top_frame = tk.Frame(self.root, height=300, bg="lightblue")
        self.top_frame.pack(fill="both")

        self.player_image_label = tk.Label(self.top_frame, bg="lightblue")
        self.player_image_label.pack(side="left", padx=50, pady=20)

        self.opponent_image_label = tk.Label(self.top_frame, bg="lightblue")
        self.opponent_image_label.pack(side="right", padx=50, pady=20)

        # ----------------------------
        # MIDDLE FRAME (Dialogue)
        # ----------------------------
        self.middle_frame = tk.Frame(self.root, height=150, bg="white")
        self.middle_frame.pack(fill="both")

        self.text_box = tk.Text(self.middle_frame, height=5, font=("Arial", 12))
        self.text_box.pack(fill="both", padx=10, pady=10)

        # ----------------------------
        # BOTTOM FRAME (Controls)
        # ----------------------------
        self.bottom_frame = tk.Frame(self.root, height=150, bg="gray")
        self.bottom_frame.pack(fill="both")

        self.attack_btn = tk.Button(self.bottom_frame, text="Attack", width=15)
        self.attack_btn.pack(side="left", padx=20, pady=20)

        self.switch_btn = tk.Button(self.bottom_frame, text="Switch", width=15)
        self.switch_btn.pack(side="left", padx=20, pady=20)

        self.item_btn = tk.Button(self.bottom_frame, text="Item", width=15)
        self.item_btn.pack(side="left", padx=20, pady=20)

    # ----------------------------
    def load_image_from_url(self, url, size=(150, 150)):
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize(size)

        return ImageTk.PhotoImage(img)

    # ----------------------------
    def show_pokemon(self, player_url, opponent_url):
        player_img = self.load_image_from_url(player_url)
        opponent_img = self.load_image_from_url(opponent_url)

        self.player_image_label.config(image=player_img)
        self.player_image_label.image = player_img

        self.opponent_image_label.config(image=opponent_img)
        self.opponent_image_label.image = opponent_img

    # ----------------------------
    def run(self):
        # TEST IMAGES
        self.show_pokemon(
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"
        )

        self.root.mainloop()
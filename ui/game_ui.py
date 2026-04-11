import tkinter as tk

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

        self.player_label = tk.Label(self.top_frame, text="Player Pokémon", bg="lightblue", font=("Arial", 14))
        self.player_label.pack(side="left", padx=50, pady=50)

        self.opponent_label = tk.Label(self.top_frame, text="Opponent Pokémon", bg="lightblue", font=("Arial", 14))
        self.opponent_label.pack(side="right", padx=50, pady=50)

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

    def run(self):
        self.root.mainloop()
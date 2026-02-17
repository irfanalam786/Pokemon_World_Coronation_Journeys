# ==============================
# Save & Load System (Full State Version)
# ==============================

# Import JSON module for file operations
import json

# Import trainer classes
from characters.ash import Ash
from characters.goh import Goh
from characters.chloe import Chloe

# Import Pokémon classes
from pokemon.pikachu import Pikachu
from pokemon.cinderace import Cinderace
from pokemon.eevee import Eevee

# Define save file name
SAVE_FILE = "savegame.json"

# SaveLoadManager class
class SaveLoadManager:

    # Save full trainer state
    @staticmethod
    def save_game(trainer):

        # Create data dictionary
        data = {
            "trainer_name": trainer.name,
            "rank": trainer.rank,
            "pokemon_team": []
        }

        # Loop through trainer Pokémon
        for pokemon in trainer.team:

            # Append Pokémon data
            data["pokemon_team"].append({
                "name": pokemon.name,
                "current_hp": pokemon.hp
            })

        # Open file in write mode
        with open(SAVE_FILE, "w") as file:

            # Write JSON with formatting
            json.dump(data, file, indent=4)

        # Print confirmation
        print("Game saved successfully.")

    # Load full trainer state
    @staticmethod
    def load_game():

        try:
            # Open save file
            with open(SAVE_FILE, "r") as file:

                # Load JSON data
                data = json.load(file)

            # Recreate trainer
            if data["trainer_name"] == "Ash Ketchum":
                trainer = Ash()
            elif data["trainer_name"] == "Goh":
                trainer = Goh()
            else:
                trainer = Chloe()

            # Restore rank
            trainer.rank = data["rank"]

            # Restore Pokémon HP
            for i, pokemon_data in enumerate(data["pokemon_team"]):

                # Set HP of each Pokémon
                trainer.team[i].hp = pokemon_data["current_hp"]

            # Print confirmation
            print("Game loaded successfully.")

            return trainer

        except Exception as e:

            # If error occurs
            print("Failed to load save file.")
            print("Error:", e)

            return None
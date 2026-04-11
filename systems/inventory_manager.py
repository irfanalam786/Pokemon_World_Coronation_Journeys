class InventoryManager:
    def __init__(self):
        self.items = {
            "Potion": 3,
            "Rare Candy": 1
        }

    def show_items(self):
        print("\n🎒 Inventory:")
        for i, (item, qty) in enumerate(self.items.items()):
            print(f"{i + 1}. {item} x{qty}")

    def use_item(self, choice, pokemon):
        item_list = list(self.items.keys())

        if choice < 0 or choice >= len(item_list):
            print("❌ Invalid item!")
            return False

        item = item_list[choice]

        if self.items[item] <= 0:
            print("❌ No items left!")
            return False

        # ----------------------------
        if item == "Potion":
            heal = int(pokemon.max_hp * 0.5)
            pokemon.hp = min(pokemon.max_hp, pokemon.hp + heal)
            print(f"🧪 {pokemon.name} healed by {heal} HP!")

        elif item == "Rare Candy":
            print(f"🍬 {pokemon.name} used Rare Candy!")
            pokemon.level_up()

        self.items[item] -= 1
        return True
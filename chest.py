import random

class Chest:
    def __init__(self, items):
        self.items = items

    def open(self):
        item = random.choice(self.items)
        return item
    
items_pool = ["Nail", "Protein Flask", "Baguette", "Vape", "Ciggs", "Slipper", "Bible"]
lootbox = Chest(items_pool)

for _ in range(7):
    item = lootbox.open()
    print("You received", item)

   # def open_loot_box():
   # loot_table = {
   #     "Protein Flask": 12.2%,
    #    "Nail": 12.2%,
    #    "vape": 12.2%,
    #    "cigareter": 6.5%,
      #  "baguette": 6.5%,
   #     "slipper": 2.5%,
   #     "Holy Bible": 0.5%

   # }


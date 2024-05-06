import random

class Chest:
    def __init__(self):
        self.is_open = False
        self.items = ["Health potion"]

    def open(self):
        if not self.is_open:
            print("You opened the chest!")
            self.is_open = True
            self.open_chest()
        else:
            print("The chest is already open!")

    def open_chest(self):
        print (f"You found a {self.items}!")
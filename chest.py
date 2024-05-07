import random

class Chest:
    def __init__(self, items = []):
        self.is_open = False
        self.items = items

    def open(self):
        if not self.is_open:
            print("You opened the chest!")
            self.is_open = True
            self.open_chest()
            return self.open_chest()
        else:
            print("The chest is already open!")
            

    def open_chest(self):
        if self.items:
            found_item = random.choice(self.items)
            self.items.remove(found_item)
            return found_item
        else:
            print("The chest is empty!")
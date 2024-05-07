import random

class Potion:
    def __init__(self, name, health_amount):
        self.name = name
        self.health_amount = health_amount

    def use_health_potion(self, character):
        character.hp += self.health_amount
        
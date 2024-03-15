import random

class HealthPotion:
    def __init__(self, health_amount):
        self.healt_amount = health_amount

    def use_health_potion(player):
        health_amount = random.randint(20, 40)
        player.health += health_amount
        print(f"You've found a health potion and restored {health_amount} health!")
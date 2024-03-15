import random

class Enemy:
    def __init__(self, name, attack, hp, dialogue, weapon):
        self.name = name
        self.hp = hp
        self.dialogue = dialogue
        self.weapon = weapon
        self.attack = attack

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacked {enemy.name} with {self.weapon.name} for {damage} damage!")

    def health_bar(self):
        print(f"{self.name} has {self.hp} HP left")

    def catch_phrase(self):
        print(self.dialogue)
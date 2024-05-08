import random

class Enemy:
    def __init__(self, name, attack, hp, dialogue, weapon, accuracy):
        self.name = name
        self.hp = hp
        self.dialogue = dialogue
        self.weapon = weapon
        self.attack = attack
        self.stunned = 0
        self.weakened = 1.0
        self.accuracy = 1.0

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        if random.randint(1, 10) == 1:
            print(f"{self.name}'s attack missed!")
            return
        if self.stunned > 0:
            print(f"{self.name} is stunned and cannot attack!")
            self.stunned -= 1
        else:
            if self.weapon is None:
                damage = random.randint(1, int(self.attack // 2 * self.weakened))
            else:
                damage = random.randint(1, int(self.attack * self.weakened) + self.weapon.damage)
            enemy.take_damage(damage)
            if self.weapon:
                print(f"{self.name} attacked {enemy.name} with {self.weapon.name} for {damage} damage!")
            else:
                print(f"{self.name} attacked {enemy.name} for {damage} damage!")

    def health_bar(self):
        print(f"{self.name} has {self.hp} HP left")

    def catch_phrase(self):
        print(self.dialogue)
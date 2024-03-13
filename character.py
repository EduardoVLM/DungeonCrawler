import random

class character:
    def __init__(self, name, hp, attack,  weapon, agility, strength, s_ability):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.weapon = weapon
        self.agility = agility
        self.strength = strength
        self.s_ability = s_ability
        
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacked {enemy.name} for {damage} damage!")

    def health_bar(self):
        print(f"{self.name} has {self.hp} HP left")
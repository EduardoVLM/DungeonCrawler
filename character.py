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
        self.inventory = {"Health Potion": 2}
        
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack) + self.weapon.damage
        enemy.take_damage(damage)
        print(f"{self.name} attacked {enemy.name} with {self.weapon.name} for {damage} damage!")

    def health_bar(self):
        print(f"{self.name} has {self.hp} HP left")

    def use_item(self,item):
        if self.inventory.get(item):
            if item == "Health Potion":
                self.hp += 40
                self.inventory[item] -= 1
                print(f"{self.name} used a health potion and gained 40 HP")
            else:
                print("Invalid item")
        else:
            print("You don't have that item")

    def kleptomania(self, enemy):
        if self.name != "Edo":
            print({"Youre not him"})
            return
        if enemy.weapon:
            self.weapon = enemy.weapon
            enemy.weapon = None
            print(f"You have stolen the {self.weapon.name} from {enemy.name}")
        else:
            print(f"{enemy.name} has no weapon to steal")

    def flour_explosion(self, enemy):
        if self.name != "Emil":
            print("Youre not him")
            return
        enemy.take_damage(40)
        print(f"{self.name} used Flour Explosion on {enemy.name} for 40 damage and stunned him for 2 turns")

    def smoke(self, enemy):
        if self.name != "Ibi":
            print("Youre not him")
            return
        enemy.stunned = 2
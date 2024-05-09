import random
import os

class character:
    def __init__(self, name, hp, attack,  weapon, agility, strength, s_ability, accuracy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.weapon = weapon
        self.agility = agility
        self.strength = strength
        self.s_ability = s_ability
        self.inventory = {"Health Potion": 2}
        self.buffed = 1.0
        self.accuracy = 1.0
        self.cooldown = 3
        
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        os.system("cls")
        if random.randint(1, 10) == 1:
            print(f"{self.name}'s Attack missed!")
            return
        if self.buffed > 1.0:
            self.attack = int(self.attack * self.buffed)
        else:
            self.attack = self.attack
        damage = random.randint(1, self.attack) + self.weapon.damage
        enemy.take_damage(damage)
        print(f"{self.name} attacked {enemy.name} with {self.weapon.name} for {damage} damage!")
        self.buffed = 1.0

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
        if self.cooldown > 0:
            print("You can't use that ability yet!")
            self.cooldown -= 1
            return
        if random.randint(1, 5) == 1:
            print(f"{self.name}'s Special ability missed!")
            return
        if self.name != "Edo":
            print({"Youre not him"})
            return
        if enemy.weapon:
            self.weapon = enemy.weapon
            enemy.weapon = None
            print(f"You have stolen the {self.weapon.name} from {enemy.name}")
        else:
            print(f"{enemy.name} has no weapon to steal")
        self.cooldown = 3

    def flour_explosion(self, enemy):
        if self.cooldown > 0:
            print("You can't use that ability yet!")
            self.cooldown -= 1
            return
        if random.randint(1, 6) == 1:
            print(f"{self.name}'s Special ability missed!")
            return
        if self.name != "Emil":
            print("Youre not him")
            return
        enemy.take_damage(50)
        self.take_damage(20)
        print(f"{self.name} used Flour Explosion on {enemy.name} for 50 damage!")
        print(f"{self.name} took 20 damage from the explosion and has {self.hp} HP left!")
        self.cooldown = 3

    def røyk(self, enemy):
        if self.cooldown > 0:
            print("You can't use that ability yet!")
            self.cooldown -= 1
            return
        if random.random() > self.accuracy:
            print(f"{self.name}'s Special ability missed!")
            return
        if self.name != "Ibi":
            print("Youre not him")
            return
        enemy.stunned = 2
        print(f"{self.name} used Smoke on {enemy.name} and stunned them for 2 turns!")
        self.cooldown = 3

    def insults(self, enemy):
        if self.cooldown > 0:
            print("You can't use that ability yet!")
            self.cooldown -= 1
            return
        if random.random() > self.accuracy:
            print(f"{self.name}'s Special ability missed!")
            return
        if self.name != "Thea":
            print("Youre not her")
            return
        enemy.weakened = 0.25
        print(f"{self.name} insulted {enemy.name} and weakened their attacks!")
        self.cooldown = 3

    def stg_buff(self, enemy):
        if self.cooldown > 0:
            print("You can't use that ability yet!")
            self.cooldown -= 1
            return
        if random.random() > self.accuracy:
            print(f"{self.name}'s Special ability missed!")
            return
        if self.name != "Ody":
            print("Youre not him")
            return
        self.buffed = 2.0
        print(f"{self.name} has buffed his strength!")
        self.cooldown = 3

    def nail_barrage(self, enemy):
        if self.cooldown > 0:
            print("You can't use that ability yet!")
            self.cooldown -= 1
            return
        if random.random() > self.accuracy:
            print(f"{self.name}'s Special ability missed!")
            return
        if self.name != "Leah":
            print("Youre not her")
            return
        enemy.take_damage(30)
        print(f"{self.name} throws a barrage of sharp nails at {enemy.name} for 30 damage!")
        self.cooldown = 3
    
    def at_barrage(self, enemy):
        if random.randint(1, 5) == 1:
            print(f"{self.name}'s Special ability missed!")
            return
        if self.cooldown > 1:
            print("You can't use that ability yet!")
            self.cooldown -= 1
            return
        if self.name != "Ferdi":
            print("Youre not him")
            return
        enemy.take_damage(60)
        print(f"{self.name} shoots a barrage of artilery sheels at {enemy.name} for 60 damage!")
        self.cooldown = 3
        
        #def end_turn(self):
            #if self.cooldown > 0:
                #self.cooldown -= 1

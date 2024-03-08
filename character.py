class Character:
    def __init__(self, name, health, weapon, agility, strength, s_ability):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.agility = agility
        self.strength = strength
        self.s_ability = s_ability

    def attack(self, enemy):
        damage = self.weapon.damage
        enemy.health -= damage
        print(f"You dealt {damage} damage to {enemy}")
        
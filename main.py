#--------------------imports----------------------------#

import os
from room import Room
from enemy import Enemy
from weapon import Weapon
from character import character
from chest import Chest
#---------------------weapons---------------------------#

fists = Weapon("Fist", 2, 1)
protein_f = Weapon("Protein flask", 2, 2)
nail = Weapon("Nails", 1, 3)
vape = Weapon("Vape", 1.5, 2)
cigareter = Weapon("Cigg", 2, 2)
baguette = Weapon("Baguette", 3, 1)
teeth = Weapon("Teeth", 2, 1)
slipper = Weapon("Slipper", 7, 5)
bible = Weapon("Holy Bible", 10, 10)

#-------------------characters--------------------------#

edo = character("Edo", 100, 10, fists, 5, 5, "Kleptomania")
emil = character("Emil", 110, 10, baguette, 6, 6, "Flour explosion")
ibi = character("Ibi", 110, 10, cigareter, 4, 5, "Røyk")
thea = character("Thea", 110, 10, vape, 5, 7, "Insults")
ody = character("Ody", 120, 10, protein_f, 6, 8, "STG buff")
leah = character("Leah", 100, 10, nail, 5, 5, "MF ult")

character_choice = [edo, emil, ibi, thea, ody, leah]

def choose_character(character_choice):
        print(f"Choose your character:")

        for i in range(len(character_choice)):
            print(f"{i + 1}) {character_choice[i].name}.")

        choosen_character = input("Choose a character from the menu: ")
        while len(choosen_character) < 1 or int(choosen_character) > len(character_choice):
            choosen_character = input("Invalid input! Choose again")
        i = int(choosen_character) - 1
        return character_choice[i]
            
             
             
     

#---------------------enemies---------------------------#

meggie = Enemy("Meggie", 5, 30, "AUAUAUAUAUAUAUAUAUAU", teeth)
mor = Enemy("Mor", 10, 100, "Go buy rice now!", slipper)
bestemor = Enemy("Bestemor", 20, 200, "I want to sleep, stop playing!", bible)

#---------------------rooms-----------------------------#

current_room = None

edo_room = Room("Edo room", None, 1, "It stinks here")
hall = Room("Hall", meggie , 1, "Meggie's realm")
kitchen = Room("Kitchen", mor, 1, "smells good")
stue = Room("Living Room", bestemor, None, "You feel a menacing aura aproaching")
hell = Room("Hell", None, 1, "Welcome to the abyss of eternal torment!")

#------------------connecting rooms---------------------#

edo_room.connecting_rooms = [hall]
hall.connecting_rooms = [stue, kitchen, edo_room]
kitchen.connecting_rooms = [hall]
stue.connecting_rooms = [hall]
current_room = edo_room

#--------------------chests-----------------------------#

lootbox = Chest([nail, protein_f, slipper, bible, vape, cigareter, baguette,])

#-------------character choice menu---------------------#

os.system("cls")
character = choose_character(character_choice)

#---------------------start game------------------------#

def start_game(character):
     print(f"You are playing as {character.name}")
     input("Press ENTER to start game")
    
start_game(character)

#--------------------battle system----------------------#

def Start_battle(character, Enemy):
    score = 0
    print("Battle Start!")

    while character.is_alive() and Enemy.is_alive():
        input("Press ENTER to attack")
        character.attack_enemy(Enemy)
        Enemy.health_bar()
        if not Enemy.is_alive():
            print(f"you've defeated {Enemy.name}!")
            score = 10
            break
        input("Press ENTER to resume")
        Enemy.attack_enemy(character)
        character.health_bar()
        if not character.is_alive():
            print("You have been defeated!")
            score = -10
            break
    
    print("Battle End!")
    return score

#--------------------game loop--------------------------#

score = 0
while True:
    os.system("cls")
    current_room.room_name()
    current_room.describe_room()
    Enemy = current_room.room_monster_display()
    if Enemy:
        result = Start_battle(character, Enemy)
        score += result
        print(f"Score {score}")
        if not character.is_alive():
            print("GAME OVER")
            break
    neste_rom = current_room.room_menu()
    current_room = current_room.connecting_rooms[int(neste_rom)]
    

   
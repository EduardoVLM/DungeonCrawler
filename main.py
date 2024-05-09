#--------------------imports----------------------------#

import os
from room import Room
from enemy import Enemy
from weapon import Weapon
from character import character
from potion import Potion
from chest import Chest

#---------------------weapons---------------------------#

fists = Weapon("Fist", 10, 1)
protein_f = Weapon("Protein flask", 12, 2)
nail = Weapon("Nails", 12, 3)
vape = Weapon("Vape", 15, 2)
cigareter = Weapon("Cigg", 10, 2)
baguette = Weapon("Baguette", 15, 1)
art = Weapon("AT kanon", 20, 10)
teeth = Weapon("Teeth", 8, 1)
slipper = Weapon("Slipper", 15, 5)
bible = Weapon("Holy Bible", 18, 10)
fish = Weapon("Fish", 10, 1)
rage = Weapon("Rage", 18, 1)

#-------------------potions-----------------------------#

Health_potion = Potion("Health potion", 20)
Hp_potion = Potion("Hp potion", 30)
Healing_juice = Potion("Healing juice", 40)

#--------------------chests-----------------------------#

edo_room_chest = Chest([Health_potion, Hp_potion, Healing_juice])
hall_chest = Chest([Health_potion, Hp_potion, Healing_juice])
kitchen_chest = Chest([Health_potion, Hp_potion, Healing_juice])
hell_chest = Chest([Health_potion, Hp_potion, Healing_juice])
lager_rom_chest = Chest([Health_potion, Hp_potion, Healing_juice])
toalett_chest = Chest([Health_potion, Hp_potion, Healing_juice])

#-------------------characters--------------------------#

edo = character("Edo", 100, 10, fists, 5, 5, "Kleptomania", 0.5)
emil = character("Emil", 110, 10, baguette, 6, 6, "Flour explosion", 6)
ibi = character("Ibi", 110, 10, cigareter, 4, 5, "Røyk", 6)
thea = character("Thea", 110, 10, vape, 5, 7, "Insults", 6)
ody = character("Ody", 120, 10, protein_f, 6, 8, "STG buff", 6)
leah = character("Leah", 100, 50, nail, 5, 5, "MF ult", 6)
ferdinand = character("Ferdi", 110, 11, art, 6, 7, "Sprenge shit", 6)

character_choice = [edo, emil, ibi, thea, ody, leah, ferdinand]

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

meggie = Enemy("Meggie", 8, 30, '"AUAUAUAUAUAUAUAUAUAU"', teeth, 7)
fish = Enemy("Fish", 5, 20, '"GlubGlubGlubbGlub"', fish, 7)
mor = Enemy("Mor", 10, 100, '"Go buy rice now!"', slipper, 7)
bestemor = Enemy("Bestemor", 20, 200, '"I want to sleep, stop playing!"', bible, 7)
stefan = Enemy("Stefan", 15, 150, '"Go take care of Matheus!"', cigareter, 7)
matheus = Enemy("Matheus", 35, 75, '"EU NAO QUERO!!"', rage, 7)


#---------------------rooms-----------------------------#

current_room = None

edo_room = Room("Edo room", None, edo_room_chest, "It stinks here", {"Explore the Wardrobe": Room.explore_wardrobe, "Explore under the bed": Room.explore_under_bed})
hall = Room("Hall", meggie , hall_chest, "Meggie's realm")
lager_rom = Room("Lager Rom", None, lager_rom_chest, "You feel like theres something hidden here")
toalett = Room("Toalett", fish, toalett_chest, "Smells like fish")
kitchen = Room("Kitchen", mor, kitchen_chest, "smells good")
stue = Room("Living Room", bestemor, None, "You feel a menacing aura aproaching")
varanda = Room("Varanda", stefan, None, "It stinks cigaretes.")
mamma_rom = Room("Mor's room", matheus, None, "This was once a place of peace, but that was before HE arrived" )
hell = Room("Hell", None, hell_chest, "Welcome to the abyss of eternal torment!")

#------------------connecting rooms---------------------#

edo_room.connecting_rooms = [hall]
hall.connecting_rooms = [stue, kitchen, edo_room, mamma_rom, toalett, lager_rom]
lager_rom.connecting_rooms = [hall]
toalett.connecting_rooms = [hall]
kitchen.connecting_rooms = [hall]
mamma_rom.connecting_rooms = [hall]
stue.connecting_rooms = [hall, varanda]
varanda.connecting_rooms = [stue]
current_room = edo_room

#-------------character choice menu---------------------#

os.system("cls")
character = choose_character(character_choice)

#---------------------start game------------------------#

def start_game(character):
     print(f"You are playing as {character.name}")
     input("Press ENTER to start game")
    
start_game(character)

#---------------------battle menu------------------------#

def battle_menu():
    print("1. Attack")
    print("2. Use Special Ability")
    print("3. Use Item")
    choice = input("Choose an option: ")
    return choice

#--------------------battle system----------------------#

def Start_battle(character, Enemy):
    score = 0
    print("Battle Start!")

    while character.is_alive() and Enemy.is_alive():
        choice = battle_menu()

        if choice == "1":
            character.attack_enemy(Enemy)
        Enemy.health_bar()
        if not Enemy.is_alive():
            print(f"you've defeated {Enemy.name}!")
            score = 10
            break

        elif choice == "2":
            if character.s_ability == "Flour explosion":
                print("Special Ability: Flour Explosion")
                character.flour_explosion(Enemy)
            elif character.s_ability == "Kleptomania":
                print("Special Ability: Kleptomania")
                character.kleptomania(Enemy)
            elif character.s_ability == "Røyk":
                print("Special Ability: Røyk")
                character.røyk(Enemy)
            elif character.s_ability == "Insults":
                print("Special Ability: Insults")
                character.insults(Enemy)
            elif character.s_ability == "STG buff":
                print("Special Ability: STG buff")
                character.stg_buff(Enemy)
            elif character.s_ability == "MF ult":
                print("Special Ability: Nail Barrage")
                character.nail_barrage(Enemy)
            elif character.s_ability == "Sprenge shit":
                print("Special Ability: Sprenge Shit")
                character.at_barrage(Enemy)



        elif choice == "3":
            print("Your inventory:")
            for i, (item, quantity) in enumerate(character.inventory.items(), start=1):
                print(f"{i}. {item}: {quantity}")
            item_to_use = int(input("Choose an item to use: "))
            item_name = list(character.inventory.keys())[item_to_use - 1]
            character.use_item(item_name)


        if Enemy.is_alive():
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
total_enemies = 5 
enemies_killed = 0

score = 0
while True:
    os.system("cls")
    current_room.room_name()
    current_room.describe_room()
    Enemy = current_room.room_monster_display()
    if Enemy and Enemy.is_alive():
        Enemy.catch_phrase()

        result = Start_battle(character, Enemy)
        score += result
        print(f"Score {score}")
        if result > 0:
            enemies_killed += 1
        if not character.is_alive():
            print("GAME OVER")
            break 
        if enemies_killed == total_enemies:
            print("VICTORY! You have earned your peace!")
            break

    actions = ["Explore room", "Open chest", "Move to another room"]
    for i, actions in enumerate(actions, start=1):
        print(f"{i}. {actions}")
    choice = input("Choose an action: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(actions):
        choice = input("Invalid choice! Choose again: ")

    if choice == "1":
        os.system("cls")
        current_room.explore_room()
    elif choice == "2":
        found_potion = None
        if current_room.chest:
            print("Press ENTER to open chest")
            input()
            found_potion = current_room.chest.open()

        if found_potion is not None:
            found_potion.use_health_potion(character)
            print(f"You found a {found_potion.name}, you have now {character.hp} HP")
            input("Press ENTER to continue")
        else:
            #print("No potion found in the chest.")
            input("Press ENTER to continue")
    elif choice == "3":
        os.system("cls")
        neste_rom = current_room.room_menu()
        current_room = current_room.connecting_rooms[int(neste_rom)]
    else:
        print("Invalid choice! Choose again: ")





 
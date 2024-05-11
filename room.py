import os
from character import character

class Room:
    def __init__(self, name, enemy, chest, description, explore_options={}, connecting_rooms = []):
        self.name = name
        self.enemy = enemy
        self.chest = chest
        self.description = description
        self.explore_options = explore_options
        self.connecting_rooms = connecting_rooms

    def room_name(self):
        print(self.name)

    def describe_room(self):
        print(self.description)

    def room_monster_display(self):
        if self.enemy == None:
            print("It is quiet here...")
        elif self.enemy.is_alive():
            print(f"OH NO! {self.enemy.name} is aproaching!")
            return self.enemy
        
    def room_chest_display(self):
        if self.chest == None:
            print("There is no chest here...")
        else:
            print("There is a chest in the room")
            return self.chest


    def room_menu(self):
        print(f"Rommet har {len(self.connecting_rooms)} dører")
    
        for i in range(len(self.connecting_rooms)):
            print(f"{i+1}) go inside {self.connecting_rooms[i].name}.")
        
        choice = input("Choose from the menu: ")
        while len(choice) < 1 or int(choice) > len(self.connecting_rooms):
            choice = input("Invalid choice! choose again")
        return int(choice) - 1
    
    def explore_room(self):
        while True:
            os.system("cls")
            print("You can explore the following:")

            for i, option in enumerate(self.explore_options.keys(), start=1):
                print(f"{i}. {option}")

            print(f"{len(self.explore_options) + 1}. Go back")
            choice = input("Choose an option: ")
            while not choice.isdigit() or int(choice) < 1 or int(choice) > len(self.explore_options) + 1:
                choice = input("Invalid choice! choose again: ")

            if int(choice) == len(self.explore_options) + 1:
                break
            list(self.explore_options.values())[int(choice) - 1]()


    def explore_wardrobe():
        print("There is a pile of stinky clothes and alot of one sided socks")
        input("Press ENTER to continue")

    def explore_under_bed(character):
        print("There is a chest under the bed!")
        character.hp += 20
        print("You found a Health potion in the chest and gained 20 HP!")
        input("Press ENTER to continue")

    def explore_bookshelf():
        print("There are many books here, but none of them are interesting")
        input("Press ENTER to continue")

    def explore_meggies_bed(character):
        print("There is a chest under Meggies's bed!")
        character.hp += 30
        print("You found a HP potion in the chest and gained 30 HP!")
        input("Press ENTER to continue")

    def explore_shoe_rack():
        print("There are way too many shoes here!")
        input("Press ENTER to continue")

    def explore_toy_box():
        print("Theres something deeper hidden here..")
        input("Press ENTER to continue")

    def explore_toilett(character):
        print("There is a chest behind the toilet!")
        character.hp += 40
        print("You found a Healing Juice in the chest and gained 40 HP!")
        input("Press ENTER to continue")

    def explore_shower(character):
        print("There is a 4 meter long olive python in the shower!!")
        character.hp -= 40
        print("The python bit you and you lost 40 HP!")
        input("Press ENTER to continue")
        if not character.is_alive():
            print("GAME OVER!")
            raise SystemExit

    def explore_refrigerator():
        print("There's something rotten in the fridge. ew..")
        input("Press ENTER to continue")

    def explore_food_bowl(character):
        print("You eat the bowl of very yummy food. Yum!")
        character.hp += 40
        print("You gained 40 HP!")
        input("Press ENTER to continue")

    def explore_behind_tv(character):
        print("There is a spider behind the TV!")
        character.hp -= 10
        print("The spider bit you and you lost 10 HP!")
        input("Press ENTER to continue")
        if not character.is_alive():
            print("GAME OVER!")
            raise SystemExit

    def explore_under_couch(character):
        print("You found a chest under the couch!")
        character.hp += 20
        print("You found a Health potion in the chest and gained 20 HP!")
        input("Press ENTER to continue")

    def explore_window(character):
        print("As you were looking out from the Window you slipped and fell through it!!")
        character.hp -= 10000
        if not character.is_alive():
            print("GAME OVER!")
            raise SystemExit

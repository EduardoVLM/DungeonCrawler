import os

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

    def explore_under_bed():
        print("There is a chest under the bed!")
        input("Press ENTER to continue")

    #lage flere explore options på alle rommene



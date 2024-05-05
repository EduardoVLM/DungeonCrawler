class Room:
    def __init__(self, name, enemy, chest, description, connecting_rooms = []):
        self.name = name
        self.enemy = enemy
        self.chest = chest
        self.description = description
        self.connecting_rooms = connecting_rooms

    def room_name(self):
        print(self.name)

    def describe_room(self):
        print(self.description)

    def room_monster_display(self):
        if self.enemy == None:
            print("It is quiet here...")
        else:
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

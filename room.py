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


    def room_menu(self):
        print(f"Rommet har {len(self.connecting_rooms)} dører")
    
        for i in range(len(self.connecting_rooms)):
            print(f"{i+1}) go inside {self.connecting_rooms[i].name}.")
        
        choice = int(input("Choose from the menu: "))
        return choice - 1

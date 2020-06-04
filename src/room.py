# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc, items):
        self.name = name
        self.desc = desc
        self.items = items
    def __repr__(self):
        return f"You are currently in the {self.name} room. {self.desc}"
    def look(self):
        if len(self.items) > 0:
            print("You find: ")
            for item in self.items:
                print(item)
        else: 
            print("There are no items to be found in this room.")
    def currentItems(self):
        return self.items
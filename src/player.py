# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.inventory = ['test']
        print(currentRoom)
    def __repr__(self):
        return f"{self.currentRoom}"
    def check_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(item)
        else:
            print("Your inventory is empty, right now.")
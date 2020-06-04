from room import Room
from player import Player
from item import Item
from time import sleep

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [Item('Coin', "It's a single coin of unknown value. You can't make out anything printed on it as it is covered in rust and dirt.", 5), Item('Bucket', "It's an empty bucket, great for carrying liquids. You might need it, later.", 2)]),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", []),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", []),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", []),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", []),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['overlook'].s = room['foyer']
room['foyer'].e = room['narrow']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal command, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

class Adv:
    def __init__(self, go=None):
        current_room = room['outside']
        game_over = False
        player = Player(current_room)
        while game_over is not True:
            sleep(1)
            command = input("Enter a command in which to move (n, s, e, or w) or look with 'look', enter q to end the game: \n")
            split_command = command.split(" ")
            try: 
                if 'n' in split_command or 's' in split_command or 'e' in split_command or 'w' in split_command:
                    current_room = getattr(current_room, command.split(" ")[1])
                    player.currentRoom = current_room
                    print(player)
                elif 'look' in split_command:
                    current_room.look()
                    sleep(1)
                    print(player.current_room)
                elif 'get' in split_command:
                    player.inventory.append(split_command(" ")[1])
                    print("Trying to get item")
                elif 'inventory' in split_command:
                    print("Looking at inventory")
                    print(player.inventory)
                elif 'q' in split_command:
                    print("Thank you for playing!")
                    sleep(1)
                    break
                if current_room == room['treasure'] and 'Treasure' in player.inventory():
                    sleep(5)
                    print("Congratulations! You Win!")
                    game_over = True
            except:
                pass
                # print("Can't go that direction, right now.")
instance = Adv()
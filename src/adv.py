from room import Room
from player import Player
from time import sleep

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']
room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

class Adv:
    def __init__(self, go=None):
        current_room = room['outside']
        game_over = False
        player = Player
        player(current_room)
        while game_over is not True:
            
            sleep(1)
            direction = input("Enter a direction in which to move: ")
        
            if direction == 'north' or direction == 'North' or direction == 'NORTH' or direction == 'n' or direction == 'N':
                direction = 'n_to'
            elif direction == 'south' or direction == 'South' or direction == 'SOUTH' or direction == 's' or direction == 'S':
                direction = 's_to'
            elif direction == 'west' or direction == 'West' or direction == 'WEST' or direction == 'w' or direction == 'W':
                direction = 'w_to'
            elif direction == 'east' or direction == 'East' or direction == 'EAST' or direction == 'e' or direction == 'E':
                direction = 'e_to'
            else:
                print("That's not a valid direction.")
            try: 
                current_room = getattr(current_room, direction)   
                player(current_room)
                if current_room == room['treasure']:
                    sleep(5)
                    print("Congratulations! You Win!")
                    game_over = True
            except:
                print("Cannot move in that direction right now.")
                sleep(1)
                player(current_room)    
instance = Adv()
''' Text Adventure Game!'''


class Room:
    '''This class is all the rooms in the game'''

    def __init__(self, description, north, east, west, south):
        # This sets up all the variables in the class

        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.south = south


def main():
    # Main program function
    room_list = list()

    room = Room("You are in the foyer. To the north is the hall. To the east is the dining room. To the west is the guest bedroom",3,5,1,None)
    room_list.append(room)
    room = Room("You are in the guest bedroom. To the north is the master bedroom. To the east is the foyer.",2,0,None,None)
    room_list.append(room)
    room = Room("You are in the master bedroom. To the south is the guest bedroom. To the east is the hall.",None,3,None,1)
    room_list.append(room)
    room = Room("You are in the hall. To the north is the balcony. To the south is the foyer. To the west is the master bedroom. To the east is the kitchen",6,4,2,0)
    room_list.append(room)
    room = Room("You are in the kitchen. To the south is the dining room. To the west is the hall", None, None, 3, 5)
    room_list.append(room)
    room = Room("You are in the dining room.To the north is the kitchen. To the west is the foyer.", 4, None, 0, None)
    room_list.append(room)
    room = Room("You are in the balcony. To the south is the hall", None, None, None, 3)
    room_list.append(room)

    current_room = 0



    done = False

    while done == False:
        print()
        print(room_list[current_room].description)

        print()
        what_do = input(str("Which direction do you want to head in? Choose a direction: "))

        # making the input case insensitive
        what_do = what_do.lower()

        # North Direction
        if what_do == "n" or what_do == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can't go that way!")
                print()
            else:
                current_room = next_room

        # South Direction
        elif what_do == "s" or what_do == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can't go that way!")
                print()
            else:
                current_room = next_room

        # East Direction
        elif what_do == "e" or what_do == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You can't go that way!")
                print()
            else:
                current_room = next_room

        # West Direction
        elif what_do == "w" or what_do == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can't go that way!")
                print()
            else:
                current_room = next_room

        # Quit Command
        elif what_do == "q" or what_do == "quit":
            print("Bye Bye!")
            done = True

        else:
            print("I don't understand what you are saying.")

main()
# Alexis Perdue

def show_instructions():
    # print game instructions and commands
    print('Welcome to Curse of the Forgotten Manor!')
    print('Collect all 6 cursed artifacts to escape the haunted mansion.')
    print("Beware: Encounter Lady Thorne before you collect all 6 artifacts and you're trapped forever!")
    print('Move commands: go North, go South, go East, go West')
    print("Add to inventory: get 'item name'")
    print('-' * 40)


def show_status(current_room, inventory, rooms):
    # print players current room
    # print their current inventory
    # print item if applicable

    print('You are in the', current_room)
    print('Inventory:', inventory)
    item = rooms[current_room].get('item')
    if item and item not in inventory:
        print('you see a', item)
    print('-' * 40)


def main():
    # define rooms, directions, and items

    rooms = {

        'Foyer': {'West': 'Dining Room'},
        'Dining Room': {'East': 'Foyer', 'North': 'Living Room', 'item': 'Broken Pocket Watch'},
        'Living Room': {'South': 'Dining Room', 'West': 'Basement', 'East': 'Library', 'North': 'Kitchen',
                        'item': 'Vintage Record Player'},
        'Library': {'West': 'Living Room', 'North': 'Master Bedroom', 'item': 'Old Key'},
        'Master Bedroom': {'South': 'Library', 'item': 'Portrait Frame'},
        'Basement': {'East': 'Living Room', 'item': 'Antique Locket'},
        'Kitchen': {'South': 'Living Room', 'East': 'Attic', 'item': 'Crystal Ball'},
        'Attic': {'West': 'Kitchen', 'item': 'Lady Thorne'}  # Villain Room
    }

    current_room = 'Foyer'
    inventory = []
    total_items = 6

    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        command = input('Enter your move:\n').strip().lower()

        if command.startswith('go'):
            direction = command[3:].capitalize()
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                # if player enters the villain room
                if rooms[current_room].get('item') == 'Lady Thorne':
                    print('You see Lady Thorne')
                    if len(inventory) == total_items:
                        print('You have defeated Lady Thorne with the artifacts! You win!')
                    else:
                        print("OH NO, You've been caught! GAME OVER!")
                    print('Thanks for playing the game. Hope you enjoyed it!')
                    break
            else:
                print("You can't go that way!")

        elif command.startswith('get'):
            item_name = command[4:].strip().title()
            room_item = rooms[current_room].get('item')
            if room_item and item_name == room_item:
                if item_name not in inventory:
                    inventory.append(item_name)
                    print('{item_name} retrieved!')
                    del rooms[current_room]['item']
                else:
                    print('You already picked that up.')
            else:
                print("Can't get {item_name}!")
        else:
            print('Invalid Input!')

        # Winning Condition
        if len(inventory) == total_items:
            print('You have collected all cursed artifacts and escaped the Forgotten Manor!')
            print('Congratulations, you win!')
            print('Thanks for playing the game. Hope you enjoyed it!')
            break


if __name__ == '__main__':
    main()

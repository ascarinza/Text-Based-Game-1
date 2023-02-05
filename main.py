# Austin Scarinza Final Text Game Project

# Explains the instructions of the game
def instructions():
    print('\nWelcome to the Amusement Park Game!')
    print('Move commands: go South, go North, go East, go West.')
    print('Collect all 6 items and make it to the back gate before encountering the clown.')
    print('You can only escape though the back gate after all items are collected.')
    print('Add item to inventory by : get "item name"\n')


# Shows the user their room
def user_status(user_room, user_inventory, rooms):
    print('You are at the {}.'.format(user_room))
    print('{} : {}'. format('Inventory', user_inventory))
    if 'Item' in rooms[user_room] and (rooms[user_room]['Item'] not in user_inventory):
        print('You see a {}'.format(rooms[user_room]['Item']))
    print('-' * 30)


# Takes in current room and returns new room/ same room if they don't move
def user_movement(user_room, rooms, inventory):
    org_room = user_room
    valid_move = ['go North', 'go South', 'go West', 'go East']
    user_move = input('Enter your move: ')
    if user_move not in valid_move:
        while user_move not in valid_move:
            print('Invalid movement.')
            user_move = input('Enter your move: ')
    print()
    user_move = user_move.split()
    movement = user_move[1]
    for x in rooms:
        if x == user_room and movement in rooms[user_room]:
            new_room = rooms[user_room][movement]
            break
        else:
            new_room = org_room
    if new_room == org_room:
        print("You can't go that way!")
    if new_room == 'Back Gate' and len(inventory) == 6:
        new_room = 'Winner'

    return new_room


def second_move(user_move, user_room, rooms, inventory):
    org_room = user_room
    print()
    user_move = user_move.split()
    movement = user_move[1]
    for x in rooms:
        if x == user_room and movement in rooms[user_room]:
            new_room = rooms[user_room][movement]
            break
        else:
            new_room = org_room
    if new_room == org_room:
        print("You can't go that way!")
    if new_room == 'Back Gate' and len(inventory) == 6:
        new_room = 'Winner'

    return new_room


def collections(user_room, inventory, rooms):
    if 'Item' in rooms[user_room] and (rooms[user_room]['Item'] not in inventory):
        current_item = rooms[user_room]['Item']
        valid = ['go North', 'go South', 'go West', 'go East', 'get ' + current_item]
        user_move = input('Enter your move: ')
        directions = ['go North', 'go South', 'go West', 'go East']
        if user_move not in valid:
            while user_move not in valid:
                print('Invalid movement.')
                user_move = input('Enter your move: ')
        if user_move == 'get ' + current_item:
            inventory.append(current_item)
            print('{} retrieved!'.format(current_item))
            print()
            user_status(user_room, inventory, rooms)
        if user_move in directions:
            return user_move


# main base of the program
def main():
    rooms_lib = {
        'Ticket Office': {'North': 'Cafeteria', 'East': 'Roller Coaster'},
        'Roller Coaster': {'North': 'Fun House', 'West': 'Ticket Office', 'Item': 'Shirt'},
        'Fun House': {},
        'Cafeteria': {'South': 'Ticket Office', 'North': 'Drop Tower', 'West': 'Ferris Wheel',
                      'East': 'Fun House'},
        'Ferris Wheel': {'East': 'Cafeteria', 'West': 'Tea Cups', 'Item': 'Nose'},
        'Tea Cups': {'South': 'Log Ride', 'East': 'Ferris Wheel', 'Item': 'Wig'},
        'Log Ride': {'North': 'Tea Cups', 'Item': 'Make Up Set'},
        'Drop Tower': {'West': 'Water Park', 'South': 'Cafeteria', 'North': 'Back Gate',
                       'Item': 'Shoes'},
        'Water Park': {'East': 'Drop Tower', 'Item': 'Pants'},
        'Back Gate': {'South': 'Drop Tower'}
    }

    inventory = []

    start_room = 'Ticket Office'
    current_room = start_room

    instructions()

    directions = ['go North', 'go South', 'go West', 'go East']

    while current_room != 'Fun House' and current_room != 'Winner':

        user_status(current_room, inventory, rooms_lib)
        movement = collections(current_room, inventory, rooms_lib)
        if movement in directions:
            current_room = second_move(movement, current_room, rooms_lib, inventory)
        else:
            current_room = user_movement(current_room, rooms_lib, inventory)
    if current_room == 'Fun House':
        print('Oh No! You ended up at the Fun House')
        print('The clown got you!!')
        print('Game Over')
    else:
        print('Congrats! You made it to the gate in a disguised and escaped the park!')


main()

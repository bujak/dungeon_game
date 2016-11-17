import os, random, time
from inventory import *
from hp_system import *
from challenges import challenge1
from challenges import challenge2
from challenges import challenge3

def gameboard(x=5, y=5):
    list1 = []
    for row in range(x):
        list1.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                list1[row].append('#')
            else:
                list1[row].append('.')
    return list1

def create_box(tab):
    box_x = random.randrange(3,27)
    box_y = random.randrange(2,88)
    tab[box_x][box_y] = '#'
    tab[box_x-1][box_y+1] = '#'
    tab[box_x+1][box_y-1] = '#'
    tab[box_x][box_y-1] = '#'
    tab[box_x][box_y+1] = '#'
    tab[box_x+1][box_y+1] = '#'
    tab[box_x-1][box_y] = '#'
    tab[box_x-1][box_y-1] = '#'
    tab[box_x+1][box_y] = '#'

def put_box(box_count,tab):
    for i in range(1,box_count):
         create_box(tab)


def coloring_list():
    color_list = ["'\033[95m'", "'\033[94m'", "'\033[92m'", "'\033[93m'"]
    rand_color = random.choice(color_list)
    print(rand_color)

def clear_tab(tab):
    for i in range(len(tab)):
        tab[i] = [ ]
        for k in range(len(tab[i])):
            tab[i][k]=[ ]


    return tab

def settable(tab):
    tab[rows-2][columns//2]= "@"
    return tab


def printing_gameboard(list1):
    import os
    os.system("clear")
    for i in list1:
        print(''.join(i))


# printing_gameboard(gameboard(20,20))

def create_lvl(box_count):
    create_box()
    coloring_list()
    put_box(box_count)


# printing_gameboard(tab)

def escape(tab):
    os.system("clear")
    f = open('complete.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    time.sleep(1)
    os.system("clear")
    clear_tab(tab)
    coloring_list()
    new_lvl(tab)


def new_lvl(tab):

    tab = gameboard(rows,columns)
    settable(tab)
    create_box(tab)
    put_box(2,tab)
    positioning_loot(tab)
    positioning_exit(tab)
    positioning_python(tab)
    while True:
        printing_gameboard(tab)
        char_hp = increasing_char_hp(inventory_numbers,cloth_armour_class)
        print("You currently have %d health points!\n" %char_hp)
        key = getch()
        move(key,tab)
        if key == "i":
            try:
                print_inventory(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! Go loop for some loot!")

        if key ==  "r":
            try:
                dropping_item(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! You don't have anything to remove from inventory!")


def challenge1_main(tab):
    t0 = 0
    t1 = 0
    t2 = 0

    os.system("clear")
    print("Challenge 1\n\n")
    print("You have to collect 5 loot in 15 seconds. Good luck!\n")
    z = input("Are you ready? (y - yes, n - no)")
    if z == "y":
        t0 = time.time()

        t2 = t0 + 40

        t1 = time.time()
        # if sum(inventory_numbers.values()) > 4:

        total = t1 - t0
        tab = gameboard(rows,columns)



    settable(tab)
    create_box(tab)
    put_box(2,tab)
    positioning_exit(tab)
    positioning_loot(tab)
    while t2 < 40:
        printing_gameboard(tab)
        char_hp = increasing_char_hp(inventory_numbers,cloth_armour_class)
        print("You currently have %d health points!\n" %char_hp)
        key = getch()
        move(key,tab)
        if key == "i":
            try:
                print_inventory(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! Go loop for some loot!")

        if key ==  "r":
            try:
                dropping_item(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! You don't have anything to remove from inventory!")

    print("You were too slow :( Try again!")
    time.sleep(3)
    challenge1_main(tab)




def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def find(sign, tab):
    for row in range(len(tab)):
        for column in range(len(tab[0])):
            if tab[row][column] == sign:
                return [row,column]


def positioning_exit(gameboard):
    '''Positioning triggers for exit on gameboard'''

    tries = 0

    while tries != 1:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#"  or "C":
            gameboard[loot_position_row][loot_position_column] = "E"


            tries += 1

    tries2 = 0
    while tries2 != 1:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#"  or "C":
            gameboard[loot_position_row][loot_position_column] = "E"

            tries2 += 1

    tries3 = 0
    while tries3 != 1:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#"  or "C" or "S":
            gameboard[loot_position_row][loot_position_column] = "B"

            tries3 += 1

    tries4 = 0
    while tries4 != 2:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#"  or "C" or "S" or "B":
            gameboard[loot_position_row][loot_position_column] = "C"

            tries4 += 1

    return gameboard

def positioning_python(gameboard):
    '''Positioning triggers for exit on gameboard'''

    tries = 0

    while tries != 1:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#"  or "C" or "E":
            gameboard[loot_position_row][loot_position_column] = "S"


            tries += 1


def positioning_boss(gameboard):
    tries = 0
    while tries != 1:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#" or "C" or "E" or "S":
            gameboard[loot_position_row][loot_position_column] = "B"


            tries += 1


def move(key,tab):

    coordinates = find("@",tab)
    x = coordinates[0]
    y = coordinates[1]

    if key == "a":
        if tab[x][y-1] == "#":
            tab[x][y] = "@"

        else:
            if tab[x][y-1] == "L":
                adding_loot(inventory_weight, inventory_numbers)
                tab[x][y] == "."
                tab[x][y-1] = "."

            elif tab[x][y-1] == "E":
                escape(tab)
                tab[x][y] == "."
                tab[x][y-1] = "."

            elif tab[x][y-1] == "S":
                challenge2(inventory_numbers,weapons_damage)
                tab[x][y] == "."
                tab[x][y-1] = "."

            elif tab[x][y-1] == "B":
                challenge3(challenge3(inventory_numbers, inventory_weight, cloth_armour_class, food_restore, char_hp))
                tab[x][y] == "."
                tab[x][y-1] = "."

            

            else:
                tab[x][y] = "."
                tab[x][y-1] = "@"

    elif key == "d":
        if tab[x][y+1] == "#":
            tab[x][y] = "@"


        else:
            if  tab[x][y+1] == "L":
                adding_loot(inventory_weight, inventory_numbers)
                tab[x][y] == "."
                tab[x][y+1] = "."

            elif tab[x][y+1] == "E":
                escape(tab)
                tab[x][y] == "."
                tab[x][y+1] = "."

            elif tab[x][y+1] == "S":
                challenge2(inventory_numbers,weapons_damage)
                tab[x][y] == "."
                tab[x][y+1] = "."

            elif tab[x][y+1] == "B":
                challenge3(challenge3(inventory_numbers, inventory_weight, cloth_armour_class, food_restore, char_hp))
                tab[x][y] == "."
                tab[x][y+1] = "."

            else:
                tab[x][y] = "."
                tab[x][y+1] = "@"

    elif key == "w":

        if tab[x-1][y] == "#":
            tab[x][y] = "@"

        else:
            if tab[x-1][y] == "L":
                adding_loot(inventory_weight, inventory_numbers)
                tab[x][y] == "."
                tab[x-1][y] = "."

            elif tab[x-1][y] == "E":
                escape(tab)
                tab[x][y] == "."
                tab[x-1][y] = "."

            elif tab[x-1][y] == "S":
                challenge2(inventory_numbers,weapons_damage)
                tab[x][y] == "."
                tab[x-1][y] = "."

            elif tab[x-1][y] == "B":
                challenge3(challenge3(inventory_numbers, inventory_weight, cloth_armour_class, food_restore, char_hp))
                tab[x][y] == "."
                tab[x-1][y] = "."

            else:
                tab[x][y] = "."
                tab[x-1][y] = "@"

    elif key == "s":
        if tab[x+1][y] == "#":
            tab[x][y] = "@"


        else:
            if tab[x+1][y] == "L":
                adding_loot(inventory_weight, inventory_numbers)
                tab[x][y] == "."
                tab[x+1][y] = "."

            elif tab[x+1][y] == "E":
                escape(tab)
                tab[x+1][y] == "."

            elif tab[x+1][y] == "S":
                challenge2(inventory_numbers,weapons_damage)
                tab[x][y] == "."
                tab[x+1][y] = "."

            elif tab[x+1][y] == "B":
                challenge3(challenge3(inventory_numbers, inventory_weight, cloth_armour_class, food_restore, char_hp))
                tab[x][y] == "."
                tab[x+1][y] = "."


            else:
                tab[x][y] = "."
                tab[x+1][y] = "@"

    #elif key == "i":
        #print_inventory(inventory_weight, inventory_numbers) #prints inventory

    elif key == "q":
        os.system(quit())


'''
elif tab[x][y-1] == "C":
    challenge1(inventory_numbers)
    tab[x][y] == "."
    tab[x][y-1] = "."

elif tab[x][y-1] == "B":
    challenge3(inventory_weight, inventory_numbers,  cloth_armour_class, food_restore, char_hp)
    tab[x][y] == "."
    tab[x][y-1] = "."
'''
'''
    elif tab[x][y+1] == "C":
        challenge1(inventory_numbers)
        tab[x][y] == "."
        tab[x][y+1] = "."

    elif tab[x][y+1] == "B":
        challenge3(inventory_weight, inventory_numbers,  cloth_armour_class, food_restore, char_hp)
        tab[x][y] == "."
        tab[x][y+1] = "."
'''
'''
elif tab[x-1][y] == "C":
    challenge1(inventory_numbers)
    tab[x][y] == "."
    tab[x-1][y] = "."

elif tab[x-1][y] == "B":
    challenge3(inventory_weight, inventory_numbers,  cloth_armour_class, food_restore, char_hp)
    tab[x][y] == "."
    tab[x-1][y] = "."
'''
'''
elif tab[x+1][y] == "C":
    challenge1(inventory_numbers)
    tab[x+1][y] == "."

elif tab[x+1][y] == "B":
    challenge3(inventory_weight, inventory_numbers, cloth_armour_class, food_restore, char_hp)
    tab[x+1][y] == "."
'''


# if __name__ == '__main__':
columns = 90 #columns
rows = 30 # rows

inventory_weight = {}
inventory_numbers = {}
# tab = gameboard(rows,columns)
    # new_lvl(tab)

'''
    tab[rows-2][columns//2]= "@"

    create_lvl(20)
    positioning_loot(tab)
    positioning_challenges(tab)

    while True:
        printing_gameboard(tab)

        char_hp = increasing_char_hp(inventory_numbers,cloth_armour_class)
        print("You currently have %d health points!\n" %char_hp)
        key = getch()
        move(key)
        if key == "i":
            try:
                print_inventory(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! Go loop for some loot!")

        if key ==  "r":
            try:
                dropping_item(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! You don't have anything to remove from inventory!")
'''

import os, random

columns = 90 #columns
rows = 30 # rows
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

def create_box():
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

def put_box(box_count):
    for i in range(1,box_count):
         create_box()


def coloring_list():
    color_list = ["'\033[95m'", "'\033[94m'", "'\033[92m'", "'\033[93m'"]
    rand_color = random.choice(color_list)
    print(rand_color)


def generating_loot():
    '''Function that generates loot'''
    clothes = {'chromium chainmail' : 4, 'boots of Master Java' : 2, 'Elif gloves': 0.5, 'belt of Loop': 0.5}
    food = {'bitten apple': 0.1, 'cookies': 0.1, 'beer':0.2, 'vodka':0.2}

    weapons = {'rainbow sword of sir Charlie the Unicode': 0.5, 'dwarven axe from Lambda':0.5, 'bow from Ascii':0.6,
                   'warhammer of 40 000 lost souls': 1}

    other = {'gemstone from Git continent': 0.1, 'ruby': 0.1,'gold coin' : 0.1, 'mysterious code': 0.1}
    loot_gen = (clothes,food,weapons,other) #chooses randomly type of content
    type_of_loot = loot_gen[random.randrange(0,3)] #chooses randomly item (key)
    generating_item = random.sample(list(type_of_loot), 1)
    loot_item = ''.join(generating_item)
    loot = {loot_item: type_of_loot[loot_item]} #generates dict with randomly choosen item (item:weight)

    return loot


def positioning_loot(gameboard):
    '''Positioning triggers for loot on gameboard'''
    gameboard_loot_position_rows = []
    gameboard_loot_position_columns = []
    tries = 0

    while tries != 8:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#":
            gameboard[loot_position_row][loot_position_column] = "L"
            gameboard_loot_position_rows.append(loot_position_row)
            gameboard_loot_position_columns.append(loot_position_column)
            tries += 1

    return gameboard


def adding_loot(inventory_weight, inventory_numbers):
    looting = generating_loot()
    item = ''.join(looting.keys())

    if len(inventory_weight.keys()) == 0:
        inventory_weight.update(looting)
    else:
        if item in inventory_weight:

            inventory_weight[item] += looting[item]
        else:
            inventory_weight.update(looting)

    if len(inventory_numbers.keys()) == 0:
        inventory_numbers[item] = 1
    else:
        if item in inventory_numbers:

            inventory_numbers[item] += 1

        else:
            inventory_numbers[item] = 1

    #print_inventory(inventory_weight, inventory_numbers)
    return inventory_weight, inventory_numbers

def print_inventory(inventory_weight, inventory_numbers,  order = "count,desc"):
    '''Function that displays inventory in a specific order or without any
    order.The order input argument can be as follow: empty (by default) which
    means that the inventory is unordered;
    "count.desc" means the inventory is ordered in descending order;
    "count,asc" means the inventory is ordered in ascending order.
    '''

    clothes = ('clothes', 'chromium chainmail', 'boots of Master Java', 'Elif gloves', 'belt of Loop')
    food = ('food', 'bitten apple', 'cookies', 'beer', 'vodka')

    weapons = ('weapons', 'rainbow sword of sir Charlie the Unicode', 'dwarven axe from Lambda', 'bow from Ascii',
                   'warhammer of 40 000 lost souls')

    other = ('other', 'gemstone from Git continent', 'ruby','gold coin' , 'mysterious code')
    len_keys = []

    for key in inventory_weight.keys():
        len_keys.append(len(key))

    max_len_item_name = (max(len_keys))  #calculates the maximum length of key
    max_len_weight = len(str(max(inventory_weight.values())))  #calculactes max length
                                                        #of value

    sorted_values = sorted(inventory_numbers.values())

    print('Inventory:\n')

    column_item_num = 5
    column_item_type = 9
    column_item_name = (max_len_item_name + column_item_num + column_item_type + 4)
    column_weight = int(column_item_name + column_item_num + column_item_type + 1)
    item_types = (clothes,food,weapons,other)

    all_columns = column_item_num + column_item_type + column_item_name + column_weight

    print("{0:>{1}}".format("count", column_item_num)
          + "{0:>{1}}".format("type", column_item_type) + "{0:>{1}}".format("name", column_item_name)
          + "{0:>{1}}".format("weight",column_weight))

    print("{0:>{1}}".format("-" * all_columns, all_columns))

    total = 0
    if order == "count,desc":
        for item in sorted(inventory_numbers, key = inventory_numbers.get, reverse = True):
            total += int(inventory_numbers.get(item))
            loot_type = ""

            for it_type in range(len(item_types)):
                if item in item_types[it_type]:
                    loot_type += item_types[it_type][0]

            print('{0:>{1}}'.format(str(inventory_numbers.get(item)), column_item_num)
                  + '{0:>{1}}'.format(loot_type, column_item_type) + '{0:>{1}}'.format(item, column_item_name)
                  + '{0:>{1}}'.format(str(inventory_weight.get(item)), column_weight))

    elif order == "count,asc":
        for item in sorted(inventory_numbers, key = inventory.get, reverse = False):
            total += int(inventory_numbers.get(item))
            print('{0:>{1}}'.format(str(inventory.get(item)), column_item_num)
            + '{0:>{1}}'.format(item, column_keys))

    else:
        for item in inventory:
            total += inventory_numbers.get(item)
            print('{0:>{1}}'.format(str(inventory.get(item)), column_values)
                  + '{0:>{1}}'.format(item, column_keys))

    print("{0:>{1}}".format("-" * all_columns, all_columns))
    print('Total number of items: %d.' % total)

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

tab = gameboard(rows,columns)
tab[rows-2][columns//2]= "@"
# printing_gameboard(tab)


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


def find(sign):
    for row in range(len(tab)):
        for column in range(len(tab[0])):
            if tab[row][column] == sign:
                return [row,column]

def move(key):

    coordinates = find("@")
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
            else:
                tab[x][y] = "."
                tab[x+1][y] = "@"

    elif key == "i":
        print_inventory(inventory_weight, inventory_numbers)

    elif key == "q":
        os.system(quit())






if __name__ == '__main__':

    inventory_weight = {}
    inventory_numbers = {}

    create_lvl(20)
    positioning_loot(tab)

    while True:

        printing_gameboard(tab)
        key = getch()
        move(key)

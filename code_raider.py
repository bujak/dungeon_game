from inventory import*
from hp_system import*
import os
import random
import time
import sys


'''Global variables'''
columns = 90
rows = 30

inventory_weight = {}
inventory_numbers = {}


'''Welcome functions.'''


def welcome_to():
    """Opens welcome_to txt file"""
    f = open('welcome_to.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()


def coderaider():
    """Opens coderaider txt file"""
    f = open('coderaider.txt', 'r')
    file_contents = f.read()
    print('\033[92m' + file_contents + '\033[0m')
    f.close()


def intro():
    """Shows target of game, controls and asks user if he is ready"""
    print("1. YOUR TARGET OF THIS GAME\n")
    print("You have to pass three levels collecting some items, do some \
challenges and finally defeat a boss. \n")
    print("2. CONTROLS\n")
    print("To move up, press \"w\"")
    print("To move down, press \"s\"")
    print("To move left, press \"a\"")
    print("To move right, press \"d\" \n")
    print("To use your best weapon (if you have it), press \"t\" \n")
    print("\n To see credits press \"c\" ")
    print("To exit program press \"q\" \n \n \n ")
    print("3. A R E  Y O U  R E A D Y ???\n y - yes, n - no :(, c - credits, q - exit program")



def credits():
    """Show credits of the game"""
    os.system("clear")
    f = open('credits.txt', 'r')
    file_contents = f.read()
    print('\033[94m' + file_contents + '\033[0m')
    print("")
    print("")
    print("")
    print("OUR TEAM: \n")
    print("Piotr Balon")
    print("Michal Doniec")
    print("Tomek Bujakowski")
    print("Krzysiek Dzioba \n \n \n")

    print("WHO WHAT HAVE DONE:\n")
    print("Piotr - ASCII Master King")
    print("Michal - Item Thief, Master of Life and Unlife")
    print("Tomek - Level Developer")
    print("Krzysiek - Design Developer")
    time.sleep(5)
    f.close()
    main(tab, inventory_numbers, inventory_weight, cloth_armour_class)


'''General functions.'''


def gameboard(x=5, y=5):
    """Create list with # as borders and . as field"""
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
    """Create boxes of # in board"""
    box_x = random.randrange(3, 27)
    box_y = random.randrange(2, 88)
    tab[box_x][box_y] = '#'
    tab[box_x-1][box_y+1] = '#'
    tab[box_x+1][box_y-1] = '#'
    tab[box_x][box_y-1] = '#'
    tab[box_x][box_y+1] = '#'
    tab[box_x+1][box_y+1] = '#'
    tab[box_x-1][box_y] = '#'
    tab[box_x-1][box_y-1] = '#'
    tab[box_x+1][box_y] = '#'


def put_box(box_count, tab):
    '''Puts certain amount of boxes'''
    for i in range(1, box_count):
        create_box(tab)


def coloring_list():
    '''Print in color chosen by random'''
    color_list = ["'\033[95m'", "'\033[94m'", "'\033[92m'", "'\033[93m'"]
    rand_color = random.choice(color_list)
    print(rand_color)


def clear_tab(tab):
    '''Clears board'''
    for i in range(len(tab)):
        tab[i] = []
        for k in range(len(tab[i])):
            tab[i][k] = []
    return tab


def settable(tab):
    '''Putting @ mark on board'''
    tab[rows - 2][columns // 2] = "@"
    return tab


def printing_gameboard(list1):
    '''Print board in user-friendly format'''
    import os
    # os.system("clear")
    for i in list1:
        print(''.join(i))


def create_lvl(box_count):
    '''Prepares board for level'''
    create_box()
    coloring_list()
    put_box(box_count)


def escape(tab):
    '''Escape of level'''
    os.system("clear")
    # f = open('complete.txt', 'r')
    # file_contents = f.read()
    # print(file_contents)
    # f.close()
    time.sleep(1)
    os.system("clear")
    clear_tab(tab)


def getch():
    '''Getting one typed input sign character, some kind of magic'''
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
    '''Finds sign in gameboard'''
    for row in range(len(tab)):
        for column in range(len(tab[0])):
            if tab[row][column] == sign:
                return [row, column]


def move(key, tab, inventory_numbers, inventory_weight, cloth_armour_class):
    ''''Move function, also check for events on board and start them'''

    coordinates = find("@", tab)
    x = coordinates[0]
    y = coordinates[1]

    if key == "a":
        '''when player moves to the border, # do not change'''
        if tab[x][y-1] == "#":
            tab[x][y] = "@"

        else:
            '''Executing events when player touch sign'''
            if tab[x][y-1] == "L":
                adding_loot(inventory_weight, inventory_numbers)
                tab[x][y] == "."
                tab[x][y-1] = "."

            elif tab[x][y-1] == "B":
                boss_fight(inventory_weight, inventory_numbers, cloth_armour_class)
                tab[x][y] == "."
                tab[x][y-1] = "."

            elif tab[x][y-1] == "S":
                challenge2(inventory_numbers,inventory_weight, weapons_damage)
                tab[x][y] == "."
                tab[x][y-1] = "."
            else:
                '''Executing events when player touch sign'''
                tab[x][y] = "."
                tab[x][y-1] = "@"

    elif key == "d":
        if tab[x][y+1] == "#":
            tab[x][y] = "@"

        else:
            if tab[x][y+1] == "L":
                adding_loot(inventory_weight, inventory_numbers)
                tab[x][y] == "."
                tab[x][y+1] = "."

            elif tab[x][y+1] == "B":
                boss_fight(inventory_weight, inventory_numbers, cloth_armour_class)
                tab[x][y] == "."
                tab[x][y+1] = "."

            elif tab[x][y+1] == "S":
                challenge2(inventory_numbers, inventory_weight, weapons_damage)
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

            elif tab[x-1][y] == "B":
                boss_fight(inventory_weight, inventory_numbers, cloth_armour_class)
                tab[x][y] == "."
                tab[x-1][y] = "."

            elif tab[x-1][y] == "S":
                challenge2(inventory_numbers, inventory_weight, weapons_damage)
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

            elif tab[x+1][y] == "B":
                boss_fight(inventory_weight, inventory_numbers, cloth_armour_class)
                tab[x+1][y] == "."

            elif tab[x+1][y] == "S":
                challenge2(inventory_numbers, inventory_weight, weapons_damage)
                tab[x][y] == "."
                tab[x+1][y] = "."
            else:
                tab[x][y] = "."
                tab[x+1][y] = "@"

    elif key == "q":
        os.system(quit())


'''Challenges'''


def are_you_ready(key, tab, inventory_numbers, inventory_weight, cloth_armour_class):
    """Asks user if he is ready to play"""
    commands_list = ["y", "n", "c", "q"]
    while key not in commands_list:
        print("Wrong input")
        key = getch()
        are_you_ready(key, tab, inventory_numbers, inventory_weight, cloth_armour_class)
    if key == "y":
        time_challenge(tab, inventory_numbers, inventory_weight, cloth_armour_class)
    elif key == "n":
        os.system("clear")
        f = open('idiot.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        time.sleep(2)
        f.close()
        main(tab, inventory_numbers, inventory_weight, cloth_armour_class)
    elif key =="c":
        credits()
    elif key =="q":
        sys.exit()


def time_challenge(tab, inventory_numbers, inventory_weight, cloth_armour_class):
    '''In time challenge player have to collect items in set time'''

    os.system("clear")
    print("Challenge 1\n\n")
    print("You have to collect 5 loot in 20 seconds. Good luck!\n")
    z = input("Are you ready? (y - yes, n - no) ")
    if z == "y":

        tab = gameboard(rows, columns)
        settable(tab)
        create_box(tab)
        put_box(25, tab)
        positioning_loot(tab)
        coloring_list()
        time0 = time.time()

        while True:
            time1 = time.time()
            total = time1 - time0
            printing_gameboard(tab)

            key = getch()
            move(key, tab, inventory_numbers, inventory_weight, cloth_armour_class)
            char_hp = increasing_char_hp(inventory_numbers, cloth_armour_class)

            print("You currently have %d health points!\n" % char_hp)

            try:
                print_inventory(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! Go loop for some loot!")
            # if key == "i":

            if key == "r":
                try:
                    dropping_item(inventory_weight, inventory_numbers)
                except ValueError:
                    print('\n' * 30)
                    print("Inventory is empty! You don't have anything to remove.")

            if sum(inventory_numbers.values()) > 4:
                break
                # print("/n" * 30)
                # os.system("clear")
                # f = open('complete.txt', 'r')
                # file_contents = f.read()
                # print(file_contents)
                # time.sleep(3)

                new_lvl_python(tab, inventory_numbers, inventory_weight, cloth_armour_class)
        time1 = time.time()
        total = time1 - time0

        if total > 20:
            os.system("clear")
            f = open('youlose.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            time.sleep(6)
            main(tab, inventory_numbers, inventory_weight, cloth_armour_class)
        if total <=20:

            os.system("clear")
            f = open('complete.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            time.sleep(6)
            new_lvl_python(tab, inventory_numbers, inventory_weight, cloth_armour_class)

    if z == "n":
        print("Your loss ^^ ")
        time.sleep(2)
        time_challenge(tab, inventory_numbers, inventory_weight, cloth_armour_class)
    else:
        print("Wrong input ")
        time.sleep(2)
        time_challenge(tab, inventory_numbers, inventory_weight, cloth_armour_class)


def positioning_python(gameboard):
    '''Positioning triggers for exit on gameboard'''

    tries = 0

    while tries != 1:
        loot_position_column = random.randrange(1, 88)
        loot_position_row = random.randrange(1, 27)

        if gameboard[loot_position_row][loot_position_column] != "#":
            gameboard[loot_position_row][loot_position_column] = "S"

            tries += 1
    return gameboard


def new_lvl_python(tab, inventory_numbers, inventory_weight, cloth_armour_class):
    '''Creates and set level with Python encounter'''
    os.system("clear")
    tab = gameboard(rows, columns)
    settable(tab)
    create_box(tab)
    put_box(20, tab)
    positioning_python(tab)
    positioning_loot(tab)
    coloring_list()
    while True:
        printing_gameboard(tab)
        key = getch()
        move(key, tab, inventory_numbers, inventory_weight, cloth_armour_class)
        char_hp = increasing_char_hp(inventory_numbers, cloth_armour_class)
        print("You currently have %d health points!\n" % char_hp)
        # if key == "i":
        try:
            print_inventory(inventory_weight, inventory_numbers)
        except ValueError:
            print('\n' * 30)
            print("Inventory is empty! Go loop for some loot!")

        if key == "r":
            try:
                dropping_item(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! You don't have anything to remove from inventory!")


def challenge2(inventory_numbers, inventory_weight, weapons_damage):
    '''Challenge with python trampling'''
    os.system("clear")
    print("\033[1m Wooaaaaaaaa! Watch out! There is an extremly huge Python,\
which wants to eats you! You must defeat him! You must know, that he is not a \
normal Python. His HP recovers all of the time! If it gets doubled up you die! \n")
    print("Touch as many w, s, a, d as you can to trample him or use your \
weapon to defeat him. Your best weapon is on \"t\" key. Let's go!\n\n\n")
    time.sleep(3)  # ZROBIC DLUZEJ
    f = open('happy_python.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    time.sleep(3)  # I TEGO TEZ
    python_hp = 55
    stars_list = ["*"] * python_hp

    while python_hp > 0:
        t0 = time.time()
        os.system("clear")
        print("\033[1m Wooaaaaaaaa! Watch out! There is an extremly huge Python,\
which wants to eats you! You must defeat him! You must know, that he is not a \
normal Python. His HP recovers all of the time! If it gets doubled up you die! \n")
        print("Touch as many w, s, a, d as you can to trample him or use your \
weapon to defeat him. Your best weapon is on \"t\" key. Let's go!\n\n\n")
        f = open('python1.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        h = (''.join(stars_list))
        print('{:>103}'.format(h))
        r = 100  # CHANGE, IF YOU CHANGE PYTHON_HP. THIS VARIABLE IS MAX
        # PYTHON_HP, IF MORE - YOU LOSE
        key = getch()

        if len(stars_list) > r:
            os.system("clear")
            f = open('youlose.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            time.sleep(10)
            main(tab, inventory_numbers, inventory_weight, cloth_armour_class)
        if key == "q":
            break
        if key == "w" or key == "s" or key == "a" or key == "d":
            python_hp -= 1
            stars_list.remove("*")
            print(''.join(stars_list))

        if key == "t":
            best_weapon_in_inventory = []
            for key in inventory_numbers:

                if key in weapons_damage:
                    best_weapon_in_inventory.append(weapons_damage[key])
                    damage = max(best_weapon_in_inventory)
                else:
                    damage = 1
            python_hp -= damage

            # for i in range(damage):
            # stars_list.remove("*")

            if python_hp > 3:
                for i in range(damage):
                    stars_list.remove("*")
            print(''.join(stars_list))

        t1 = time.time()
        total = t1 - t0

        if total > 0.12:
            python_hp += 5
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")

        os.system("clear")
        if len(stars_list) < 6:
            print("\n\n\n \033[1m You defeated him, congratulations!")
            f = open('python4.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            time.sleep(3)
            new_lvl_boss(tab, inventory_numbers, inventory_weight, cloth_armour_class)
        f.close()


def positioning_boss(gameboard):
    '''Positioning triggers for Big Boss on the gameboard'''

    tries = 0

    while tries != 1:
        loot_position_column = random.randrange(1, 88)
        loot_position_row = random.randrange(1, 27)

        if gameboard[loot_position_row][loot_position_column] != "#":
            gameboard[loot_position_row][loot_position_column] = "B"

            tries += 1
    return gameboard


def new_lvl_boss(tab, inventory_numbers, inventory_weight, cloth_armour_class):
    '''Creates and set level with Python encounter'''
    os.system("clear")
    tab = gameboard(rows, columns)
    settable(tab)
    create_box(tab)
    put_box(23, tab)
    positioning_boss(tab)
    positioning_loot(tab)
    coloring_list()
    while True:
        printing_gameboard(tab)
        key = getch()
        move(key, tab, inventory_numbers, inventory_weight, cloth_armour_class)
        char_hp = increasing_char_hp(inventory_numbers, cloth_armour_class)
        print("You currently have %d health points!\n" % char_hp)
        # if key == "i":
        try:
            print_inventory(inventory_weight, inventory_numbers)
        except ValueError:
            print('\n' * 30)
            print("Inventory is empty! Go loop for some loot!")

        if key == "r":
            try:
                dropping_item(inventory_weight, inventory_numbers)
            except ValueError:
                print('\n' * 30)
                print("Inventory is empty! You don't have anything to remove from inventory!")


def number_generator():
    '''Number generator for boss fight'''

    a = str(random.randrange(1, 9))
    b = str(random.randrange(1, 9))

    while a == b:
        b = str(random.randrange(1, 9))
    b = a+b

    c = str(random.randrange(1, 9))
    while c in b:
        c = str(random.randrange(1, 9))
    c = b+c

    number = c
    return number


def check_win(user_input, number):
    '''checks win for boss fight'''
    if user_input == number:
        return True
    else:
        return False


def check(user_input, number):
    '''check user input for boss fight'''
    counter = 0
    hot = []
    for i in range(len(number)):
        if number[i] == user_input[i]:
                print('hot', end=' ')
                hot.append(i)
                counter += 1
    for i in range(len(number)):
        if i not in hot and user_input[i] in number:
            print('warm', end=' ')
            counter += 1
    if counter == 0:
        print("cold")


def boss_fight(inventory_weight, inventory_numbers, cloth_armour_class):
    '''boss encounter'''

    os.system("clear")
    coloring_list()
    char_hp = increasing_char_hp(inventory_numbers, cloth_armour_class)
    print('''I am thinking of a 3-digit number. Try to guess what it is.

        Here are some clues:

        When I say:    That means:

          Cold       No digit is correct.

          Warm       One digit is correct but in the wrong position.

          Hot        One digit is correct and in the right position.

        I have thought up a number. You have %d guesses to get it.''' % char_hp)
    random_number = number_generator()
    print(random_number)  # USUNAC TO NA KONCU

    print("You currently have %d ❤ health points." % char_hp)
    while True:
        key = getch()
        user_input = input("\nLives: %d ❤ \n" % (char_hp))
        #if user_input == "h":
            #print_inventory(inventory_weight, inventory_numbers)
            #restore_char_hp(inventory_numbers, inventory_weight, cloth_armour_class, char_hp)
        if len(user_input) != 3 or not user_input.isdigit():
            print("wrong input")
            continue
        win = check_win(user_input, random_number)
        if win == True:
            os.system("clear")
            f = open('youwin.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            f.close()
            time.sleep(10)
            credits()
            time.sleep(10)
            sys.exit()
        check(user_input, random_number)
        if char_hp == 0:
            print("\n"*20)
            print("*" * 5)
            os.system("clear")
            f = open('youlose.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            time.sleep(10)
            main(tab, inventory_numbers, inventory_weight, cloth_armour_class)
        char_hp -= 1


# if __name__ == '__main__':


tab = gameboard(rows, columns)


def main(tab, inventory_numbers, inventory_weight, cloth_armour_class):
    """Runs program as a tree"""
    inventory_weight = {}
    inventory_numbers = {}
    os.system("clear")
    welcome_to()
    time.sleep(1)
    coderaider()
    time.sleep(1)
    intro()
    key = getch()
    are_you_ready(key, tab, inventory_numbers, inventory_weight, cloth_armour_class)

main(tab, inventory_numbers, inventory_weight, cloth_armour_class)

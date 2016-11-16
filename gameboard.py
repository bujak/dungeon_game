import os, random, time


columns = 90
rows = 30

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


tab = gameboard(rows,columns)
tab[rows-2][columns//2]= "@"

def settable(gameboard):
    tab = gameboard(rows,columns)
    tab[rows-2][columns//2]= "@"
    return tab


def printing_gameboard(list1):
    import os
    os.system("clear")
    for i in list1:
        print(''.join(i))


def create_box(): #take random position and putting # around it
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

def put_box(box_count): #executing create_box X times
    for i in range(1,box_count):
         create_box()


def coloring_list(): #coloring printed gameboard with random color
    color_list = ["'\033[95m'", "'\033[94m'", "'\033[92m'", "'\033[93m'",
                  "'\033[91m'", "'\033[0m'", "\[\033[0;32m\]", "\[\033[0;35m\]",
                  "\[\033[0;35m\]", "\[\033[0;36m\]"]
    rand_color = random.choice(color_list)
    print(rand_color)


# def create_lvl(box_count):
#     create_box()
#     coloring_list()
#     put_box(box_count)



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


def escape():
    # esc_on_gameboard = True
    esc = find("E")
    player = find("@")
    f=None
    print(esc)
    print(player)
    if esc == None:
        os.system("clear")
        f = open('complete.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        f.close()
        time.sleep(3)
        os.system("clear")
        settable(gameboard)

def move(key):
    coordinates = find("@")
    x = coordinates[0]
    y = coordinates[1]
    escape()
    if key == "a":
        if tab[x][y-1] == "#":
            tab[x][y] = "@"
        else:
            tab[x][y] = "."
            tab[x][y-1] = "@"

    elif key == "d":
        if tab[x][y+1] == "#":
            tab[x][y] = "@"
        else:
            tab[x][y] = "."
            tab[x][y+1] = "@"
    elif key == "w":

        if tab[x-1][y] == "#":
            tab[x][y] = "@"
        else:
            tab[x][y] = "."
            tab[x-1][y] = "@"

    elif key == "q":
        os.system(quit())

    elif key == "s":
        if tab[x+1][y] == "#":
            tab[x][y] = "@"
        else:
            tab[x][y] = "."
            tab[x+1][y] = "@"



def positioning_escape(gameboard):
    '''Positioning triggers for loot on gameboard'''
    gameboard_loot_position_rows = []
    gameboard_loot_position_columns = []
    tries = 0

    while tries != 1:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#":
            gameboard[loot_position_row][loot_position_column] = "E"
            gameboard_loot_position_rows.append(loot_position_row)
            gameboard_loot_position_columns.append(loot_position_column)
            tries += 1

    return gameboard

def print_complete():
    os.system("clear")
    f = open('complete.txt', 'r')
    file_contents = f.read()
    print(file_contents)



    # if (esc[0] == player[0]) and (esc[1] == player[1]):
    #     coloring_list()
    #     return ("ok")

def new_lvl():
    tab = gameboard(rows,columns)
    tab[rows-2][columns//2]= "@"
    create_box()
    coloring_list()
    put_box(50)
    tab[rows-2][columns//2]= "@"
    positioning_escape(tab)


def letsplay():
    print(find("@"))
    while True:
        printing_gameboard(tab)
        escape()
        key = getch()
        move(key)


if __name__ == '__main__':


    create_box()
    coloring_list()
    put_box(20)
    tab[rows-2][columns//2]= "@"
    positioning_escape(tab)
    letsplay()



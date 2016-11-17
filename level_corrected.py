import random
import os
import time

columns = 90
rows = 30



def gameboard(x=30, y=90):
    tab = []
    for rzad in range(x):
        tab.append([])
        for kolumn in range(y):
            if rzad == 0 or rzad == x-1 or kolumn == 0 or kolumn == y-1:
                tab[rzad].append('#')
            else:
                tab[rzad].append('.')
    return tab


def printing_gameboard(tab):
    os.system("clear")
    for i in tab:
        print(''.join(i))

def clear_tab(tab):
    for i in range(len(tab)):
        tab[i] = [ ]
        for k in range(len(tab[i])):
            tab[i][k]=[ ]

    print(tab)
    return tab

def settable(tab):
    tab[rows-2][columns//2]= "@"
    return tab


def create_box(tab): #take random position and putting # around it
    box_x = random.randrange(3,27)
    box_y = random.randrange(2,88)
    tab[box_x][box_y] = '#'
    #tab[box_x-1][box_y+1] = '#'
    tab[box_x+1][box_y-1] = '#'
    #tab[box_x][box_y-1] = '#'
    tab[box_x][box_y+1] = '#'
    #tab[box_x+1][box_y+1] = '#'
    tab[box_x-1][box_y] = '#'
    #tab[box_x-1][box_y-1] = '#'
    tab[box_x+1][box_y] = '#'
    return tab


def put_box(box_count): #executing create_box X times
    for i in range(1,box_count):
         create_box(tab)


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


def move(key, tab):
    coordinates = find("@",tab)
    x = coordinates[0]
    y = coordinates[1]
    print(x)
    print(y)

    if key == "a":
        if tab[x][y-1] == "#":
            tab[x][y] = "@"
        else:
            if tab[x][y-1] == "E":
                escape(tab)

            else:
                tab[x][y] = "."
                tab[x][y-1] = "@"

    elif key == "d":
        if tab[x][y+1] == "#":
            tab[x][y] = "@"
        else:
            if tab[x][y+1] == "E":
                escape(tab)

            else:
                tab[x][y] = "."
                tab[x][y+1] = "@"
    elif key == "w":

        if tab[x-1][y] == "#":
            tab[x][y] = "@"
        else:
            if tab[x-1][y] == "E":
                escape(tab)

            else:
               tab[x][y] = "."
               tab[x-1][y] = "@"

    elif key == "q":
        os.system(quit())

    elif key == "s":
        if tab[x+1][y] == "#":
            tab[x][y] = "@"
        else:
            if tab[x+1][y] == "E":
                escape(tab)

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

def coloring_list(): #coloring printed gameboard with random color
    color_list = ["'\033[95m'", "'\033[94m'", "'\033[92m'", "'\033[93m'",
                  "'\033[91m'", "'\033[0m'", "\[\033[0;32m\]", "\[\033[0;35m\]",
                  "\[\033[0;35m\]", "\[\033[0;36m\]"]
    rand_color = random.choice(color_list)
    print(rand_color)

def escape(tab):
    #esc = find("E")

    #player = find("@")


    os.system("clear")
    #f = open('complete.txt', 'r')
    #file_contents = f.read()
    #print(file_contents)
    #f.close()
    time.sleep(1)
    os.system("clear")
    clear_tab(tab)
    new_lvl(tab)
    #printing_gameboard(tab)

    #positioning_escape(tab)
        # tab = gameboard()
    #coloring_list()
    #create_box()

    #put_box(10)





def new_lvl(tab):

    tab = gameboard()
    settable(tab)
    create_box(tab)
    put_box(2)
    positioning_escape(tab)
    while True:
        printing_gameboard(tab)
        key = getch()
        move(key,tab)
    return tab

if __name__ == '__main__':
    tab = gameboard(rows,columns)
    new_lvl(tab)

    '''tab = gameboard()
    settable(tab)
    create_box()
    put_box(10)
    positioning_escape(tab)
    game = 0
    while game == 0:
        printing_gameboard(tab)
        key = getch()
        move(key)
        escape(tab)
        '''

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
                tab[rzad].append('x')
            else:
                tab[rzad].append('.')
    return tab


def printing_gameboard(tab):
    os.system("clear")
    for i in tab:
        print(''.join(i))


def settable(tab):
    tab[rows-2][columns//2]= "@"
    return tab


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
    return tab


def put_box(box_count): #executing create_box X times
    for i in range(1,box_count):
         create_box()


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

def escape():
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
        tab[rows-2][columns//2]= "@"
        positioning_escape(tab)

tab = gameboard()
settable(tab)
create_box()
put_box(20)
positioning_escape(tab)
while True:
    escape()
    printing_gameboard(tab)
    key = getch()
    move(key)

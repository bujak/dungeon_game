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




if __name__ == '__main__':

    create_lvl(40)

    while True:
        printing_gameboard(tab)
        key = getch()
        move(key)

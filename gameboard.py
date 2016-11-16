<<<<<<< HEAD
import os
columns = 90 #columns
rows = 30 # rows
def gameboard(x=5, y=5):
    list1 = []
    for row in range(x):
        list1.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                list1[row].append('#')
=======
#blebkflkdb
#komentarz Tomka
#komentarz krzycha
#komentarz Piotrusia
def tablica(x=5, y=5):
    lista = []
    for rzad in range(x):
        lista.append([])
        for kolumn in range(y):
            if rzad == 0 or rzad == x-1 or kolumn == 0 or kolumn == y-1:
                lista[rzad].append('#')
>>>>>>> cac092d0674baf1ce6d91a91464a778bb88af233
            else:
                list1[row].append('.')
    return list1


def printing_gameboard(list1):
    import os
    os.system("clear")
    for i in list1:
        print(''.join(i))


# printing_gameboard(gameboard(20,20))

tab = gameboard(rows,columns)
tab[rows-2][columns//2]= "@"
printing_gameboard(tab)


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


while True:
    key = getch()
    move(key)
    printing_gameboard(tab)

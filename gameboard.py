#blebkflkdb
def tablica(x=5, y=5):
    lista = []
    for rzad in range(x):
        lista.append([])
        for kolumn in range(y):
            if rzad == 0 or rzad == x-1 or kolumn == 0 or kolumn == y-1:
                lista[rzad].append('#')
            else:
                lista[rzad].append('.')
    return lista


def drukowanie_tablicy(lista):
    import os
    os.system("clear")
    for i in lista:
        print(''.join(i))


# drukowanie_tablicy(tablica(20,20))

tab = tablica(14,14)
tab[1][1]= "@"
drukowanie_tablicy(tab)

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




def move(key):
    def find(sign):
        for rzad in range(len(tab)):
            for kolumna in range(len(tab[0])):
                if tab[rzad][kolumna] == sign:
                    return [rzad,kolumna]


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

    elif key == "s":
        if tab[x+1][y] == "#":
            tab[x][y] = "@"
        else:
            tab[x][y] = "."
            tab[x+1][y] = "@"


while True:
    key = getch()
    move(key)
    drukowanie_tablicy(tab)

from gameboard import tab, printing_gameboard, columns, rows
import random

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

for i in range(1,106):
    create_box()
printing_gameboard(tab)

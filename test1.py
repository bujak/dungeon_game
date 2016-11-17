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

def printing_gameboard(list1):
    import os
    os.system("clear")
    for i in list1:
        print(''.join(i))


def clear_tab(tab):
    for i in range(len(tab)):
        tab[i] = [ ]
        for k in range(len(tab[i])):
            tab[i][k]=[ ]

    print(tab)
    return tab



if __name__ == '__main__':
    tab = gameboard(30,90)
    printing_gameboard(tab)
    clear_tab(tab)
    printing_gameboard(tab)
    tab = gameboard(30,90)
    tab[28][45] = "@"
    printing_gameboard(tab)

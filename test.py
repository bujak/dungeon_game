

import os, random, csv

class GameBoard:

    def __init__(self):
        self.columns = 90
        self.rows = 30
        self.list1 = []
        self.tab = []
        self.box_count=9

    def gameboard(self):

        for row in range(self.columns):
            self.list1.append([])
            for column in range(self.rows):
                if row == 0 or row == self.columns - 1 or column == 0 or column == self.rows - 1:
                    self.list1[row].append('#')
                else:
                    self.list1[row].append('.')
        return self.list1

    def create_box(self): #take random position and putting # around it
        box_x = random.randrange(3,27)
        box_y = random.randrange(2,88)
        self.tab[box_x][box_y] = '#'
        self.tab[box_x - 1][box_y + 1] = '#'
        self.tab[box_x + 1][box_y - 1] = '#'
        self.tab[box_x][box_y - 1] = '#'
        self.tab[box_x][box_y + 1] = '#'
        self.tab[box_x + 1][box_y + 1] = '#'
        self.tab[box_x - 1][box_y] = '#'
        self.tab[box_x - 1][box_y - 1] = '#'
        self.tab[box_x + 1][box_y] = '#'

    def put_box(self): #executing create_box X times
        for i in range(1,self.box_count):
         self.create_box()


    def coloring_list(self): #coloring printed gameboard with random color
        color_list = ["'\033[95m'", "'\033[94m'", "'\033[92m'", "'\033[93m'",
                      "'\033[91m'", "'\033[0m'", "\[\033[0;32m\]", "\[\033[0;35m\]",
                      "\[\033[0;35m\]", "\[\033[0;36m\]"]
        rand_color = random.choice(color_list)
        print(rand_color)


    def printing_gameboard(self):
        import os
        os.system("clear")
        for i in self.list1:
            print(''.join(i))


    def create_lvl(self):
        self.create_box()
        self.coloring_list()
        self.put_box()


    def creating_board(self):
        self.tab = self.gameboard()
        self.tab[self.rows - 2][self.columns // 2]= "@"
        # printing_gameboard(selftab)


    def getch(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


    def find(self, sign):
        for row in range(len(self.tab)):
            for column in range(len(self.tab[0])):
                if self.tab[row][column] == sign:
                    return [row,column]

    def move(self, key):

        coordinates = self.find("@")
        x = coordinates[0]
        y = coordinates[1]
        if key == "a":
            if self.tab[x][y-1] == "#":
                self.tab[x][y] = "@"
            else:
                self.tab[x][y] = "."
                self.tab[x][y - 1] = "@"

        elif key == "d":
            if self.tab[x][y+1] == "#":
                self.tab[x][y] = "@"
            else:
                self.tab[x][y] = "."
                self.tab[x][y + 1] = "@"
        elif key == "w":

            if self.tab[x-1][y] == "#":
                self.tab[x][y] = "@"
            else:
                self.tab[x][y] = "."
                self.tab[x - 1][y] = "@"

        elif key == "q":
            os.system(quit())

        elif key == "s":
            if self.tab[x+1][y] == "#":
                self.tab[x][y] = "@"
            else:
                self.tab[x][y] = "."
                self.tab[x + 1][y] = "@"

    def main(self):
        self.creating_board()
        self.create_box()
        self.put_box()
        self.coloring_list()
        while True:
            self.printing_gameboard()
            key = self.getch()
            self.move(key)


game_board = GameBoard()
game_board.main()

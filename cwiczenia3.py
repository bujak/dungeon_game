import time
import os



def welcome_to():
    f = open('welcome_to.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

def coderaider():
    f = open('coderaider.txt', 'r')
    file_contents = f.read()
    print('\033[92m' + file_contents + '\033[0m')
    f.close()

def intro():
    print("1. YOUR TARGET OF THIS GAME\n")
    print("You have to pass three levels collecting some items, do some \
challenges and finally defeat a boss. \n")
    print("2. CONTROLS\n")
    print("To move up, press \"w\"")
    print("To move down, press \"s\"")
    print("To move left, press \"a\"")
    print("To move right, press \"d\" \n")
    print("3. A R E  Y O U  R E A D Y ???\n (y - yes =), n - no :( ))")

def getch():
    global ch
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def are_you_ready():
    if ch == "y":
        print("dziala") ##### TUTAJ ZMIENIC NA FUNKCJE MAIN GLOWNEGO PROGRAMU
    elif ch == "n":
        os.system("clear")
        f = open('idiot.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        time.sleep(2)
        f.close()
        main()

def main():
    os.system("clear")
    welcome_to()
    time.sleep(1)
    coderaider()
    time.sleep(1)
    intro()
    ch = getch()
    are_you_ready()

main()

import time
import os

def welcome_to():
    """Opens welcome_to txt file"""
    f = open('welcome_to.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

def coderaider():
    """Opens coderaider txt file"""
    f = open('coderaider.txt', 'r')
    file_contents = f.read()
    print('\033[92m' + file_contents + '\033[0m')
    f.close()

def intro():
    """Shows target of game, controls and asks user if he is ready"""
    print("1. YOUR TARGET OF THIS GAME\n")
    print("You have to pass three levels collecting some items, do some \
challenges and finally defeat a boss. \n")
    print("2. CONTROLS\n")
    print("To move up, press \"w\"")
    print("To move down, press \"s\"")
    print("To move left, press \"a\"")
    print("To move right, press \"d\" \n")
    print("3. A R E  Y O U  R E A D Y ???\n (y - yes =), n - no :( c - challenge1 v - challenge2))")

def getch():
    """Get one character from user without pressing enter"""
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
    """Asks user if he is ready to play"""
    if ch == "y":
        credits() ##### TUTAJ ZMIENIC NA FUNKCJE MAIN GLOWNEGO PROGRAMU
    elif ch == "n":
        os.system("clear")
        f = open('idiot.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        time.sleep(2)
        f.close()
        main()

    elif ch == "c": ##### PAMIETAC ZEBY TO ZMIENIC
        challenge1()

    elif ch == "v":
        challenge2()

    else:
        print("Wrong command")
        time.sleep(2)
        intro()


def challenge1():
    """Challenge 1 in level 1"""
    os.system("clear")
    print("Challenge 1\n\n")
    print("You have to collect 5 loot in 15 seconds. Good luck!\n")
    z = input("Are you ready? (y - yes, n - no)")
    if z == "y":
        t0 = time.time()
        t1 = input("Trwa pomiar czasu. Wprowadz cos, aby go zatrzymac")
            ##### PODSTAWIC TUTAJ FUNKCJE GLOWNY MAIN GRY I W NIEJ TRZEBA
            ##### NAPISAC, ZE ONA (main) PRZESTAJE DZIALAC, GDY ZDOBYTO 5 LOOTA.
        t1 = time.time()
        total = t1 - t0

        print("Hurra! You collect 5 loot. Let's check if you do it in less\
than 15 seconds... \n ")
        time.sleep(1)
        print("***")
        time.sleep(1)
        print("***")
        time.sleep(1)
        print("***")
        time.sleep(1)
        if total<=15:
            print("Yeah, you did it! You shall pass to next level!")
            ### WKLEIC TUTAJ 2 level
        else:
            print("You were too slow :( Try again!")
            time.sleep(3)
            challenge1()

def challenge2():

    os.system("clear")
    print("Wooaaaaaaaa! Watch out! There is an extremly huge Python,\
which wants to eats you! You must defeat him! You must know, that he is not a \
normal Python. His HP recovers all of the time!\n")
    print("Touch as many w, s, a, d as you can to trample him or use your \
weapon to defeat him. Your best weapon is on \"t\" key. Let's go!\n\n\n")
    time.sleep(1)
    f = open('happy_python.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    time.sleep(1)
    python_hp = 55
    stars_list = ["*"] * python_hp
    #print("dziala")
    #print(''.join(stars_list))


    while python_hp > 0:
        t0 = time.time()
        os.system("clear")
        print("Wooaaaaaaaa! Watch out! There is an extremly huge Python,\
which wants to eats you! You must defeat him! You must know, that he is not a \
normal Python. His HP recovers all of the time!\n")
        print("Touch as many w, s, a, d as you can to trample him or use your \
weapon to defeat him. Your best weapon is on \"t\" key. Let's go!\n\n\n")
        f = open('python1.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        h = (''.join(stars_list))
        print('{:>103}'.format(h))
        r = 100 ####### CHANGE, IF YOU CHANGE PYTHON_HP. THIS VARIABLE IS MAX
        #PYTHON_HP, IF MORE - YOU LOST
        key = getch()
        if len(stars_list) > r:
            print("You lost :( ")
            time.sleep(3)
            break #### PUT EXIT TO GAMEBOARD FUNCTION HERE
        if key == "q":
            break
        if key == "w" or key == "s" or key == "a" or key == "d":
            python_hp -=1
            stars_list.remove("*")
            print(''.join(stars_list))
        if key == "t":
            python_hp -=2            ###### YOU CAN CHANGE POWER OF WEAPON HERE
            if python_hp > 1:
                stars_list.remove("*")
                stars_list.remove("*")
            print(''.join(stars_list))
        t1 = time.time()
        total = t1 - t0

        if total > 0.15:
            python_hp+=5
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")

    print("You defeat him, congratulations!")
    time.sleep(3)
        ##### WYJSCIE DO GAMEBOARD
    f.close()


def credits():
    """Show credits of the game"""
    os.system("clear")
    f = open('credits.txt', 'r')
    file_contents = f.read()
    print('\033[94m' + file_contents + '\033[0m')
    print("")
    print("")
    print("")
    print("OUR TEAM: \n")
    print("Piotr")
    print("Michal")
    print("Tomek")
    print("Krzysiek")
    print(" ")
    print(" ")
    print(" ")
    print("WHO WHAT HAVE DONE:\n")
    print("Piotr - ASCII Master King")
    print("Michal - Item Thief")
    print("Tomek - Level Developer")
    print("Krzysiek - Design Developer")
    f.close()


def main():
    """Runs program as a tree"""
    os.system("clear")
    welcome_to()
    time.sleep(1)
    coderaider()
    time.sleep(1)
    intro()
    ch = getch()
    are_you_ready()

main()
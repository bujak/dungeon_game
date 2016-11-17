from inventory import *
from hp_system import *
from gameboard_test import *
import os
import random
import time


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


    print("3. A R E  Y O U  R E A D Y ???\n (y - yes =), n - no :( c - challenge1 \
v - challenge2 b - challenge3")

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
        time.sleep(0)         ##### TUTAJ ZMIENIC NA FUNKCJE MAIN GLOWNEGO PROGRAMU
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

    elif ch == "b":
        challenge3()

    elif ch == "k":
        credits()

    else:
        print("Wrong command")
        time.sleep(2)
        intro()


# def challenge1(tab):
#     """Challenge 1 in level 1"""
#     os.system("clear")
#     print("Challenge 1\n\n")
#     print("You have to collect 5 loot in 15 seconds. Good luck!\n")
#     z = input("Are you ready? (y - yes, n - no)")
#     if z == "y":
#         t0 = time.time()
#
#         if sum(inventory_numbers.values()) > 4:
#         #t1 = input("Trwa pomiar czasu. Wprowadz cos, aby go zatrzymac")
#             ##### PODSTAWIC TUTAJ FUNKCJE GLOWNY MAIN GRY I W NIEJ TRZEBA
#             ##### NAPISAC, ZE ONA (main) PRZESTAJE DZIALAC, GDY ZDOBYTO 5 LOOTA.
#             t1 = time.time()
#         total = t1 - t0
#
#         print("Hurra! You collect 5 loot. Let's check if you do it in less\
# than 15 seconds... \n ")
#         time.sleep(1)
#         print("          ***")
#         time.sleep(1)
#         print("          ***")
#         time.sleep(1)
#         print("          ***\n")
#         time.sleep(1)
#         if total<=15: ########### ILOSC CZASU NA ZEBRANIE LOOTA, DO OKIELZNANIA
#             print("Yeah, you did it! You shall pass to next level!")
#             ############################################## WKLEIC TUTAJ 2 level
#         else:
#             print("You were too slow :( Try again!")
#             time.sleep(3)
#             challenge1()

def challenge2():

    os.system("clear")
    print("\033[1m Wooaaaaaaaa! Watch out! There is an extremly huge Python,\
which wants to eats you! You must defeat him! You must know, that he is not a \
normal Python. His HP recovers all of the time! If it gets doubled up you die! \n")
    print("Touch as many w, s, a, d as you can to trample him or use your \
weapon to defeat him. Your best weapon is on \"t\" key. Let's go!\n\n\n")
    time.sleep(1) ### ZROBIC DLUZEJ
    f = open('happy_python.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    time.sleep(1) ### I TEGO TEZ
    python_hp = 55
    stars_list = ["*"] * python_hp


    while python_hp > 0:
        t0 = time.time()
        os.system("clear")
        print("\033[1m Wooaaaaaaaa! Watch out! There is an extremly huge Python,\
which wants to eats you! You must defeat him! You must know, that he is not a \
normal Python. His HP recovers all of the time! If it gets doubled up you die! \n")
        print("Touch as many w, s, a, d as you can to trample him or use your \
weapon to defeat him. Your best weapon is on \"t\" key. Let's go!\n\n\n")
        f = open('python1.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        h = (''.join(stars_list))
        print('{:>103}'.format(h))
        r = 100 ####### CHANGE, IF YOU CHANGE PYTHON_HP. THIS VARIABLE IS MAX
        #PYTHON_HP, IF MORE - YOU LOSE
        key = getch()
        if len(stars_list) > r:
            os.system("clear")
            f = open('youlose.txt', 'r')
            file_contents = f.read()
            print(file_contents)
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

        if total > 0.12:
            python_hp+=5
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")
            stars_list.append("*")

    os.system("clear")
    if len(stars_list) < 2:
        #stars_list.clear
        print("\n\n\n \033[1m You defeated him, congratulations!")
        f = open('python4.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        time.sleep(3)
        ##### WYJSCIE DO GAMEBOARD
    f.close()


def challenge3():
    import random
    import time
    import os
    def number_generator():

        a = str(random.randrange(1,9))
        b = str(random.randrange(1,9))

        while a == b:
           b = str(random.randrange(1,9))
        b=a+b

        c = str(random.randrange(1,9))
        while c in b:
           c = str(random.randrange(1,9))
        c=b+c

        number = c
        return number


    def check_win(user_input, number):
        if user_input == number:
            return True
        else:
            return False

    def check(user_input, number):
        counter = 0
        hot = []
        for i in range(len(number)):
            if number[i] == user_input[i]:
                    print('hot', end=' ')
                    hot.append(i)
                    counter += 1
        for i in range(len(number)):
            if i not in hot and user_input[i] in number:
                print('warm', end=' ' )
                counter += 1
        if counter == 0:
            print("cold")


    def main2():
        os.system("clear")
        print('''I am thinking of a 3-digit number. Try to guess what it is.

        Here are some clues:

        When I say:    That means:

          Cold       No digit is correct.

          Warm       One digit is correct but in the wrong position.

          Hot        One digit is correct and in the right position.

        I have thought up a number. You have 10 guesses to get it.''')
        random_number = number_generator()
        print(random_number) ###### USUNAC TO NA KONCU
        guess_count = 1
        while True:
            user_input = input("\nGuess #%d:\n" % (guess_count))
            if len(user_input) != 3 or not user_input.isdigit():
                print("wrong input")
                continue
            win = check_win(user_input, random_number)
            if win == True:
                os.system("clear")
                f = open('youwin.txt', 'r')
                file_contents = f.read()
                print(file_contents)
                f.close()
                time.sleep(3)
                ####### TUTAJ WSTAWIC WYJSCIE DO GAMEBOARD
                break
            check(user_input, random_number)
            if guess_count == 10:
                break
            guess_count += 1


    #if __name__ == '__main__':
    main2()





##################################################

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
    time.sleep(7)
    main()


def main():
    """Runs program as a tree"""
    tab = gameboard(rows,columns)
    os.system("clear")
    welcome_to()
    time.sleep(1)
    coderaider()
    time.sleep(1)
    intro()
    ch = getch()
    are_you_ready()
    # challenge1_main(tab)
    new_lvl(tab)
main()

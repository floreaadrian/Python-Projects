from domain import airplane, board
from random import randint


def ai_move():
    dir = randint(1, 4)
    x = 0
    y = 0
    if dir == 1:
        x = randint(2, 6)
        y = randint(3, 6)
    if dir == 2:
        x = randint(3, 6)
        y = randint(3, 7)
    if dir == 3:
        x = randint(3, 7)
        y = randint(3, 6)
    else:
        x = randint(3, 6)
        y = randint(2, 6)

    return airplane(x,y,dir)


def making_moves():
    k = 0
    while k < 2:
        player.print(False)
        print("Please enter the position you want to put your airplane and his direction: ")
        try:
            x = int(input("X: "))
            y = input("Y: ")
            if y in letters:
                y = int(letters[y])
                dir = int(input("Direction: "))
                ar = airplane(x, y, dir)
                if player.validate_move(ar,'player') == True:
                    k += 1
                    player.make_move(ar)
                    ar_ai=ai_move()
                    while ai.validate_move(ar_ai,'ai') == False:
                        ar_ai =ai_move()
                    ai.make_move(ar_ai)
            else:
                print("Invalid input!")
        except ValueError:
            print("X and Direction must be int!")

    player.print(False)


def help():
    s = "This is some game information: \n"
    s += "If the direction of the plane is 1 it will look like this: \n"
    s += "0 0 ^ 0 0 \n"
    s += "- - - - - \n"
    s += "0 0 | 0 0 \n"
    s += "0 - - - 0 \n"
    s += "If the direction of the plane is 2 it will look like this: \n"
    s += "0 0 | 0 \n"
    s += "| 0 | 0 \n"
    s += "| - | > \n"
    s += "| 0 | 0 \n"
    s += "0 0 | 0 \n"
    s += "If the direction of the plane is 3 it will look like this: \n"
    s += "0 - - - 0 \n"
    s += "0 0 | 0 0 \n"
    s += "- - - - - \n"
    s += "0 0 ˅ 0 0 \n"
    s += "If the direction of the plane is 4 it will look like this: \n"
    s += "0 | 0 0 \n"
    s += "0 | 0 | \n"
    s += "< | - | \n"
    s += "0 | 0 | \n"
    s += "0 | 0 0 \n"
    s += "The plane occupy all the position different from 0\n"
    print(s)


def playing():
    ok = True
    auto = True
    ply=player.get_board()
    while ok:
        vld = True
        x1 = 0
        y1 = 0
        while vld:
            try:
                print("Please enter the position of the attack")
                x = int(input("X: "))
                y = input("Y: ")
                if y in letters:
                    y = int(letters[y])
                    if ai.make_attack(x, y,'player') == True:
                        x=randint(x1-1,x1+1)
                        y=randint(y1-1,y1+1)
                        if auto == True:
                            while player.make_attack(x,y,'ai') == False:
                                x = randint(0, 7)
                                y = randint(0, 7)
                            if ply[x][y] == -2 or ply[x][y] == -4:
                                x1=x
                                y1=y
                        else:
                            while player.make_attack(x, y, 'ai') == False:
                                x = randint(x1 - 1, x1 + 1)
                                y = randint(y1 - 1, y1 + 1)
                            if ply[x][y] == -2 or ply[x][y] == -4:
                                x1=x
                                y1=y
                        vld = False
                else:
                    print("Y is not valid!")
            except ValueError:
                print("X must be int!")
        print("This is your board attacked:")
        player.print(False)
        print("This is the board you attacked:")
        ai.print(True)
        if player.isGameLoose() == True:
            print("You lost the game!")
            ok = False
        elif ai.isGameLoose() == True:
            print("You won the game")
            ok = False


player = board()
ai = board()
letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
           'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
help()
making_moves()
playing()

from domain import Point


class UserInterface:
    def __init__(self, game):
        self.__game = game

    def check(self):
        '''
        This funtion checks if someone won the game
        '''
        if self.__game.verifyWinPlayer() == True and self.__game.checkWin() == False:
            print("Human won")
            return True
        elif self.__game.verifyWinPlayer() == False and self.__game.checkWin() == True:
            print("Ai won")
            return True
        elif self.__game.verifyWinPlayer() == True and self.__game.checkWin() == True:
            print("Tie")
            return True
        return False

    def _start(self):
        print(self.__game)
        while True:
            valid = True
            if self.check() == True:
                return
            self.__game.makeMoveAi()
            print(self.__game)
            if self.check() == True:
                return
            while valid:
                '''
                Here we will read the input until it's valid
                '''
                try:
                    x = int(input("X cord: "))
                    y = int(input("Y cord: "))
                    sym = input("X or O: ")
                    point = Point(x - 1, y - 1, sym)
                    if self.__game.makeMovePlayer(point) == True:
                        valid = False
                    else:
                        print("Invalid move!")
                except ValueError:
                    print("X and Y must be int!")

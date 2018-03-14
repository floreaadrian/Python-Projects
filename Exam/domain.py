from random import randint


class Point:
    '''
    This class will hold the point in the board
    '''
    def __init__(self, x, y, symb):
        self._x = x
        self._y = y
        self._symb = symb


    def getX(self):

        return self._x


    def getY(self):
        return self._y


    def getSymb(self):
        return self._symb


class Board:
    def __init__(self):
        self._board = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0], ]


    def encode(self, x):
        '''
        Encode the board from numbers to o,x or space
        '''
        if x == 0:
            return " "
        elif x == 1:
            return "o"
        else:
            return "x"


    def __str__(self):
        '''
        The funtion that is called when print()
        :return:
        '''
        brd = self._board
        s = ""
        for i in range(0, 6):
            s += "+-" * 6 + "+" + "\n"
            s += "|"
            for j in range(0, 6):
                s += self.encode(brd[i][j]) + "|"
            s += "\n"
        s += "+-" * 6 + "+" + "\n"
        return s


    def valide_move(self, x, y):
        '''
        Validate the move by verifying if the space is empty and it is in the bounds
        '''
        if x >= 0 and x < 6 and y >= 0 and y < 6:
            if self._board[x][y] == 0:
                return True
        return False


    def makeMovePlayer(self, point):
        '''
        It makes the move for the player by the point it gets
        It won't make a move if the point isn't valid
        :return:
        '''
        x = point.getX()
        y = point.getY()
        symb = point.getSymb()
        if self.valide_move(x, y):
            if symb == "O":
                self._board[x][y] = 1
                return True
            elif symb == "X":
                self._board[x][y] = 2
                return True
        return False


    def verifyWinPlayer(self):
        '''
        Verify if thw player wins by going trough all the matrix
        '''
        for i in range(0, 6):
            for j in range(0, 6):
                if self._board[i][j] == 0:
                    return False
        return True


    def AiMove(self):
        '''
        Give the point for ai to move
        :return:
        '''
        brd = self._board
        for i in range(0, 6):
            for j in range(0, 6):
                if self.valide_move(i, j) == True:
                    self._board[i][j] = 1
                    if self.checkWin() == False:
                        self._board[i][j] = 2
                        if self.checkWin() == False:
                            self._board[i][j] = 0
                        else:
                            return
                    else:
                        return
        symX=0
        symO=0
        for i in range(0,6):
            for j in range(0,6):
                if brd[i][j] == 1:
                    symO+=1
                elif brd[i][j]==2:
                    symX+=1
        if symX > symO:
            return Point(randint(0, 5), randint(0, 5), "X")
        else:
            return Point(randint(0, 5), randint(0, 5), "O")


    def makeMoveAi(self):
        '''
        Make move ai
        It will get the point from another function
        :return:
        '''
        while True:
            pnt = self.AiMove()
            if pnt == None:
                return
            x = pnt.getX()
            y = pnt.getY()
            symb = pnt.getSymb()
            if self.valide_move(x, y) == True:
                if symb == "O":
                    self._board[x][y] = 1
                elif symb == "X":
                    self._board[x][y] = 2
                return


    def getBoard(self):
        return self._board


    def Empty(self):
        '''
        Will make the board empty for the tests
        :return:
        '''
        for i in range(0, 6):
            for j in range(0, 6):
                self._board[i][j] = 0


    def checkWin(self):
        a = self._board
        '''
        All of this if are hand written
        '''
        for i in range(0, 6):
            # Will check for every row the if there are 5 equal numbers different from 0
            if (a[i][0] == a[i][1] == a[i][2] == a[i][3] == a[i][4] or a[i][5] == a[i][1] == a[i][2] == a[i][3] == a[i][
                4]) and a[i][1] != 0:
                return True
            # Will check for every column if there are 5 equal numbers different from 0
            elif (a[0][i] == a[1][i] == a[2][i] == a[3][i] == a[4][i] or a[5][i] == a[1][i] == a[2][i] == a[3][i] ==
                  a[4][i]) and a[1][i] != 0:
                return True
        # the main diagonals
        # Will check for every main diagonal if there are 5 consecutive numbers different from 0
        if (a[0][0] == a[1][1] == a[2][2] == a[3][3] == a[4][4] or a[1][1] == a[2][2] == a[3][3] == a[4][4] == a[5][
            5]) and a[1][1] != 0:
            return True
        #under the main diagonal
        if (a[1][0] == a[2][1] == a[3][2] == a[4][3] == a[5][4] and a[1][0] != 0):
            return True
        #above the main diagonal
        if (a[0][1] == a[1][2] == a[2][3] == a[3][4] == a[4][5] and a[0][1] != 0):
            return True
        # the secondary diagonals
        # Will check for every secondary diagonal if there are 5 consecutive numbers different from 0
        if (a[0][5] == a[1][4] == a[2][3] == a[3][2] == a[4][1] or a[1][4] == a[2][3] == a[3][2] == a[4][1] == a[5][
            0]) and a[1][4] != 0:
            return True
        #above the second diagonal
        if a[0][4] == a[1][3] == a[2][2] == a[3][1] == a[4][0] and a[4][0] != 0:
            return True
        #below the second diagonal
        if a[1][5] == a[2][4] == a[3][3] == a[4][2] == a[5][1] and a[5][1] != 0:
            return True
        return False

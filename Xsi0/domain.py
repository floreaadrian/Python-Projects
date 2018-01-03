from random import randint


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y


class Board:
    def __init__(self):
        self._board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

    def makeMove(self, point, user):
        u = 0
        exc = "The space is already taken"
        if user == "player":
            u = 3
        else:
            u = 0
        if point.getX() < 3 and point.getX() > -1 and point.getY() < 3 and point.getY() > -1:
            if self._board[point.getX()][point.getY()] == -1:
                self._board[point.getX()][point.getY()] = u
            else:
                raise Exception(exc)
        else:
            raise Exception("Move outside the board")

    def isGameWon(self):
        for l in self._board:
            if sum(l) in [0, 9]:
                return True
        b = self._board
        for l in range(0, 3):
            if b[0][l] + b[1][l] + b[2][l] in [0, 9]:
                return True
        if b[0][0] + b[1][1] + b[2][2] in [0, 9]:
            return True
        if b[0][2] + b[1][1] + b[2][0] in [0, 9]:
            return True
        return False

    def avMoves(self):
        moves = []
        b = self._board
        for l in range(0, 3):
            for c in range(0, 3):
                if b[l][c] == -1:
                    moves.append(Point(l, c))
        return moves

    def isDraw(self):
        if self.avMoves() == []:
            return True
        return False

    def encode(self, number):
        if number == -1:
            return ' '
        if number == 0:
            return '0'
        if number == 3:
            return 'X'

    def __str__(self):
        result = ''
        lineNumber = 0
        for line in self._board:
            result += self.encode(line[0]) + '|' + self.encode(line[1]) + '|' + self.encode(line[2]) + '\n'
            if lineNumber in [0, 1]:
                result += '-----\n'
                lineNumber += 1
        return result


class Game:
    def __init__(self, board):
        self.__board = board

    def makeMoveAi(self):
        avalibleMoves = self.__board.avMoves()
        randMove = randint(0, len(avalibleMoves) - 1)
        self.__board.makeMove(avalibleMoves[randMove], "ai")

    def makeMovePlayer(self, point):
        self.__board.makeMove(point, "player")


class UserInterface:
    def __init__(self, game):
        self.__game = game
        self._start()

    def _start(self):
        crtPlayer = 3
        while self.__game.getBoard().isGameWon():
            print(self.__game.getBoard())
            if crtPlayer == 3:
                x = int(input("X cord: "))
                y = int(input("Y cord: "))
                point = Point(x,y)
                try:
                    self.__game.makeMovePlayer(point)
                    crtPlayer = 0
                except Exception as exc:
                    print(exc)
            else:
                self.__game.makeMoveAi()
                crtPlayer = 3
        print(self.__game.getBoard())
        if self.__game.getBoard().isDraw() == False:
            if crtPlayer ==3:
                print("Computer has won")
            elif crtPlayer == 0:
                print("Human has won")
        else:
            print("It's a draw")

GameBoard = Board()
print(GameBoard)
GameBoard.makeMove(Point(0, 0), "player")
GameBoard.makeMove(Point(-1, 0), "ai")
print(GameBoard)

Gm = Game(GameBoard)
ui = UserInterface(Gm)
ui._start()

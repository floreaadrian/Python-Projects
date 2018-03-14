from domain import Board
from Ui import UserInterface
class Game:
    '''
    This comunicates with the domain layer
    '''
    def __init__(self, board):
        self.__board = board

    def makeMoveAi(self):
        return self.__board.makeMoveAi()

    def makeMovePlayer(self, point):
        return self.__board.makeMovePlayer(point)

    def __str__(self):
        return str(self.__board)

    def verifyWinPlayer(self):
        return self.__board.verifyWinPlayer()

    def checkWin(self):
        return self.__board.checkWin()

GameBoard = Board()
Gm = Game(GameBoard)
ui = UserInterface(Gm)
ui._start()

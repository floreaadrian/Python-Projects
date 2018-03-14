class airplane:
    def __init__(self, x, y, direction):
        self._x = x
        self._y = y
        self._direction = direction


    def getX(self):
        return self._x


    def getY(self):
        return self._y


    def getDirection(self):
        return self._direction


class board:
    def __init__(self, ):
        '''
        Here we initialize the board,-1 will be an empty space
        '''
        self._board = [[-1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1]]


    def get_board(self):
        return self._board


    def cond1(self, x, y):
        '''
        We verify the the first condition
        '''
        k = self._board
        if k[x][y] == k[x][y - 2] == k[x][y - 1] == k[x][y + 1] == k[x][y + 2] == k[x - 1][y] == k[x + 1][y] == \
                k[x + 2][y - 1] == k[x + 2][y] == k[x + 2][y + 1] == -1:
            return True
        return False


    def cond2(self, x, y):
        '''
        We verify the the second condition
        '''
        k = self._board
        if k[x][y] == k[x][y - 2] == k[x][y - 1] == k[x][y + 1] == k[x - 1][y - 2] == k[x + 1][y - 2] == k[x - 2][y] == \
                k[x - 1][y] == k[x + 1][y] == k[x + 2][y] == -1:
            return True
        return False


    def cond3(self, x, y):
        '''
        We verify the the third condition
        '''
        k = self._board
        if k[x][y] == k[x][y - 2] == k[x][y - 1] == k[x][y + 2] == k[x][y + 2] == k[x + 1][y] == k[x - 1][y] == \
                k[x - 2][y] == k[x - 2][y - 1] == k[x - 2][y + 1] == -1:
            return True
        return False


    def cond4(self, x, y):
        '''
        We verify the the forth condition
        '''
        k = self._board
        if k[x][y] == k[x - 2][y] == k[x - 1][y] == k[x + 1][y] == k[x + 2][y] == k[x - 1][y + 2] == k[x][y + 2] == \
                k[x - 1][y + 2] == k[x][y + 1] == k[x][y - 1] == -1:
            return True
        return False


    def make1(self, avion):
        '''
        We put the avion in the 1 position
        '''
        k = self._board
        x = avion.getX() - 1
        y = avion.getY() - 1
        k[x][y] = k[x][y - 2] = k[x][y - 1] = k[x][y + 1] = k[x][y + 2] = k[x + 2][y] = k[x + 2][y + 1] = k[x + 2][
            y - 1] = 1
        k[x + 1][y] = 2
        k[x - 1][y] = 3


    def make2(self, avion):
        '''
        We put the avion in the 2 position
        '''
        k = self._board
        x = avion.getX() - 1
        y = avion.getY() - 1
        k[x][y - 1] = 1
        k[x - 1][y - 2] = k[x + 1][y - 2] = k[x - 2][y] = k[x - 1][y] = k[x + 1][y] = k[x + 2][y] = k[x][y - 2] = k[x][
            y] = 2
        k[x][y + 1] = 4


    def make3(self, avion):
        '''
        We put the avion in the 3 position
        '''
        k = self._board
        x = avion.getX() - 1
        y = avion.getY() - 1
        k[x][y] = k[x][y - 2] = k[x][y - 1] = k[x][y + 1] = k[x][y + 2] = k[x - 2][y - 1] = k[x - 2][y] = k[x - 2][
            y + 1] = 1
        k[x - 1][y] = 2
        k[x + 1][y] = 5


    def make4(self, avion):
        '''
        We put the avion in the 4 position
        '''
        k = self._board
        x = avion.getX() - 1
        y = avion.getY() - 1
        k[x][y + 1] = 1
        k[x][y] = k[x - 2][y] = k[x - 1][y] = k[x + 1][y] = k[x + 2][y] = k[x - 1][y + 2] = k[x][y + 2] = k[x + 1][
            y + 2] = 2
        k[x][y - 1] = 6


    def validate_move(self, avion, prt):
        '''
        THis function wil validate the move
        prt is for us to see if the player is the one who makes the moves
        because we give visual feedback only to him
        '''
        x = avion.getX()
        y = avion.getY()
        dir = avion.getDirection()
        out = 'Plane will be outside the board'
        over = 'This plane is over another plane'
        if dir == 1:
            if x < 2 or x > 6 or y < 3 or y > 6:
                if prt == 'player':
                    print(out)
            elif self.cond1(x - 1, y - 1) == False:
                if prt == 'player':
                    print(over)
            else:
                return True
        elif dir == 2:
            if x < 3 or x > 6 or y < 3 or y > 7:
                if prt == 'player':
                    print(out)
            elif self.cond2(x - 1, y - 1) == False:
                if prt == 'player':
                    print(over)
            else:
                return True
        elif dir == 3:
            if x < 3 or x > 7 or y < 3 or y > 6:
                if prt == 'player':
                    print(out)
            elif self.cond3(x - 1, y - 1) == False:
                if prt == 'player':
                    print(over)
            else:
                return True
        elif dir == 4:
            if x < 3 or x > 6 or y < 2 or y > 6:
                if prt == 'player':
                    print(out)
            elif self.cond4(x - 1, y - 1) == False:
                if prt == 'player':
                    print(over)
            else:
                return True
        else:
            print("Invalid direction")
            return False
        return False


    def make_move(self, avion):
        '''
        Making moves based on the avion param
        '''
        if avion.getDirection() == 1:
            self.make1(avion)
        elif avion.getDirection() == 2:
            self.make2(avion)
        elif avion.getDirection() == 3:
            self.make3(avion)
        else:
            self.make4(avion)


    def encode(self, number, attack):
        '''
        Here we encode the board
        :param number: The number on the board
        :param attack: If we need to hide were the airplanes are
        :return:
        '''
        if number == -2:
            return 'M'
        if number == -3:
            return 'H'
        if number == -4:
            return 'C'
        elif attack == True:
            return 'X'

        if attack == False:
            if number == -1:
                return '0'
            if number == 1:
                return '-'
            if number == 2:
                return '|'
            if number == 3:
                return '^'
            if number == 4:
                return '>'
            if number == 5:
                return '˅'
            if number == 6:
                return '<'


    def make_attack(self, x, y, player):
        '''

        :param x: The x position
        :param y: The y position
        :param player: We see who makes the atack
        :return: True if the attack was good and false if it was not
        '''
        x -= 1
        y -= 1
        brd = self._board
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            if not (brd[x][y] == -2 or brd[x][y] == -3 or brd[x][y] == -4):
                if brd[x][y] == -1:
                    brd[x][y] = -2
                    if player == 'player':
                        print("You missed! :(")
                elif brd[x][y] == 1 or brd[x][y] == 2:
                    if player == 'player':
                        print("Hit an airplane!")
                    brd[x][y] = -3
                else:
                    if player == 'player':
                        print("You crashed the airplane! :)")
                    brd[x][y] = -4
            else:
                if player == 'player':
                    print("You already attacked here!")
                return False
        else:
            if player == 'player':
                print("Attacked outside the board!")
            return False
        return True


    def isGameLoose(self):
        k = 0
        for line in self._board:
            for clm in line:
                if clm == -4:
                    k += 1
        if k == 2:
            return True
        return False


    def print(self, val):
        result = '    A B C D E F G H\n'
        result += '    ' + 15 * '-' + '\n'
        lines = 1
        for line in self._board:
            result += str(lines) + ' |'
            for clm in line:
                result += ' ' + self.encode(clm, val)
            result += '\n'
            lines += 1
        print(result)

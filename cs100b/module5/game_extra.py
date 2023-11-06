
class Game:
    def __init__(self):
        self.clearBoard()

    def clearBoard(self):
        #2d list of characters representing board
        self.board = [
            [' ' , ' ' , ' '],
            [' ' , ' ' , ' '],
            [' ' , ' ' , ' '],
        ]

        #turn variable
        self.turnX = True
        #gameover variable
        self.gameOver = False

    def takeTurn(self, x, y):
        #takes coordinates of click, and makes sure click is within board
        if self.board[int(x)][int(y)] != ' ' or self.gameOver:
            return
        
        #sets token to match turn
        if self.turnX:
            token = 'X'
        else:
            token = 'O'

        self.board[x][y] = token

        #flips turnx, whichever way it was
        self.turnX = not self.turnX


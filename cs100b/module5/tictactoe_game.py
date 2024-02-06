#oh, return is a useful, like, null value, remember that

class Game:
    def __init__(self):
        #clear board at start of new game
        self.clearBoard()

    def clearBoard(self):
        #matrix for squares
        self.board = [
                [' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']
            ]
        self.turnX = True
        self.gameOver = False

    def takeTurn(self, x, y):

        self.publicX = x
        self.publicY = y
        
        #duplicate tokens & infinite games not allowed
        if self.board[x][y] != ' ' or self.gameOver:
            return
        
        if self.turnX:
            token = 'X'
        else:
            token = 'O'

        #put token on board
        self.board[x][y] = token
        #switch turns
        self.turnX = not self.turnX

    def checkForWinner(self):
        self.gameOver = True
        for i in range(0,3):
            #use for loop check all horizontal & vertical rows
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]   
            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        #check for diagonals
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return self.board[2][0]

        #check for cat's game
        cat = True
        for r in range(0,3):
            for c in range(0,3):
                if self.board[r][c] == ' ':
                    cat = False
        if cat:
            return 'C'

        #sneakily turn it false at the bottom, for if all checks fail
        self.gameOver = False
        return ' '

        
        
        
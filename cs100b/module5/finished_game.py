class Game:
    def __init__(self):
        self.clearBoard()

    def clearBoard(self):
        # The board cells have three possible values: ' ', 'X', and 'O'
        self.board = [
                [' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']
            ]
        # It is X's turn?
        self.turnX = True
        self.gameOver = False

    def takeTurn(self, x, y):
        if self.board[x][y] != ' ' or self.gameOver:
            return

        if self.turnX:
            token='X'
        else:
            token='O'

        # Set the token in the right spot
        self.board[x][y] = token
        # Next person's turn
        self.turnX = not self.turnX

    def checkForWinner(self):
        #check rows and columns
        self.gameOver = True
        for i in range(0,3):
            #check each row
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            #check each column
            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        #now check diagonals
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return self.board[2][0]

        #Check for cat's game -- if there aren't any spaces in the board,
        #  then there's no place left to play. No winner
        cat = True
        for r in range(0,3):
            for c in range(0,3):
                if self.board[r][c] == ' ':
                    cat = False
        if cat:
            return 'C'

        #no winner, keep playing
        self.gameOver = False
        return ' '
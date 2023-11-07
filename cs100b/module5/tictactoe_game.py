class Game:
    def __init__(self):
        self.clearBoard()

    def clearBoard(self):
        self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' '],
        ]
        #are these variables archaic or something? they're not used anywhere else

        #wait what, 'self' is not defined?????
        #ohhhh, i forgot to indent
        self.TurnX = True
        self.gameOver = False

    def takeTurn(x, y):
        #oh wait, here's gameover again
        if self.board[x][y] == ' ' or self.gameOver:
            mainwindow.mousepressevent()
        
        if self.TurnX:
            token = 'X'

        else:
            token = 'O'

        #mark token on board
        self.board[x][y] = token
        #switch to opposite turn
        self.TurnX = not TurnX

    def checkForWinner(self):
        self.gameOver = True
        for i in range (0, 3):
            #remember to check if not blank
            if self.board != ' ' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                #winner is owner of chain
                return self.board[i][0]
            if self.board != ' ' and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        
        if self.board[2][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return self.board[2][0]
        
        #first mark cat true so you can go through and check if all the spaces are not blank
        cat = True
        #remember to go through both ways
        for x in range (0,3):
            for y in range (0, 3):
                if self.board[x][y] == ' ':
                    cat = False

        if cat == True:
            return 'C'

        self.gameOver = False
        return ' '


        #if you get through all the returns without returning anything, THEN game isn't over

        
    
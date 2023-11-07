class Game:
    def __init__(self):
        self.clearBoard()

    def clearBoard(self):
        self.board = [
                [' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']
            ]

        self.turnX = True
        self.gameOver = False

        #i'm going to initialize this just in case
        current_f = 0
        #we are sticking the data in here since... board is cleared at the end/start of every game, right?
        f = open('plays.txt', 'r')
        current_f = int(f.read())
        f.close()

        #oh, i forgot to put the filename in parentheses!!!
        f = open('plays.txt', "w")
        current_f += 1
        f.write(current_f)
        f.close()



    #oh wait, there WAS a difference in the arguments of takeTurn? how did that get there???
    def takeTurn(self, x, y):
        if self.board[x][y] != ' ' or self.gameOver:
            return
        
        if self.turnX:
            token = 'X'

        else:
            token = 'O'

        #mark token on board
        self.board[x][y] = token
        #switch to opposite turn
        #oh!! i DID forget to call the second one self.turnX!
        self.turnX = not self.turnX

    def checkForWinner(self):
        roundCount += 1
        self.gameOver = True
        for i in range (0, 3):
            #remember to check if not blank

            #well, i forgot to make this first self.board specific. is that what's messing it up? really?
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                #winner is owner of chain
                return self.board[i][0]
            if self.board[i][0] != ' ' and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        
        if self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
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

        
    
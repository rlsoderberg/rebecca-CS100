class game:
    def __init__(self):
        #clear board at start of new game
        self.clearBoard()

    def clearBoard(self):
        self.board = [
            [' '],[' '],[' ']
            [' '],[' '],[' ']
            [' '],[' '],[' ']
        ]
        self.turnX = True
        self.gameOver = False
        
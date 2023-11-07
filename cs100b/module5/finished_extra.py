import math
import sys
import random

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from finished_game import Game

class mainwindow(QWidget):
    def __init__(self, parent = None):
        #super window
        super(mainwindow, self).__init__(parent)
        #resize adjusts window size
        self.resize(500,500)
        self.setWindowTitle('Tic Tac Toe')

        #create game object using class from tictactoe_game
        self.game = Game()

    def paintEvent(self, event):
        qp = QPainter(self)
        #i saw SOME thing that had qp.begin, but it doesn't seem necessary here
        qp.setPen(QColor(0,0,0))

        #so this doesn't allow resizing, but it does work
        rect = QRect(0, 0, 500, 500)

        colsize = rect.width()//5
        rowsize = rect.height()//5

        qp.drawLine(colsize*2, rowsize, colsize * 2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize * 3, rowsize * 4)
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

        #now, this goes up here, with all the qp stuff!!!
        #remember, c and r come from INSIDE the loops!!!
        for r in range(0, 3):
            for c in range(0, 3):
                #use the game object we created, & self.board from Game
                if self.game.board[c][r] == 'X':
                    self.drawX(qp, c, r, colsize, rowsize)
                elif self.game.board[c][r] == 'O':
                    self.drawO(qp, c, r, colsize, rowsize)


    def drawX(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize

        #drawing x
        qp.drawLine(x, y, x+colsize, y+rowsize)
        qp.drawLine(x+colsize, y, x, y+rowsize)

    def drawO(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize

        #drawing o
        qp.drawEllipse(x, y, colsize, rowsize)

    #idk, i stole this mousePressEvent function from somewhere, and it's very mysterious
    #didn't help messing with the order of these functions, this is going at the bottom, and catching everything
    def mousePressEvent(self, event):
        #so we're passing event.position straight from nowhere, into the QUADRANT DETERMINATOR? mysterious
        size = self.size()
        
        #do this again down here
        colsize = size.width() // 5
        rowsize = size.height() // 5

        #for some reason it is important to have double parentheses here????
        col = math.floor((event.position().x() // colsize)) - 1
        row = math.floor((event.position().y() // rowsize)) - 1

        #oh, but i didn't have this, and this is important
        if col >= 0 and col < 3 and row >= 0 and row < 3:
            self.game.takeTurn(col, row)

        #so... this is a built-in function!
        self.repaint()

        #check for winner
        winner = self.game.checkForWinner()
        if winner != ' ':
            dlg = WinnerDialog(winner)
            if dlg.exec():
                self.game.clearBoard()
    
class WinnerDialog(QDialog):
    def __init__(self, winner):
        super().__init__()

        title = winner + ' has won!'
        if winner == 'C':
            title = "Cat's game"

        self.setWindowTitle(title)

        qbtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(qbtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        msg = "Congratulations " + winner + ". New Game?"
        if winner == 'C':
            msg = "No winner this time. New Game?"
        lbl = QLabel(msg)
        self.layout.addWidget(lbl)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    #well, when i try to call this here the program breaks!!!
    #w.clickEvent()
    

    #i still don't EXACTLY get the deal with sys.exit
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
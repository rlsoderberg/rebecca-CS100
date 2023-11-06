import sys
import math
import random
"""
#well, here's the thing, i'm trying to use this to find mouse event location
#but it seems to not work alongside all the other imports!!!
from PySide6.QtWidgets import *
#nvm, i'm going to try to stick to pyqt6
"""
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from game_extra import Game

class mainwindow(QWidget):
    def __init__(self, parent = None):
        #super window
        super(mainwindow, self).__init__(parent)
        #resize adjusts window size
        self.resize(500,500)
        self.setWindowTitle('Tic Tac Toe')

        #create game object using class from tictactoe_game
        self.game = Game()

    #yooo!!! i'm just putting everything in one function, just so i can work on it!!!

    #idk, i stole this mousePressEvent function from somewhere, and idk how it works
    def mousePressEvent(self, e):
        position = e.position()
        if e: 
            qp = QPainter(self)
            qp.setPen(QColor(0,0,0))

            rect = QRect(0, 0, 500, 500)

            #figure out how to deal with this Qpoint integer that QMouseEvent is giving me
            col = position.x()
            row = position.y()

            colsize = rect.width()//5
            rowsize = rect.height()//5

            qp.drawLine(colsize*2, rowsize, colsize * 2, rowsize*4)
            qp.drawLine(colsize*3, rowsize, colsize * 3, rowsize * 4)
            qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
            qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

            Game.clearBoard(self)
            Game.takeTurn(self, col, row)

            for r in range(0, 3):
                for c in range(0, 3):
                    #use the game object we created, & self.board from Game
                    if self.game.board[col][row] == 'X':
                        self.drawX(qp, col, row, colsize, rowsize)
                    elif self.game.board[col][row] == 'O':
                        self.drawO(qp, col, row, colsize, rowsize)

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

import sys
import math
import random
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from game_extra import Game

class mainwindow(QWidget):
    def __init__(self, parent = None):
        #i'm actually making proper comments now because i need to understand this new code!!!
        super(mainwindow, self).__init__(parent)
        #resize adjusts window size
        self.resize(500,500)
        self.setWindowTitle('Tic Tac Toe')

        #create game object using class from tictactoe_game
        self.game = Game()

    #well, this is what i got so far, and it broke when i clicked it, so that's a good sign
    def clickEvent(self):
        event = self.clicked.connect(mainwindow.mousePressEvent)
        pos = PySide2.QtWidgets.QGraphicsSceneMouseEvent.pos()
        if event:
            self.repaint(pos)


        #alright!!! we're taking drastic measures against this paint error!!!
        

    def paintEvent(self, pos):
        qp = QPainter(self)
        qp.setPen(QColor(0,0,0))
        #i'm redoing rect again... even though i passed it in? back down to paint errors, so leaving this
        rect = QRect(0, 0, 500, 500)

        colsize = rect.width()//5
        rowsize = rect.height()//5

        qp.drawLine(colsize*2, rowsize, colsize * 2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize * 3, rowsize * 4)
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)


        print(pos)
        #pos = PySide2.QtWidgets.QGraphicsSceneMouseEvent.pos()
        """
        col = math.floor((event.position().x() // colsize)) - 1
        row = math.floor((event.position().y() // rowsize)) - 1
        """
        """
        Game.takeTurn(self, col, row)

        #oh!!! this was in the wrong place!!!
        #now, draw the tokens that are on the board
        for r in range(0, 3):
            for c in range(0, 3):
                #use the game object we created, & self.board from Game
                if self.game.board[c][r] == 'X':
                    #what is this drawing letters thing??? (painter, coordinates, scale)???
                    self.drawX(qp, c, r, colsize, rowsize)
                elif self.game.board[c][r] == 'O':
                    self.drawO(qp, c, r, colsize, rowsize)
                    #oh i see!! we're defining the functions!!

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
"""
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
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

    #idk, i stole this mousePressEvent thing from somewhere, and idk how it works
    #but for now i'm hung up on arguments for paintEvent
    def mousePressEvent(self, e):
        #i was just trying to get around paintEvent's weird argument hunger, so i put this down there instead
        #but then it complained about QPaintEvent object has no attribute position!!!
        position = e.position()
        if e: 
            #i'm trying to figure out why paintEvent is hungry for arguments, and idk about these selfs
            self.paintEvent(self, e, position)


    """
    def clickEvent(self):
        #event = self.clicked.connect(mainwindow.mousePressEvent)
        event = PySide6.QtGui.QSinglePointEvent()
        #i'm very likely not dealing with position correctly
        (col, row) = PySide6.QtGui.QSinglePointEvent.globalPosition(col, row)
        #pos = PySide2.QtWidgets.QGraphicsSceneMouseEvent.pos()
        if event:
            self.paintEvent(event)
    """  
    #seriously!!! why is paintEvent ALWAYS an argument short???
    def paintEvent(self, event, position):
        qp = QPainter(self)
        qp.setPen(QColor(0,0,0))

        rect = QRect(0, 0, 500, 500)

        #i was going to try to figure out how to deal with this Qpoint integer that QMouseEvent is giving me
        #but this is behind paintEvent's weird hunger so at this point who knows
        col = position.x()
        row = position.y()

        colsize = rect.width()//5
        rowsize = rect.height()//5

        qp.drawLine(colsize*2, rowsize, colsize * 2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize * 3, rowsize * 4)
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)


        #print(pos)
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

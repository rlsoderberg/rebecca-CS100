#well, ok, i tried to isolate the click interaction
#you know what i got stuck on? self.setlayout!!! come on!!!

#so... it's about how you label the function? like mousePressEvent? that is sooo weird

#i was thinking about mousepressevent for right click... and that reminded me of the runescape examine feature
#well, we've got to do something. runescape tictactoe?
#i can totally cop some early 2005 graphics
#but i don't have very much time tonight!!!
#well, first... let me get my tictactoe file working... 
#that means it's time for my comments to hop over!

import sys
import math
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from tictactoe_game import Game

class MainWindow(QWidget):

    #MainWindow constructor 
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        #set geometry...
        self.resize(500,500)
        self.setWindowTitle("Tic-Tac-Toe")

        #commented out for now since we haven't made it yet
        #self.game = Game()

    #respond to paint event
    def paintEvent(self, event):
        qp = QPainter(self)
        #set pen color
        qp.setPen(QColor(0,0,0))
        #what is event? where is rect coming from?
        size = event.rect().size()

        #calculate width & height of rows & columnds
        colsize = size.width() // 5
        rowsize = size.height() // 5

        #draw vertical lines
        qp.drawLine(colsize*2, rowsize, colsize*2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize*3, rowsize*4)
        #draw horizontal lines
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()






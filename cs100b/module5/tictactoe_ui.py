#now... i'm having trouble with getting colsize. i see i did it a little differently before:
#basically, i went size = QRect(0, 0, 500, 500)
#and i just don't really understand the deal with size & rect anyway
#ok, i tried the example program, and it DOES work. what am i doing???
#I HAD TO PUT PARENTHESES AFTER SIZE
#now, i'm still waiting to see exactly what event is

#so... what about resize? why are we using resize instead of setgeometry
#well, i guess setgeometry messes up the resizable window effect

#i should totally make minesweeper & tetris next

import sys
import math
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

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






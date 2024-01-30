

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






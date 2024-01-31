#oh that's right, i still need to listen to graceland tonight, time for coding
#it might take me a while just to figure out how to do an image border
#well, eventually i want to attach the right border to the right side of the screen so it's resizable
#but i'll skip that for starters
#i stole that alignmentflag thing from the tutorial, and i have no idea if it will work
#it's not working!!! at all!!!
#ohhh, i think i'm forgetting to add them to the layout...
#well gee!!! how do you put them next to each other?
#i'll also have to figure out how to tile them vertically

import sys
import math
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from pathlib import Path

class MainWindow(QWidget):

    #MainWindow constructor 
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        #set geometry...
        self.resize(500,500)
        self.setWindowTitle("Tic-Tac-Toe")

        lBorder = QLabel('Left Border', alignment=Qt.AlignmentFlag.AlignLeft)
        border = QPixmap('border.png')
        lBorder.setPixmap(border)

        rBorder = QLabel('Right Border', alignment=Qt.AlignmentFlag.AlignRight)
        rBorder.setPixmap(border)

        layout = QVBoxLayout()
        layout.addWidget(lBorder)
        layout.addWidget(rBorder)
        self.setLayout(layout)




        #commented out for now since we haven't made it yet
        #self.game = Game()
"""
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
    """

def main():
    app = QApplication([])
    w = MainWindow()
    w.setStyleSheet(Path('style.qss').read_text())
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()






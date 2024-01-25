#so i could mess about with qpainter, right?
#this time i drew, like, a weird table
#sqrt is cool

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
        self.setWindowTitle("qpainter")

    #respond to paint event
    def paintEvent(self, event):
        qp = QPainter(self)

        r = 0
        g = 250
        b = 2

        for x in range(0, 25):
            r = r + 10
            g = g - 10
            h = int(math.sqrt(g*b))
            b = b + 5
            qp.setPen(QColor(r,g,b))
            qp.drawLine(h, r, h, b)
            qp.drawLine(h+1, r, h, b)
            qp.drawLine(h+2, r, h, b)
            qp.drawLine(h+3, r, h, b)
            qp.drawLine(h+5, r, h, b)           
            qp.drawLine(h+8, r, h, b)
            qp.drawLine(h+13, r, h, b)
            qp.drawLine(h+21, r, h, b)
            qp.drawLine(h+34, r, h, b)
            qp.drawLine(h+55, r, h, b)
            qp.drawLine(h+89, r, h, b)
            qp.drawLine(h+144, r, h, b)
            qp.drawLine(h+360, r, h, b)

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()






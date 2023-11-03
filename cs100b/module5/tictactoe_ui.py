import sys
import math
import random
from PyQt6.QtWidgets import *
#so qtgui is for making graphics?
from PyQt6.QtGui import *
#and qtcore is for... animation and stuff?
from PyQt6.QtCore import *

#let's gooo!!! i'm thinking, i totally have to make a gui version of risk later. tic tac toe first tho
class mainwindow(QWidget):
    def __init__(self, parent = None):
        #oh, and i'm totally waiting before making proper comments. at the end of cs100b i'll come back!!!
        super(mainwindow, self).__init__(parent)
        #so this is a new thing!!! i think it's just from qtwidgets, right?
        self.resize(500,500)
        self.setWindowTitle('Tic Tac Toe')

        #waiting to see what this is for???
        #self.game = Game()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QColor(0,0,0))
        size = event.rect().size()

        colsize = size.width() // 5
        rowsize = size.height() // 5

        #i am totally going to have to look at qpainter, and see what is actually happening!!!
        """
        qp.drawLine(colsize*2, rowsize, colsize * 2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize * 3, rowsize * 4)
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)
        """
        #i do not have that much time today so i just drew a face
        img1 = QPixmap("trfarclio.png")

        qp.drawLine(50, 50, 150, 150)
        qp.drawLine(350, 150, 450, 50)

        qp.drawEllipse(100, 300, 300, 100)

        brush = QBrush(Qt.BrushStyle.SolidPattern)
        qp.setBrush(brush)

        qp.drawEllipse(100, 130, 10, 10)
        qp.drawEllipse(400, 130, 10, 10)
        qp.drawPixmap(215, 310, img1)

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    #i don't EXACTLY get the deal with this
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

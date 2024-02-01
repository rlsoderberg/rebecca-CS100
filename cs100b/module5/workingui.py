import math
import sys
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from workinggame import Game

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.resize(500,500)
        self.setWindowTitle("Tic-Tac-Toe")

        self.game = Game()

    #respond to paint events
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QColor(0,0,0))
        size = event.rect().size()

        # draw the board to fit the size
        colsize = size.width() // 5
        rowsize = size.height() // 5

        qp.drawLine(colsize*2, rowsize, colsize*2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize*3, rowsize*4)
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

        # now, draw the tokens that are on the board
        for r in range(0,3):
            for c in range(0,3):
                if self.game.board[c][r] == 'X':
                    self.drawX(qp, c, r, colsize, rowsize)
                elif self.game.board[c][r] == 'O':
                    self.drawO(qp, c, r, colsize, rowsize)

    def drawX(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        colmargin = int(colsize * 0.05)
        rowmargin = int(rowsize * 0.05)
        pen = QPen(QBrush(QColor(255,0,0)), 8)
        qp.setPen(pen)
        qp.drawLine(x+colmargin, y+rowmargin, x+colsize-2*colmargin, y+rowsize-2*rowmargin)
        qp.drawLine(x+colsize-2*colmargin, y+rowmargin, x+colmargin, y+rowsize-2*rowmargin)

    def drawO(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        colmargin = int(colsize * 0.05)
        rowmargin = int(rowsize * 0.05)
        pen = QPen(QBrush(QColor(0,255,0)), 5)
        qp.setPen(pen)
        qp.drawEllipse(x+colmargin, y+rowmargin, colsize-2*colmargin, rowsize-2*rowmargin)

    #respond to mousepress events
    def mousePressEvent(self, event):
        size = self.size()

        colsize = size.width() // 5
        rowsize = size.height() // 5

        col = math.floor((event.position().x() // colsize)) - 1
        row = math.floor((event.position().y() // rowsize)) - 1

        if col >= 0 and col < 3 and row >= 0 and row < 3:
            self.game.takeTurn(col, row)

        # force a repaint
        self.repaint()

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
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
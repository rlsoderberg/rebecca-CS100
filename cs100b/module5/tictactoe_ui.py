#i also still need to deal with right click & examine

#well... i just noticed that resizing messes with my scroll... so i guess THAT'S out for now... 
#oh, i feel so bad. is it because i'm spoiling the resizability? david bowie plz help me
#i stole screen size from banjo
#so THAT didn't work... 
#i totally cheated by finding the exact size of the window
#i'm sorry!!!

#i'd have to sort out the different levels later

#right now i'm trying to get it to paint runes, instead of xs and os
#i'm thinking of using, uh... painter.drawimage, or something
#the thing is, i'm on my phone right now, and i'm probably not getting much of this done tonight
#so i'll try to at least get it to paint runes...
#i thought, what if it drew the xs and the os exactly where you clicked???
#yeah, that would be a whole extra thing to code i guess, but wouldn't that be cool???
#well, maybe i'll at least get it to paint runes at some point

import sys
import math
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from pathlib import Path
from tictactoe_game import Game

class MainWindow(QWidget):

    #MainWindow constructor 
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        #set geometry...
        self.setGeometry(100, 100, 100, 100)
        self.setFixedSize(560, 370)
        self.setWindowTitle("Runescape Tic-Tac-Toe")

        #images for screen layout
        lBorder = QLabel('Left Border', alignment=Qt.AlignmentFlag.AlignLeft)
        border = QPixmap('border.png')
        lBorder.setPixmap(border)

        rBorder = QLabel('Right Border', alignment=Qt.AlignmentFlag.AlignRight)
        rBorder.setPixmap(border)
        
        layout = QHBoxLayout()
        layout.addWidget(lBorder)
        
        layout.addSpacing(400)
        

        layout.addWidget(rBorder)
        self.setLayout(layout)

        #game from tictactoe_game
        self.game = Game()

    #respond to paint event
    def paintEvent(self, event):
        qp = QPainter(self)
        #set pen color
        qp.setPen(QColor(0,0,0))
        pixmap = QPixmap("scroll3.png")
        qp.drawPixmap(self.rect(), pixmap)
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

        #draw tokens
        for c in range(0, 3):
            for r in range(0, 3):
                if self.game.board[c][r] == 'X':
                    self.drawX(qp, c, r, colsize, rowsize)
                elif self.game.board[c][r] == 'O':
                    self.drawO(qp, c, r, colsize, rowsize)
    
    #draw ellipse(x_offset, y_offset, diameter, diameter)
    def drawO(self, qp, c, r, colsize, rowsize):
        runemap = QPixmap("water.png")
        

    def drawX(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        colmargin = int(colsize * 0.05)
        rowmargin = int(rowsize * 0.05)
        pen = QPen(QBrush(QColor(0,0,0)),5)
        qp.setPen(pen)
        qp.drawLine(x+colmargin, y+rowmargin, x+colsize-2*colmargin, y+colsize-2*rowmargin)

    #mousePressEvent generates its own event
    def mousePressEvent(self, event):
        #get size of full board
        size = self.size()

        #calculate row & column size
        colsize = size.width() // 5
        rowsize = size.height() // 5

        #mark which col & row were clicked on
        col = math.floor((event.position().x() // colsize)) - 1
        row = math.floor((event.position().y() // rowsize)) - 1

        self.clickx = event.position().x()
        self.clicky = event.position().y()

        #only clicks within board are processed
        if col >= 0 and col < 3 and row >= 0 and row < 3:
            self.game.takeTurn(col, row)
        
        self.repaint()

        winner = self.game.checkForWinner()
        if winner != ' ':
            dlg = WinnerDialog(winner)
            if dlg.exec():
                self.game.clearBoard()

class WinnerDialog(QDialog):
    def __init__(self, winner):
        super().__init__()
    
        #set title
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
    w.setStyleSheet(Path('style.qss').read_text())
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()






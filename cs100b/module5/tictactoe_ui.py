#so... what's this, like, matrix thing that's being used to keep track of tokens?
#well, i guess i just don't use matrixes very often, but i guess python matrixes do kind of make sense 

#ok, i get where event is coming from, but i still don't get where event.rect().size() is coming from
#i get that the size of a QWidget is the whole window
#and mousePressEvent is a behavior of a QWidget, so i guess that makes sense
#but why rect.size??? can't i just use size???
#see, the previous line says qp.drawPixmap(self.rect(), pixmap), so does that have anything to do with it?

#oh, so winner dialog is another class. i honestly don't really get when to use classes?
#i wonder if that would help me to communicate between files? is that what i'm not getting?
#anyway... so qdialog... kind of like qmessagebox?
#super is different in the winner dialog class... is that what super does? connects all the classes?

#i also still need to deal with right click & examine

#i should have committed it as soon as it started working!!! now it's complaining about [' '],[' '],[' ']

#it was literally a difference between 
"""
self.board = [
                [' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']
            ]
(CORRECT)
and
self.board = [
            [' '],[' '],[' ']
            [' '],[' '],[' ']
            [' '],[' '],[' ']
        ]
(INCORRECT)
how did that even get there??? i swear i didn't touch it!!!
"""
#well, now it's KIND OF working... i'm saving this version before anything else randomly stops working
#i mean, it's almost possible that was an archaic mistake
#and i didn't notice on my first run, because i was so excited that it was working that i closed it right away
#however, didn't the error appeared immediately after initiating program? i guess that's the question



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
        self.setWindowTitle("Tic-Tac-Toe")

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
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        colmargin = int(colsize * 0.05)
        rowmargin = int(rowsize * 0.05)
        pen = QPen(QBrush(QColor(0,0,0)),5)
        qp.setPen(pen)
        qp.drawEllipse(x+colmargin, y+rowmargin, colsize-2*colmargin, rowsize-2*rowmargin)

    def drawX(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        colmargin = int(colsize * 0.05)
        rowmargin = int(rowsize * 0.05)
        pen = QPen(QBrush(QColor(0,0,0)),5)
        qp.setPen(pen)
        qp.drawLine(x+colmargin, y+rowmargin, x+colsize-colmargin, y+colsize-rowmargin)

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






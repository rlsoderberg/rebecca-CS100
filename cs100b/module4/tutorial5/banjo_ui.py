#this is... harder than expected, trying to relocate message box
#i think i'm just going to relocate the whole mainwindow to the center of the screen
#look, i found ways to get the coordinates of mainwindow AND the screen
#but the question is, how do i extract these coordinates so i get usable numbers???
#ah, the key was parentheses after width

#my new sadending wasn't working for some reason, so i replaced it with my old one
#it must be something about critical...
#i should see this as an opportunity to add my own losing graphic

#i want to make unclick clearer by making it unclick when you click a different option...
#i was going to make list prevselect... but you know what??? for now i'm just going to make everything blue!!!
#is it me, or are the buttons a little tiny bit harder to click now?

#i did also go through and put everything in camelcase

#oh, right, we're separating these into multiple files!
#you know, i could totally start doing that here...
#i moved my click handling to game
#and then... probloop had a hard time starting... it didn't seem to be getting probcount...
#i tried creating an instance of probloop...
#oh wait, you have to make a CLASS and create an instance of THAT

#so here's the problem...
#at first, i tried putting the button connects in game, because they connect to stuff in game
#but then i put them back in ui, because i created the buttons in ui
#so what do i do with them???

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from pathlib import Path
from pygame import mixer
import os
import random

from banjo_game import Game

class MainWindow (QWidget):
    #initialize superwindow
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        #qvbox for button
        self.mainLayout = QVBoxLayout()
        #qhbox for images
        self.imgLayout = QHBoxLayout()
        #qhbox for subheadings
        self.subLayout = QHBoxLayout()

        #setting & adding layouts
        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.imgLayout)
        self.mainLayout.addLayout(self.subLayout)

        #set geometry
        screen = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        sWidth = screen.width()
        sHeight = screen.height()
        self.setGeometry(int((sWidth/2)-(500/2)), int((sHeight/2)-(300/2)), 500, 300)
        
        #initialize variables
        self.initVariables()

        #show window
        self.show()

        #create instance of game
        self.game = Game()

        #function for initializing graphics
    def initVariables(self):
        #title widget
        self.title = QLabel(objectName='title')
        self.title.setText('We are on the lookout for')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.title)

        #3 label widgets showing qpixmap images
        self.label1 = QLabel()
        self.img1 = QPixmap('')
        self.label1.setPixmap(self.img1)
        self.imgLayout.addWidget(self.label1)

        self.label2 = QLabel()
        self.img2 = QPixmap('')
        self.label2.setPixmap(self.img2)
        self.imgLayout.addWidget(self.label2)

        self.label3 = QLabel()
        self.img3 = QPixmap('')
        self.label3.setPixmap(self.img3)
        self.imgLayout.addWidget(self.label3)

        #3 button widgets for answer options
        self.button1 = QPushButton('')
        self.button1.clicked.connect(self.click1)
        self.subLayout.addWidget(self.button1)

        self.button2 = QPushButton('')
        self.button2.clicked.connect(self.click2)
        self.subLayout.addWidget(self.button2)

        self.button3 = QPushButton('')
        self.button3.clicked.connect(self.click3)
        self.subLayout.addWidget(self.button3)


        #list of option buttons
        self.buttonList = [self.button1, self.button2, self.button3]

        #button widget for submit button
        self.button = QPushButton('')
        self.button.setIcon(QIcon(''))
        self.button.clicked.connect(self.submit)
        self.mainLayout.addWidget(self.button)

        #variables for unclicking buttons
        self.alreadySelect1 = False
        self.alreadySelect2 = False
        self.alreadySelect3 = False

        #set variables for number of problems & point total
        self.probTotal = 3
        self.points = 0
        #initialize correctlist so you only have to grab it once
        self.correctList = 0


#main function to execute app & play music
def main():
    mixer.init()
    mixer.music.load("src/banjo.wav")
    mixer.music.play()
    app = QApplication([])
    app.setStyleSheet(Path('src/style.qss').read_text())
    w = MainWindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()
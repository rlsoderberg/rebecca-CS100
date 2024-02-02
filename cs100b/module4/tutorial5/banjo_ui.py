#aha!!! you have to use classes!!!
#well, this will be a whole thing to work on... i'll do it tomorrow...

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from pathlib import Path
from pygame import mixer
import os
import random

from banjo_inter import Inter

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

        #set geometry
        screen = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        sWidth = screen.width()
        sHeight = screen.height()
        self.setGeometry(int((sWidth/2)-(500/2)), int((sHeight/2)-(300/2)), 500, 300)
        

        #show window
        self.show()

        self.inter = Inter()

        self.probCount = 0

        #get & set variables
        self.getVariables()
        self.initLayout()

    #function to import problem data from file
    def getVariables(self):

        questionList = open("src/questiontxt.txt", "r")
        data = questionList.read()
        self.questionList = data.replace('\n', ' ').split(".")
        questionList.close()
        self.thisQuestion = self.questionList[self.probCount]

        self.thisTitle = str(self.probCount + 1) + '. ' + str(self.thisQuestion)

        self.imgTxt = open(f"src/{self.probCount+1}/imgtxt{self.probCount+1}.txt", "r")
        data = self.imgTxt.read()
        self.imgList = data.replace('\n', ' ').split("/")
        self.imgTxt.close()

        self.correctTxt = open("src/correcttxt.txt", "r")
        data = self.correctTxt.read()
        self.correctList = data.replace('\n', ' ').split(".")
        self.correct = self.correctList[self.probCount]
        self.correctTxt.close()

        self.optionTxt = open(f"src/{self.probCount+1}/optiontxt{self.probCount+1}.txt", "r")
        data = self.optionTxt.read()
        self.optionList = data.replace('\n', ' ').split(".")
        self.optionTxt.close()
        

        self.thisSubmit = 'Submit'

    def initLayout(self):
        #setting & adding layouts
        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.imgLayout)
        self.mainLayout.addLayout(self.subLayout)

        #title widget
        self.title = QLabel(objectName='title')
        self.title.setText(self.thisQuestion)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.title)

        #3 label widgets showing qpixmap images
        self.label1 = QLabel()
        self.img1 = QPixmap(f'src/img/{self.imgList[0]}')
        self.label1.setPixmap(self.img1)
        self.imgLayout.addWidget(self.label1)

        self.label2 = QLabel()
        self.img2 = QPixmap(f'src/img/{self.imgList[1]}')
        self.label2.setPixmap(self.img2)
        self.imgLayout.addWidget(self.label2)

        self.label3 = QLabel()
        self.img3 = QPixmap(f'src/img/{self.imgList[2]}')
        self.label3.setPixmap(self.img3)
        self.imgLayout.addWidget(self.label3)

        #3 button widgets for answer options
        self.button1 = QPushButton('')
        self.button1.setText(self.optionList[0])
        self.button1.clicked.connect(Inter.click1)
        self.subLayout.addWidget(self.button1)

        self.button2 = QPushButton('')
        self.button2.setText(self.optionList[1])
        self.button2.clicked.connect(Inter.click2)
        self.subLayout.addWidget(self.button2)

        self.button3 = QPushButton('')
        self.button3.setText(self.optionList[2])
        self.button3.clicked.connect(Inter.click3)
        self.subLayout.addWidget(self.button3)


        #list of option buttons
        self.buttonList = [self.button1, self.button2, self.button3]

        #button widget for submit button
        self.button = QPushButton('')
        self.button.setIcon(QIcon(f'src/img/submit.png'))
        self.button.setText('Submit')
        self.button.clicked.connect(Inter.submit)
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
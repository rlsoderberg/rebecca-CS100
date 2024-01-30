

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from pathlib import Path
from pygame import mixer
import os
import random

class MainWindow (QWidget):
    #initialize superwindow
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        window = self.frameGeometry()
        wWidth = window.width()
        wHeight = window.height()
        screen = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        sWidth = screen.width()
        sHeight = screen.height()
        self.setGeometry(int((sWidth/2)-(500/2)), int((sHeight/2)-(300/2)), 500, 300)

        #initialize variables
        self.initVariables()
        
        #show window, and then first info box
        self.show()
        self.info()

        #start list of problems
        self.probLoop(self.probCount)

    #function for initializing graphics & variables
    def initVariables(self):
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
        self.probCount = 0
        #initialize correctlist so you only have to grab it once
        self.correctList = 0



    #probloop sets display for each problem, based on problem data
    def probLoop(self, probCount):

        self.prevSelect = []
        
        for o in self.buttonList:
            o.setStyleSheet("background-color: blue")

        self.getVariables(probCount)
        self.setVariables()

    #functions to show button which button is selected, and communicate selection data
    def click1(self):
        self.button1.setStyleSheet('QPushButton {background-color: red}')
        self.select = 1

        if self.alreadySelect1 == True:
            self.button1.setStyleSheet('QPushButton {background-color: blue}')
            self.alreadySelect1 = False
        else:
            self.alreadySelect1 = True

        self.button2.setStyleSheet('QPushButton {background-color: blue}')
        self.button3.setStyleSheet('QPushButton {background-color: blue}')

    def click2(self):
        self.button2.setStyleSheet('QPushButton {background-color: red}')
        self.select = 2

        if self.alreadySelect2 == True:
            self.button2.setStyleSheet('QPushButton {background-color: blue}')
            self.alreadySelect2 = False
        else:
            self.alreadySelect2 = True

        self.button1.setStyleSheet('QPushButton {background-color: blue}')
        self.button3.setStyleSheet('QPushButton {background-color: blue}')

    def click3(self):
        self.button3.setStyleSheet('QPushButton {background-color: red}')
        self.select = 3 

        if self.alreadySelect3 == True:
            self.button3.setStyleSheet('QPushButton {background-color: blue}')
            self.alreadySelect3 = False
        else:
            self.alreadySelect3 = True

        self.button1.setStyleSheet('QPushButton {background-color: blue}')
        self.button2.setStyleSheet('QPushButton {background-color: blue}')

    #function to handle either correct or incorrect selection, upon submit
    def submit(self):
        if int(self.select) == int(self.correct):
            self.corrects()
        elif self.select != self.correct:
            self.incorrects()

        self.probCount += 1

        if self.probCount < self.probTotal:
            self.probLoop(self.probCount)
        elif self.probCount == self.probTotal:
            if self.points == self.probTotal:
                self.happyEnding()
            else:
                self.sadEnding()

    #function to import problem data from file
    def getVariables(self, probCount):

        questionList = open("src/questiontxt.txt", "r")
        data = questionList.read()
        self.questionList = data.replace('\n', ' ').split(".")
        questionList.close()
        self.thisQuestion = self.questionList[probCount]

        self.thisTitle = str(probCount + 1) + '. ' + str(self.thisQuestion)

        self.imgTxt = open(f"src/{probCount+1}/imgtxt{probCount+1}.txt", "r")
        data = self.imgTxt.read()
        self.imgList = data.replace('\n', ' ').split("/")
        self.imgTxt.close()

        self.correctTxt = open("src/correcttxt.txt", "r")
        data = self.correctTxt.read()
        if self.correctList == 0:
            self.correctList = data.replace('\n', ' ').split(".")
        self.correct = self.correctList[probCount]
        self.correctTxt.close()

        self.optionTxt = open(f"src/{probCount+1}/optiontxt{probCount+1}.txt", "r")
        data = self.optionTxt.read()
        self.optionList = data.replace('\n', ' ').split(".")
        self.optionTxt.close()
        

        self.thisSubmit = 'Submit'
    
    #function to set problem data to display widgets
    def setVariables(self):

        self.title.setText(self.thisTitle)

        self.img1 = QPixmap(f'src/img/{self.imgList[0]}')
        self.label1.setPixmap(self.img1)
        self.img2 = QPixmap(f'src/img/{self.imgList[1]}')
        self.label2.setPixmap(self.img2)
        self.img3 = QPixmap(f'src/img/{self.imgList[2]}')
        self.label3.setPixmap(self.img3)

        self.button1.setText(self.optionList[0])
        self.button2.setText(self.optionList[1])
        self.button3.setText(self.optionList[2])

        self.button.setText(self.thisSubmit)

    #first info box function
    def info(self):
        infoBox = QMessageBox()
        infoBox.setWindowTitle('Banjo Tyrwo')
        infoBox.setText('Answer all questions\nto gain super combo')
        infoBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        inf = infoBox.exec()

    #correct/incorrect functions
    def corrects(self):
        correctBox = QMessageBox()
        correctBox.setWindowTitle('Correct')
        correctBox.setText("You are correct.")
        correctBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        cor = correctBox.exec()

        self.points += 1

    def incorrects(self):
        incorrectBox = QMessageBox()
        incorrectBox.setWindowTitle('Incorrect')
        incorrectBox.setText('You are incorrect.')
        incorrectBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        inc = incorrectBox.exec()

    #happy/sad endings
    def sadEnding(self):
        sadEnding = QMessageBox()
        sadEnding.setWindowTitle('Game Over')
        sadEnding.setText('So sorry, you have not achieved super bonus.')
        sadEnding.setStandardButtons(QMessageBox.StandardButton.Ok)
        icon = QPixmap('src/img/sadlogo.png')
        sadEnding.setIconPixmap(icon)
        sad = sadEnding.exec()

        QApplication.quit()

    def happyEnding(self):
        happyEnding = QMessageBox()
        happyEnding.setWindowTitle('Game Over')
        happyEnding.setText('Congratulations! you have achieved super bonus!')
        happyEnding.setStandardButtons(QMessageBox.StandardButton.Ok)
        icon = QPixmap('src/img/happylogo.png')
        happyEnding.setIconPixmap(icon)
        hap = happyEnding.exec()

        QApplication.quit()

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
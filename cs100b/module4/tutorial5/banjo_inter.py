#oh, but now, how do i deal with changing button style upon interaction?
#is that beyond the scope of pyqt, dynamic state changes? it couldn't be!!!
#apparently there's a property system... maybe i'll try that sometime...

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Inter():
    def __init__(self):
        super().__init__()

        #show first info box
        self.info()

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
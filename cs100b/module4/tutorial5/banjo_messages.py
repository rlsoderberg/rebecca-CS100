from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Messages():
    def __init__(self):
        super().__init__()

        #show first info box
        self.info()

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
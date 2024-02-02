#well, i'm remaking the images every round, because it can't seem to find label1
#AND the buttons. like, what's the deal? how do i modify existing buttons?
#well, now the buttons are empty! what else am i supposed to do???

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from banjo_messages import Messages

class Game:
    def __init__(self):
        super().__init__()

        self.probCount = 0

        self.messages = Messages()

        #get & set variables
        self.getVariables()
        self.setVariables()

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

    #function to set problem data to display widgets
    def setVariables(self):
        self.label1 = QLabel()
        self.img1 = QPixmap(f'src/img/{self.imgList[0]}')
        self.label1.setPixmap(self.img1)

        self.label2 = QLabel()
        self.img2 = QPixmap(f'src/img/{self.imgList[1]}')
        self.label2.setPixmap(self.img2)

        self.label3 = QLabel()
        self.img3 = QPixmap(f'src/img/{self.imgList[2]}')
        self.label3.setPixmap(self.img3)

        self.button1 = QPushButton()
        self.button1.setText(self.optionList[0])

        self.button2 = QPushButton()
        self.button2.setText(self.optionList[1])

        self.button3 = QPushButton()
        self.button3.setText(self.optionList[2])

        self.button = QPushButton()
        self.button.setText(self.thisSubmit)

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
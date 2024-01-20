#i restructured my files so i didn't need duplicate images

#i am still modifying color inefficiently
#i guess what i should do is go through the buttons at first and add them to a button list
#but i actually don't have time for that right now!

#i used a workaround for setting the text in the ending message box
#and i wish i knew how to set text properly, from outside!
#but that was annoyingly not included in the pyqt6 tutorial!

#i'm also not sure how to set the logo for a qmessagebox
#see, whenever i try to modify my qmessageboxes, i get this same error
#AttributeError: 'StandardButton' object has no attribute 'setText'
#which kind of leads me to believe i'm doing the whole thing wrong?
#if it thinks my messagebox is a button???


from PyQt6.QtWidgets import *
from pathlib import Path
from pygame import mixer
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import os
import random

class mainwindow (QWidget):
    #initialize superwindow
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)

        #set geometry and layouts
        self.setGeometry(100,100,350,300)

        #qvbox for button
        self.mainlayout = QVBoxLayout()
        #qhbox for images
        self.imglayout = QHBoxLayout()
        #qhbox for subheadings
        self.sublayout = QHBoxLayout()

        #setting & adding layouts
        self.setLayout(self.mainlayout)
        self.mainlayout.addLayout(self.imglayout)
        self.mainlayout.addLayout(self.sublayout)

        #title widget
        self.title = QLabel(objectName='title')
        self.title.setText('We are on the lookout for')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainlayout.addWidget(self.title)

        #3 label widgets showing qpixmap images
        self.label1 = QLabel()
        self.img1 = QPixmap('')
        self.label1.setPixmap(self.img1)
        self.imglayout.addWidget(self.label1)

        self.label2 = QLabel()
        self.img2 = QPixmap('')
        self.label2.setPixmap(self.img2)
        self.imglayout.addWidget(self.label2)

        self.label3 = QLabel()
        self.img3 = QPixmap('')
        self.label3.setPixmap(self.img3)
        self.imglayout.addWidget(self.label3)

        #3 button widgets for answer options
        self.button1 = QPushButton('')
        self.button1.clicked.connect(self.click1)
        self.sublayout.addWidget(self.button1)

        self.button2 = QPushButton('')
        self.button2.clicked.connect(self.click2)
        self.sublayout.addWidget(self.button2)

        self.button3 = QPushButton('')
        self.button3.clicked.connect(self.click3)
        self.sublayout.addWidget(self.button3)

        #button widget for submit button
        self.button = QPushButton('')
        self.button.setIcon(QIcon(''))
        self.button.clicked.connect(self.submit)
        self.mainlayout.addWidget(self.button)

        #set variables for number of problems & point total
        self.probtotal = 3
        self.points = 0
        self.probcount = 0
        #initialize correctlist so you only have to grab it once
        self.correctlist = 0

        #show window, and then first info box
        self.show()
        self.info()

        #list of problems
        self.probloop(self.probcount)

    #probloop sets display for each problem, based on problem data
    def probloop(self, probcount):

        self.button1.setStyleSheet("background-color: blue")
        self.button2.setStyleSheet("background-color: blue")
        self.button3.setStyleSheet("background-color: blue")

        self.alreadyselect1 = False
        self.alreadyselect2 = False
        self.alreadyselect3 = False

        self.get_variables(probcount)
        self.set_variables()

    #functions to show button which button is selected, and communicate selection data
    def click1(self):
        self.button1.setStyleSheet('QPushButton {background-color: red}')
        self.select = 1

        if self.alreadyselect1 == True:
            self.button1.setStyleSheet('QPushButton {background-color: blue}')
            self.alreadyselect1 = False
        else:
            self.alreadyselect1 = True

    def click2(self):
        self.button2.setStyleSheet('QPushButton {background-color: red}')
        self.select = 2

        if self.alreadyselect2 == True:
            self.button2.setStyleSheet('QPushButton {background-color: blue}')
            self.alreadyselect2 = False
        else:
            self.alreadyselect2 = True

    def click3(self):
        self.button3.setStyleSheet('QPushButton {background-color: red}')
        self.select = 3 

        if self.alreadyselect3 == True:
            self.button3.setStyleSheet('QPushButton {background-color: blue}')
            self.alreadyselect3 = False
        else:
            self.alreadyselect3 = True

    #function to handle either correct or incorrect selection, upon submit
    def submit(self):
        if int(self.select) == int(self.correct):
            self.corrects()
        elif self.select != self.correct:
            self.incorrects()

        self.probcount += 1

        if self.probcount < self.probtotal:
            self.probloop(self.probcount)
        elif self.probcount == self.probtotal:
            if self.points == self.probtotal:
                self.happyending()
            else:
                self.sadending()

    #first info box function
    def info(self):
        info = QMessageBox.information(
            self,
            'Banjo Tyrwo',
            'Answer all questions\nto gain super combo'
        )

    #correct/incorrect functions
    def corrects(self):
        corrects = QMessageBox.information(
            self,
            'Correct',
            'You are correct.'
        )
        self.points += 1

    def incorrects(self):
        incorrects = QMessageBox.information(
            self,
            'Incorrect',
            'You are incorrect.'
        )

    #function to import problem data from file
    def get_variables(self, probcount):

        questionlist = open("src/questiontxt.txt", "r")
        data = questionlist.read()
        self.questionlist = data.replace('\n', ' ').split(".")
        questionlist.close()
        self.thisquestion = self.questionlist[probcount]

        self.thisTitle = str(probcount + 1) + '. ' + str(self.thisquestion)

        self.imgtxt = open(f"src/{probcount+1}/imgtxt{probcount+1}.txt", "r")
        data = self.imgtxt.read()
        self.imglist = data.replace('\n', ' ').split("/")
        print(self.imglist)
        self.imgtxt.close()

        self.correcttxt = open("src/correcttxt.txt", "r")
        data = self.correcttxt.read()
        if self.correctlist == 0:
            self.correctlist = data.replace('\n', ' ').split(".")
        self.correct = self.correctlist[probcount]
        self.correcttxt.close()

        self.optiontxt = open(f"src/{probcount+1}/optiontxt{probcount+1}.txt", "r")
        data = self.optiontxt.read()
        self.optionlist = data.replace('\n', ' ').split(".")
        self.optiontxt.close()
        

        self.thisSubmit = 'Submit'
    
    #function to set problem data to display widgets
    def set_variables(self):

        self.title.setText(self.thisTitle)

        self.img1 = QPixmap(f'src/img/{self.imglist[0]}')
        self.label1.setPixmap(self.img1)
        self.img2 = QPixmap(f'src/img/{self.imglist[1]}')
        self.label2.setPixmap(self.img2)
        self.img3 = QPixmap(f'src/img/{self.imglist[2]}')
        self.label3.setPixmap(self.img3)

        self.button1.setText(self.optionlist[0])
        self.button2.setText(self.optionlist[1])
        self.button3.setText(self.optionlist[2])

        self.button.setText(self.thisSubmit)

    def sadending(self):
        ending = QMessageBox.critical(
            self,
            'Game Over',
            'So sorry, you have not achieved super bonus.'
        )
        QApplication.quit()

    def happyending(self):
        ending = QMessageBox.question(
            self,
            'Game Over',
            'Congratulations! you have achieved super bonus!',
        )
        #ending.setIconPixmap('src/logo.png')
        QApplication.quit()

#main function to execute app & play music
def main():
    mixer.init()
    mixer.music.load("src/banjo.wav")
    mixer.music.play()
    app = QApplication([])
    app.setStyleSheet(Path('src/style.qss').read_text())
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()
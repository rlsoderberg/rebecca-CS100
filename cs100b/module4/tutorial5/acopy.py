#my images still aren't working
#the one that IS working has the same filename as an image used previously
#that KIND of seems like it's about memory or something, but idk how that would be an issue?
#i am also totally failing to set the text in the ending message box
#and i have to fix the button color
#and go through and debug


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
        self.button3.setGeometry(100,100,100,100)
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

        #show window, and then first info box
        self.show()
        self.info()

        #list of problems
        self.probloop(self.probcount)

    #probloop sets display for each problem, based on problem data
    def probloop(self, probcount):

        self.get_variables(probcount)
        self.set_variables()

    #functions to show button which button is selected, and communicate selection data
    def click1(self):
        self.button1.setStyleSheet('QPushButton {background-color: red}')
        self.select = 1
    def click2(self):
        self.button2.setStyleSheet('QPushButton {background-color: red}')
        self.select = 2
    def click3(self):
        self.button3.setStyleSheet('QPushButton {background-color: red}')
        self.select = 3 

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
            self.ending()

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

        questionlist = open("img/questionlist.txt", "r")
        data = questionlist.read()
        self.questionlist = data.replace('\n', ' ').split(".")
        questionlist.close()
        self.thisquestion = self.questionlist[probcount]

        self.thisTitle = str(probcount + 1) + '. ' + str(self.thisquestion)

        dir = (f"./img/{probcount + 1}")
        self.dirlist = os.listdir(path=dir)
        self.imagelist = []
        for file in self.dirlist:
            if file.endswith('.png'):
                self.imagelist.append(file)

        self.correcttxt = open("img/correctlist.txt", "r")
        data = self.correcttxt.read()
        self.correctlist = data.replace('\n', ' ').split(".")
        self.correct = self.correctlist[probcount]
        self.correcttxt.close()

        for file in self.dirlist:
            if file.endswith('.txt'):
                self.optionlist = file
        self.optiontxt = open(f'img/{probcount + 1}/{str(self.optionlist)}', "r")
        data = self.optiontxt.read()
        self.optionchoices = data.replace('\n', ' ').split(".")
        self.optiontxt.close()

        self.thisSubmit = 'Submit'
    
    #function to set problem data to display widgets
    def set_variables(self):

        self.title.setText(self.thisTitle)

        self.img1 = QPixmap(self.imagelist[0])
        self.label1.setPixmap(self.img1)
        self.img2 = QPixmap(self.imagelist[1])
        self.label2.setPixmap(self.img2)
        self.img3 = QPixmap(self.imagelist[2])
        self.label3.setPixmap(self.img3)

        self.button1.setText(self.optionchoices[0])
        self.button2.setText(self.optionchoices[1])
        self.button3.setText(self.optionchoices[2])

        self.button.setText(self.thisSubmit)

    def ending(self):
        ending = QMessageBox.critical(
            self,
            'Game Over',
            'Game Over'
        )
        if self.points == self.probtotal:
            ending.setText()('congratulations! you have achieved super bonus!')
        else:
            ending.setText()('so sorry, you have not achieved super bonus.')
        QApplication.quit()

#main function to execute app & play music
def main():
    mixer.init()
    mixer.music.load("img/banjo.wav")
    mixer.music.play()
    app = QApplication([])
    app.setStyleSheet(Path('img/style.qss').read_text())
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()
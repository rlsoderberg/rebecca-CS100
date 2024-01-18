#OK!!! i got a semi working copy, the one where i was going to whack it over the head tomorrow
#i just deleted all the comments, so i'm going to recomment everything
#and then the main thing left to fix should be mainwindow, and triggers for new questions
#i just discovered this online, and it looks promising, although i haven't tested it yet
"""
        if corrects.close:
            print('CLOSED CORRECTS')
"""
#is that all i have to do??? to get a signal from the x button???
#so here, i'll save a blank copy first

from PyQt6.QtWidgets import *
from pathlib import Path
from pygame import mixer
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import os
import pathlib
class mainwindow (QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,350,300)
        self.mainlayout = QVBoxLayout()
        self.imglayout = QHBoxLayout()
        self.sublayout = QHBoxLayout()
        self.setLayout(self.mainlayout)
        self.probtotal = 2
        self.points = 0
        self.show()
        self.info()
        for self.probcount in range(0, self.probtotal):
            self.probloop(self.probcount)

    def probloop(self, probcount):
        self.get_variables(probcount)
        title = QLabel(objectName='title')
        title.setText(str(probcount) + '. ' + self.thisquestion)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainlayout.addWidget(title)
        self.mainlayout.addLayout(self.imglayout)
        label1 = QLabel()
        img1 = QPixmap(self.imagelist[0])
        label1.setPixmap(img1)
        self.imglayout.addWidget(label1)
        label2 = QLabel()
        img2 = QPixmap(self.imagelist[1])
        label2.setPixmap(img2)
        self.imglayout.addWidget(label2)
        label3 = QLabel()
        img3 = QPixmap(self.imagelist[2])
        label3.setPixmap(img3)
        self.imglayout.addWidget(label3)
        self.mainlayout.addLayout(self.sublayout)
        
        self.select = 0
        self.correcttext = 'That is correct! \nPoints: ' + str(self.points) + '/' + str(self.probtotal)
        self.incorrecttext = 'That is incorrect! \nPoints: ' + str(self.points) + '/' + str(self.probtotal)
        print(f'self.optionlist = {self.optionlist}') 
        print(f'self.optionchoices = {self.optionchoices}')
        self.button1 = QPushButton(self.optionchoices[0])
        self.button1.clicked.connect(self.click1)
        self.sublayout.addWidget(self.button1)
        self.button2 = QPushButton(self.optionchoices[1])
        self.button2.clicked.connect(self.click2)
        self.sublayout.addWidget(self.button2)
        self.button3 = QPushButton(self.optionchoices[2])
        self.button3.setGeometry(100,100,100,100)
        self.button3.clicked.connect(self.click3)
        self.sublayout.addWidget(self.button3)
        self.button = QPushButton("Submit")
        self.button.setIcon(QIcon('img/submit.png'))
        self.button.clicked.connect(self.submit)
        self.mainlayout.addWidget(self.button)
    def click1(self):
        self.button1.setStyleSheet('QPushButton {background-color: red}')
        self.button2.setStyleSheet('QPushButton {background-color: blue}')
        self.button3.setStyleSheet('QPushButton {background-color: blue}')
        self.select = 1
    def click2(self):
        self.button2.setStyleSheet('QPushButton {background-color: red}')
        self.button1.setStyleSheet('QPushButton {background-color: blue}')
        self.button3.setStyleSheet('QPushButton {background-color: blue}')
        self.select = 2
    def click3(self):
        self.button3.setStyleSheet('QPushButton {background-color: red}')
        self.button1.setStyleSheet('QPushButton {background-color: blue}')
        self.button2.setStyleSheet('QPushButton {background-color: blue}')
        self.select = 3 
    def submit(self):
        print(f'self.select = {self.select}')
        print(f'self.correct = {self.correct}')
        if int(self.select) == int(self.correct):
            print('you are correct')
            self.corrects()
        elif self.select != self.correct:
            print('you are incorrect')
            self.incorrects()
    
    
    def info(self):
        QMessageBox.information(
            self,
            'Banjo Tyrwo',
            'Answer all questions\nto gain super combo'
        )
    def corrects(self):
        QMessageBox.information(
            self,
            'Banjo Tyrwo',
            str(self.correcttxt)
        )
        self.probcount += 1
        self.points += 1
    def incorrects(self):
        QMessageBox.information(
            self,
            'Banjo Tyrwo',
            str(self.incorrecttxt)
        )
    def get_variables(self, probcount):
        questionlist = open("img/questionlist.txt", "r")
        data = questionlist.read()
        self.questionlist = data.replace('\n', ' ').split(".")
        questionlist.close()
        self.thisquestion = self.questionlist[probcount - 1]
        self.thisquestion = self.questionlist[probcount]
        dir = (f"./img/{probcount + 1}")
        self.dirlist = os.listdir(path=dir)
        self.imagelist = []
        for file in self.dirlist:
            if file.endswith('.png'):
                self.imagelist.append(file)
        print(f'imagelist: {self.imagelist}')
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
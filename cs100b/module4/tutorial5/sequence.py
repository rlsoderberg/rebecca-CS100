#after sleeping on this, i thought... we really don't need a signal on close message box
#first i thought, can't we do a signal on open message box? but that seems awkward
#more importantly, i realized that the message box has buttons! surely those can emit a signal
#so... with that, i think i'd also have to abandon the for loop
#instead count with while < and incremented counter

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from pathlib import Path



class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('QMessageBox')
        self.setGeometry(100, 100, 300, 100)

        #qvbox for button
        self.mainlayout = QVBoxLayout()
        #qhboxlayout for images 
        self.imglayout = QHBoxLayout()
        #qhboxlayout for subheadings 
        self.sublayout = QHBoxLayout()

        #ok, i'm going to try setting the layout first up here!
        #so i'm copying this ALL up here... more duplicates... i'm pretty sure none of this is ideal!
        #well... i'm going to make sure i'm labeling everything with self...
        self.setLayout(self.mainlayout)

        self.mainlayout.addLayout(self.imglayout)
        self.mainlayout.addLayout(self.sublayout)


        self.title = QLabel(objectName='title')
        self.title.setText('')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainlayout.addWidget(self.title)

        self.label1 = QLabel()
        self.img1 = QPixmap('amgicians.png')
        self.label1.setPixmap(self.img1)
        self.imglayout.addWidget(self.label1)

        self.label2 = QLabel()
        self.img2 = QPixmap('avllegirs.png')
        self.label2.setPixmap(self.img2)
        self.imglayout.addWidget(self.label2)

        self.label3 = QLabel()
        self.img3 = QPixmap('demons.png')
        self.label3.setPixmap(self.img3)
        self.imglayout.addWidget(self.label3)

        self.button1 = QPushButton('Magicians')
        self.button1.clicked.connect(self.click1)
        self.sublayout.addWidget(self.button1)

        self.button2 = QPushButton('Villagers')
        self.button2.clicked.connect(self.click2)
        self.sublayout.addWidget(self.button2)

        self.button3 = QPushButton('Demons')
        self.button3.setGeometry(100,100,100,100)
        self.button3.clicked.connect(self.click3)
        self.sublayout.addWidget(self.button3)

        self.button = QPushButton('Submit')
        self.button.setIcon(QIcon(''))
        self.button.clicked.connect(self.submit)
        self.mainlayout.addWidget(self.button)

        self.probtotal = 3
        self.points = 0
        self.probcount = 0

        #so... the important thing is the info message box & the submit message box

        self.show()
        #and i'm still going to sneakily put this here!!! yeah!!!
        self.info()
    
    def printing(self, probcount):

        self.select = 0
        self.interaction_marker = False

        self.get_variables(probcount)
    
        #so, REALLY... all i should have to do is setText, right?
        self.title.setText(str(self.probcount) + '. ' + self.thisquestion)

        self.img1 = QPixmap(self.imagelist[0])
        self.label1.setPixmap(self.img1)

        self.img2 = QPixmap(self.imagelist[1])
        self.label2.setPixmap(self.img2)

        self.img3 = QPixmap(self.imagelist[2])
        self.label3.setPixmap(self.img3)

        self.button1.setText(self.optionchoices[0])

        self.button2.setText(self.optionchoices[1])

        self.button3.setText(self.optionchoices[2])

        self.button.setText('Submit')


    #ok fine, i'm just going to put in a timer. but... there MUST be an easier way to do this...
    #now i'm using this one from stack overflow. the good thing, is i know how to abort it.
    #basically, threading is a mess, and i'd better find another way...
    #how about this one? it seems pretty simple

        
        
        

        



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
        #to keep everything from being incorrect all the time, we must put this in a separate function...
        #we also need to make sure they are the same variable type
        if int(self.select) == int(self.correct):
            self.corrects()
        elif self.select != self.correct:
            self.incorrects()
        self.interaction_marker = True
        #i'm just taking out cancel right now, since it seems to be causing problems. let them wait
        #self.thread1.cancel()
    def info(self):
        QMessageBox.information(
            self,
            'Banjo Tyrwo',
            'Answer all questions\nto gain super combo.\nYou have one minute\nto answer each question.'
        )
        #self.interaction_marker = True
        #self.thread1.cancel()
    def corrects(self):
        QMessageBox.information(
            self,
            'Correct',
            'You are correct.'
        )
        self.probcount += 1
        self.points += 1
    def incorrects(self):
        QMessageBox.information(
            self,
            'Incorrect',
            'You are incorrect.'
        )

    def get_variables(self, probcount):
        #i am putting this in its own function because it is a lot

        #import all the data - first, questions
        questionlist = open("img/questionlist.txt", "r")

        data = questionlist.read()
        self.questionlist = data.replace('\n', ' ').split(".")
        questionlist.close()

        self.thisquestion = self.questionlist[probcount - 1]

        #images. now, HOW am i going to reference images within a specific subfolder?
        #i can do images up here, because i've got self.filenames!
        dir = (f"./img/{probcount}")
        self.dirlist = os.listdir(path=dir)
        #making an imagelist... from the dirlist...
        self.imagelist = []
        for file in self.dirlist:
            if file.endswith('.png'):
                self.imagelist.append(file)
        print(f'imagelist: {self.imagelist}')

        #correct answer
        self.correcttxt = open("img/correctlist.txt", "r")

        data = self.correcttxt.read()
        self.correctlist = data.replace('\n', ' ').split(".")
        self.correct = self.correctlist[probcount - 1]
        self.correcttxt.close()

        #answer options
        #using dirlist again
        for file in self.dirlist:
            if file.endswith('.txt'):
                self.optionlist = file
        
        #uh, i wasn't expecting this complicated address to work, but it might have? idk?
        self.optiontxt = open(f'img/{probcount}/{str(self.optionlist)}', "r")

        data = self.optiontxt.read()
        self.optionchoices = data.replace('\n', ' ').split(".")
        self.optiontxt.close()
    


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(Path('img/style.qss').read_text())
    w = MainWindow()
    sys.exit(app.exec())
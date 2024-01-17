from PyQt6.QtWidgets import *
from pathlib import Path
from pygame import mixer
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import os
import pathlib
import threading
import time
from threading import Timer

#Banjo Tyrwo: Bango Gyro/The Dark Tower crossover
class mainwindow (QWidget):
    def __init__(self, parent = None):
        #super init
        super(mainwindow, self).__init__(parent)

        self.setGeometry(100,100,350,300)

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

        #label/QPixMap widget
        self.label1 = QLabel()
        #at first i was trying to use (f"img/{imagelist[1]}") for my pixmap...
        #i had to get around it by posting duplicate images in the main folder!!!

        #oh right, that means when i rename the images, i have to rename them twice!!!
        self.img1 = QPixmap('')
        self.label1.setPixmap(self.img1)
        self.imglayout.addWidget(self.label1)

        #label/QPixMap widget
        self.label2 = QLabel()
        self.img2 = QPixmap('')
        self.label2.setPixmap(self.img2)
        self.imglayout.addWidget(self.label2)

        #label/QPixMap widget
        self.label3 = QLabel()
        self.img3 = QPixmap('')
        self.label3.setPixmap(self.img3)
        self.imglayout.addWidget(self.label3)

        #i'm going to try to verify interaction starting up here...
        #i mean, i don't know if i need this one, because i did put it in print
        #self.interaction_marker = False

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

        self.button = QPushButton('')
        self.button.setIcon(QIcon(''))
        self.button.clicked.connect(self.submit)
        self.mainlayout.addWidget(self.button)

        self.probtotal = 3
        self.points = 0
        self.probcount = 0
        self.interaction_marker = False
        timer_runs = 60

        self.show()
        #wait, can i literally just say the name of the probloop after info???
        self.info()
        #putting probloop in actual loop
        #this loop still isn't working, i don't think!!! so i'm kind of cheating on it for now...

        #so, um, probloop isn't where i need my interaction marker at all, is it???
        #shouldn't i put it up with the buttons?

        #um, this doesn't seem exactly right either, but at least it's starting on the first problem...
        #i'll probably have to sleep on this, AGAIN!!!


       
        for self.probcount in range(1, self.probtotal):
            print(f'probcount right before for loop body: {self.probcount}')
            print(f'interaction_marker right before for loop body: {self.interaction_marker}')

            #new timer? very simple?
            T = self.threading.Timer (60, function, args = None, kwargs = None)
            T.start()

            #i thought i was being smooth, info generating interaction marker, and that being the only criterion
            #well, now my program is being weird, so... back to the awkward double while criteria
            while self.probcount == 1 or self.interaction_marker == True:
                self.printing(self.probcount)
                #it's looping (or failing to loop) before i hit submit... how do i force it to wait for submit???
                #do i have to set a timer or something??? that seems... like... 
        

    #alright, well... data??? uhhhh, i'm sure we've covered how to import from text files... so i need:
    #A) a txt of questions
    #B) a txt of image filenames
    #C) images
    #D) a txt of correct numbers
    #E) a txt of answer options
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

#oh!!! it wasn't displaying, and you know what i did? i forgot this part!!!
def main():
    mixer.init()
    mixer.music.load("img/banjo.wav")
    mixer.music.play()

    app = QApplication([])
    app.setStyleSheet(Path('img/style.qss').read_text())
    w = mainwindow()
    w.show()
    #at one point, sys.exit(app.exec()) seemed necessary for the combo box to work, but idk
    app.exec()

if __name__ == '__main__':
    main()
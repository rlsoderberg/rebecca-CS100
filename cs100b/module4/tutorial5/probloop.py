from PyQt6.QtWidgets import *
from pathlib import Path
from pygame import mixer
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import os
import pathlib

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

        #set the probcount up here, because what i should really be doing is writing all of this in the probloop
        self.probtotal = 2
        self.points = 0
        self.continueloop = False

        self.show()
        #wait, can i literally just say the name of the probloop after info???
        self.info()
        #putting probloop in actual loop
        #this loop still isn't working, i don't think!!! so i'm kind of cheating on it for now...
        for self.probcount in range(0, self.probtotal):
            #now here is where i need a way to connect my different data, so i can go question by question 
            #for now, it works, and that's fine, because i actually need to go read the dark tower
            #i'll have to come back and look at it again in... well, maybe not in THAT long...
            #oh wait!!!! all i have to do is use different filenames!!!
            self.probloop(self.probcount)
        

    #alright, well... data??? uhhhh, i'm sure we've covered how to import from text files... so i need:
    #A) a txt of questions
    #B) a txt of image filenames
    #C) images
    #D) a txt of correct numbers
    #E) a txt of answer options
    def probloop(self, probcount):

        self.get_variables(probcount)
        self.select = 0


        #i want to use some kind of loop to keep it from automatically going to the last question
        #'while self.select == 0' totally did not work!!!

        #so, REALLY... all i should have to do is setText, right?
        self.title.setText(str(probcount + 1) + '. ' + self.thisquestion)

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
        
        #well, i was going to put something here, to make it repeat the question if you're wrong
        #but i guess that's not entirely necessary
        #if self.select != 0 and self.select != self.correct:
        #    self.select = 0


    def click1(self):
        #print('magicians')
        self.button1.setStyleSheet('QPushButton {background-color: red}')
        self.button2.setStyleSheet('QPushButton {background-color: blue}')
        self.button3.setStyleSheet('QPushButton {background-color: blue}')
        self.select = 1
    def click2(self):
        #print('villagers')
        self.button2.setStyleSheet('QPushButton {background-color: red}')
        self.button1.setStyleSheet('QPushButton {background-color: blue}')
        self.button3.setStyleSheet('QPushButton {background-color: blue}')
        self.select = 2
    def click3(self):
        #print('demons')
        self.button3.setStyleSheet('QPushButton {background-color: red}')
        self.button1.setStyleSheet('QPushButton {background-color: blue}')
        self.button2.setStyleSheet('QPushButton {background-color: blue}')
        self.select = 3 
    def submit(self):
        #oh, well, it became obvious when i actually printed the select & correct values
        #i have to put this in a separate function...
        print(f'self.select = {self.select}')
        print(f'self.correct = {self.correct}')
        #oh, they were different variable types. are we surprised?
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
        self.continueloop = False
    def corrects(self):
        QMessageBox.information(
            self,
            'Information',
            'This is important information.'
        )
        self.continueloop = True
        """
        QMessageBox.information(
            self,
            'Banjo Tyrwo',
            'That is correct!'
            #for some reason, it doesn't like my correctline, so i'm just using a generic one for now
            #self.correctline

            #well, these text variables just won't be correct, but we're going to ignore that for now...
            
            #oh right!!! i need to stop it between loops...
            #i guess i should include the corrects?
            self.next_question = True

        )
        """
        self.probcount += 1
        self.points += 1
    def incorrects(self):
        QMessageBox.information(
            self,
            'Information',
            'This is important information.'
        )

    def get_variables(self, probcount):
        #i am putting this in its own function because it is a lot

        #import all the files - first, questions
        questionlist = open("img/questionlist.txt", "r")

        data = questionlist.read()
        self.questionlist = data.replace('\n', ' ').split(".")
        questionlist.close()

        self.thisquestion = self.questionlist[probcount]

        #images. now, HOW am i going to reference images within a specific subfolder?
        #i can do images up here, because i've got self.filenames!
        dir = (f"./img/{probcount + 1}")
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
        #this is pretty awkward... subtracting 1...
        self.correct = self.correctlist[probcount]
        self.correcttxt.close()

        #answer options
        #using dirlist again
        for file in self.dirlist:
            if file.endswith('.txt'):
                self.optionlist = file
        
        #uh, i wasn't expecting this complicated address to work, but it might have? idk?
        self.optiontxt = open(f'img/{probcount + 1}/{str(self.optionlist)}', "r")

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
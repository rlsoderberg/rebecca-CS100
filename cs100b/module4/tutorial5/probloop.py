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

        self.setLayout(self.mainlayout)

        #set the probcount up here, because what i should really be doing is writing all of this in the probloop
        probtotal = 1

        self.show()
        #wait, can i literally just say the name of the probloop after info???
        self.info()
        #putting probloop in actual loop
        #this loop still isn't working, i don't think!!! so i'm kind of cheating on it for now...
        for e in range(probtotal):
            #now here is where i need a way to connect my different data, so i can go question by question 
            #for now, it works, and that's fine, because i actually need to go read the dark tower
            #i'll have to come back and look at it again in... well, maybe not in THAT long...
            #oh wait!!!! all i have to do is use different filenames!!!
            self.probloop(probtotal)
        

    #alright, well... data??? uhhhh, i'm sure we've covered how to import from text files... so i need:
    #A) a txt of questions
    #B) a txt of image filenames
    #C) images
    #D) a txt of correct numbers
    #E) a txt of answer options
    def probloop(self, probcount):

        self.get_variables(probcount)

        title = QLabel(objectName='title')
        title.setText(self.thisquestion)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainlayout.addWidget(title)

        self.mainlayout.addLayout(self.imglayout)

        #label/QPixMap widget
        label1 = QLabel()
        #at first i was trying to use (f"img/{imagelist[1]}") for my pixmap...
        #i had to get around it by posting duplicate images in the main folder!!!
        img1 = QPixmap(self.imagelist[0])
        label1.setPixmap(img1)
        self.imglayout.addWidget(label1)

        #label/QPixMap widget
        label2 = QLabel()
        img2 = QPixmap(self.imagelist[1])
        label2.setPixmap(img2)
        self.imglayout.addWidget(label2)

        #label/QPixMap widget
        label3 = QLabel()
        img3 = QPixmap(self.imagelist[2])
        label3.setPixmap(img3)
        self.imglayout.addWidget(label3)

        self.mainlayout.addLayout(self.sublayout)
        
        self.select = 0

        #correctness still isn't working!!!! i really don't know which of my things are in the right place...
        self.button1 = QPushButton("MAGICIANS")
        self.button1.clicked.connect(self.click1)
        self.sublayout.addWidget(self.button1)

        self.button2 = QPushButton("VILLAGERS")
        self.button2.clicked.connect(self.click2)
        self.sublayout.addWidget(self.button2)

        self.button3 = QPushButton("DEMONS")
        self.button3.setGeometry(100,100,100,100)
        self.button3.clicked.connect(self.click3)
        self.sublayout.addWidget(self.button3)

        self.button = QPushButton("Submit")
        self.button.setIcon(QIcon('img/submit.png'))
        self.button.clicked.connect(self.submit)
        self.mainlayout.addWidget(self.button)

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
        print(f'why are these two different things??? {self.select} = {self.correct}!!!!')
        #i renamed the functions so it didn't get confused, but they're still not working...
        if self.select == self.correct:
            print('you are correct')
            #wait, this isn't working again!!!
            self.corrects()
        elif self.select != self.correct:
            #why am i incorrect????
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
            'That is correct! \nPoints:1/1'
        )
    def incorrects(self):
        QMessageBox.information(
            self,
            'Banjo Tyrwo',
            'That is incorrect! \nPoints:0/0'
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
        #this is pretty awkward... subtracting 1...
        self.correct = self.correctlist[probcount - 1]
        self.correcttxt.close()

        #answer options
        #using dirlist again
        for file in self.dirlist:
            if file.endswith('.txt'):
                optionlist = file
        print(f'optionslist: {optionlist}')



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
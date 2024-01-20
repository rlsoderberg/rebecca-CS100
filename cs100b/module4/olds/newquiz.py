#ok, well, it seems like pyqt is made more for interfaces, not for creating new screens
#i will make a new version of this quiz program, and i can use message boxes for a lot of the stuff 
#but look, i started, and now everything is incorrect!
#i am going to have to just rewrite this whole thing sometime
#i totally am not doing variables right!

from PyQt6.QtWidgets import *
from pathlib import Path
from pygame import mixer
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

#Banjo Tyrwo: Bango Gyro/The Dark Tower crossover
class mainwindow (QWidget):
    def __init__(self, parent = None):
        #super init
        super(mainwindow, self).__init__(parent)

        #set window title
        self.setWindowTitle("Banjo Tyrwo")

        #qvbox for button
        mainlayout = QVBoxLayout()
        #qhboxlayout for images 
        imglayout = QHBoxLayout()
        #qhboxlayout for subheadings 
        sublayout = QHBoxLayout()

        self.setLayout(mainlayout)
        
        title = QLabel(objectName='title')
        title.setText("1. We are on the lookout for")
        #a center align that works!!! i had to import qt from qtcore. not sure how to put this into qss?
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainlayout.addWidget(title)

        mainlayout.addLayout(imglayout)

        #label/QPixMap widget
        label1 = QLabel()
        img1 = QPixmap("img/magicians.png")
        label1.setPixmap(img1)
        imglayout.addWidget(label1)

        #label/QPixMap widget
        label2 = QLabel()
        img2 = QPixmap("img/villagers.png")
        label2.setPixmap(img2)
        imglayout.addWidget(label2)

        #label/QPixMap widget
        label3 = QLabel()
        img3 = QPixmap("img/demons.png")
        label3.setPixmap(img3)
        imglayout.addWidget(label3)

        mainlayout.addLayout(sublayout)
        self.select = 0
        self.correct = 3

        self.button1 = QPushButton("MAGICIANS")
        self.select = self.button1.clicked.connect(self.click1)
        sublayout.addWidget(self.button1)

        self.button2 = QPushButton("VILLAGERS")
        self.select = self.button2.clicked.connect(self.click2)
        sublayout.addWidget(self.button2)

        self.button3 = QPushButton("DEMONS")
        self.button3.setGeometry(100,100,100,100)
        self.select = self.button3.clicked.connect(self.click3)
        sublayout.addWidget(self.button3)

        self.button = QPushButton("Submit")
        self.button.setIcon(QIcon('img/submit.png'))
        mainlayout.addWidget(self.button)

        if self.select == self.correct:
            self.button.clicked.connect(self.correct)
        else:
            self.button.clicked.connect(self.incorrect)

        self.show()
        self.info()
            
    def click1(self):
            #print('magicians')
            self.button1.setStyleSheet('QPushButton {background-color: red}')
            #this seems like not the best way to do this either
            self.button2.setStyleSheet('QPushButton {background-color: blue}')
            self.button3.setStyleSheet('QPushButton {background-color: blue}')
            self.select = 1
            return(self.select)
    def click2(self):
            #print('villagers')
            self.button2.setStyleSheet('QPushButton {background-color: red}')
            self.button1.setStyleSheet('QPushButton {background-color: blue}')
            self.button3.setStyleSheet('QPushButton {background-color: blue}')
            self.select = 2
            return(self.select)
    def click3(self):
            #print('demons')
            self.button3.setStyleSheet('QPushButton {background-color: red}')
            self.button1.setStyleSheet('QPushButton {background-color: blue}')
            self.button2.setStyleSheet('QPushButton {background-color: blue}')
            self.select = 3
            return(self.select)
    
    def info(self):
        QMessageBox.information(
            self,
            'Banjo Twyro',
            'Answer all questions\nto gain super combo'
        )
    def correct(self):
        QMessageBox.information(
            self,
            'That is correct!',
            'Answer all questions\nto gain super combo'
        )
    def incorrect(self):
        QMessageBox.information(
            self,
            'Banjo Twyro',
            'That is incorrect!'
        )

    def button_clicked(self):
        if self.select == self.correct:
            self.button.clicked.connect(self.correct)
        else:
            self.button.clicked.connect(self.incorrect)

         
         
    def question2(self):
        self.title.setText("2. What did the bulldozer say to the dishwasher?")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainlayout.addWidget(title)

        self.mainlayout.addLayout(self.imglayout)

        #label/QPixMap widget
        label1 = QLabel()
        img1 = QPixmap("villagers.png")
        label1.setPixmap(img1)
        self.imglayout.addWidget(label1)

        #label/QPixMap widget
        label2 = QLabel()
        img2 = QPixmap("villagers.png")
        label2.setPixmap(img2)
        self.imglayout.addWidget(label2)

        #label/QPixMap widget
        label3 = QLabel()
        img3 = QPixmap("villagers.png")
        label3.setPixmap(img3)
        self.imglayout.addWidget(label3)
            

def main():
    #don't stick the music right in the middle
    #pygame wins for now
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


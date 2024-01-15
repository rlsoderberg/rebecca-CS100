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

        self.setGeometry(100,100,350,300)

        #qvbox for button
        self.mainlayout = QVBoxLayout()
        #qhboxlayout for images 
        self.imglayout = QHBoxLayout()
        #qhboxlayout for subheadings 
        self.sublayout = QHBoxLayout()

        self.setLayout(self.mainlayout)

        self.show()
        #wait, can i literally just say the name of the probloop after info???
        self.info()
        self.probloop()
        

    #i'm going to have to import data later...
    def probloop(self):
        #import data here
        title = QLabel(objectName='title')
        title.setText("1. We are on the lookout for")
        #a center align that works!!! i had to import qt from qtcore. not sure how to put this into qss?
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainlayout.addWidget(title)

        self.mainlayout.addLayout(self.imglayout)

        #import data here
        #label/QPixMap widget
        label1 = QLabel()
        img1 = QPixmap("img/magicians.png")
        label1.setPixmap(img1)
        self.imglayout.addWidget(label1)

        #label/QPixMap widget
        label2 = QLabel()
        img2 = QPixmap("img/villagers.png")
        label2.setPixmap(img2)
        self.imglayout.addWidget(label2)

        #label/QPixMap widget
        label3 = QLabel()
        img3 = QPixmap("img/demons.png")
        label3.setPixmap(img3)
        self.imglayout.addWidget(label3)

        self.mainlayout.addLayout(self.sublayout)
        
        #import data here
        self.select = 0
        self.correct = 3

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
        self.mainlayout.addWidget(self.button)

        #well, i forgot this part... THAT might be a problem...
        #everything is still incorrect though, so i need to fix my variables still, i guess
        if self.select == self.correct:
            self.button.clicked.connect(self.correct)
        else:
            self.button.clicked.connect(self.incorrect)

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
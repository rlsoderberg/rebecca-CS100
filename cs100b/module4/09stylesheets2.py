#pyqt6 tutorial pt 3 - displaying image with qlabel
#pyqt6 tutorial pt 4 - adding icon to button

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
        title.setText("We are on the lookout for")
        #a center align that works!!! i had to import qt from qtcore. not sure how to put this into qss?
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainlayout.addWidget(title)

        mainlayout.addLayout(imglayout)

        #label/QPixMap widget
        label1 = QLabel()
        img1 = QPixmap("magicians.png")
        label1.setPixmap(img1)
        imglayout.addWidget(label1)

        #label/QPixMap widget
        label2 = QLabel()
        img2 = QPixmap("villagers.png")
        label2.setPixmap(img2)
        imglayout.addWidget(label2)

        #label/QPixMap widget
        label3 = QLabel()
        img3 = QPixmap("demons.png")
        label3.setPixmap(img3)
        imglayout.addWidget(label3)
        
        #sublayout doesn't seem like the best way to do this
        #i will do the tutorials and then find a better way, right???

        mainlayout.addLayout(sublayout)

        self.button1 = QPushButton("MAGICIANS")
        self.button1.clicked.connect(self.click1)
        sublayout.addWidget(self.button1)

        self.button2 = QPushButton("VILLAGERS")
        self.button2.clicked.connect(self.click2)
        sublayout.addWidget(self.button2)

        self.button3 = QPushButton("DEMONS")
        #honestly, idk how to set geometry
        self.button3.setGeometry(100,100,100,100)
        self.button3.clicked.connect(self.click3)
        sublayout.addWidget(self.button3)

        button = QPushButton("Submit")
        button.setIcon(QIcon('submit.png'))
        mainlayout.addWidget(button)

        self.show()
            
    def click1(self):
            print('magicians')
            self.button1.setStyleSheet('QPushButton {background-color: red}')
            #this seems like not the best way to do this either
            self.button2.setStyleSheet('QPushButton {background-color: blue}')
            self.button3.setStyleSheet('QPushButton {background-color: blue}')
    def click2(self):
            print('villagers')
            self.button2.setStyleSheet('QPushButton {background-color: red}')
            self.button1.setStyleSheet('QPushButton {background-color: blue}')
            self.button3.setStyleSheet('QPushButton {background-color: blue}')
    def click3(self):
            print('demons')
            self.button3.setStyleSheet('QPushButton {background-color: red}')
            self.button1.setStyleSheet('QPushButton {background-color: blue}')
            self.button2.setStyleSheet('QPushButton {background-color: blue}')
            

def main():
    #don't stick the music right in the middle
    #pygame wins for now
    mixer.init()
    mixer.music.load("banjo.wav")
    mixer.music.play()

    app = QApplication([])
    app.setStyleSheet(Path('style.qss').read_text())
    w = mainwindow()
    w.show()
    #at one point, sys.exit(app.exec()) seemed necessary for the combo box to work, but idk
    app.exec()

if __name__ == '__main__':
    main()

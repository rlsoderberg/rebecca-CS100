#pyqt6 tutorial pt 3 - displaying image with qlabel

from PyQt6.QtWidgets import *
from pathlib import Path
from pygame import mixer
from PyQt6.QtGui import QPixmap

#Banjo Tyrwo: Bango Gyro/The Dark Tower crossover
class mainwindow (QWidget):
    def __init__(self, parent = None):
        #super init
        super(mainwindow, self).__init__(parent)
        #set geometry
        self.setGeometry(500, 100, 300, 50)

        #set window title
        self.setWindowTitle("Banjo Tyrwo")

        #list of labels
        labels = ['first name', 'last name', 'email']
        #dictionary of textboxes
        #this is a property
        self.textboxes = {}

        #qvbox for button
        mainlayout = QVBoxLayout()
        #qhboxlayout for images 
        imglayout = QHBoxLayout()

        self.setLayout(mainlayout)
        
        title = QLabel("We are on the lookout for")
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
        
        button = QPushButton("Submit")
        mainlayout.addWidget(button)

        self.show()

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

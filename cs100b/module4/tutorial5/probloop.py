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
        #putting probloop in actual loop
        probcount = 1
        for e in range(probcount):
            #now here is where i need a way to connect my different data, so i can go question by question 
            #for now, it works, and that's fine, because i actually need to go read the dark tower
            #i'll have to come back and look at it again in... well, maybe not in THAT long...
            self.probloop()
        

    #alright, well... data??? uhhhh, i'm sure we've covered how to import from text files... so i need:
    #A) a txt of questions
    #B) a txt of image filenames
    #C) images
    #D) a txt of correct numbers
    #E) a txt of possible answers
    def probloop(self):
        #like, what though? why is it looping twice?
        print('loopcount')
        title = QLabel(objectName='title')
        title.setText("1. We are on the lookout for")
        #a center align that works!!! i had to import qt from qtcore. not sure how to put this into qss?
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainlayout.addWidget(title)

        self.mainlayout.addLayout(self.imglayout)

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
        #i renamed the functions so it didn't get confused, but they're still not working...
        if self.select == self.correct:
            #OH, well, i don't really need these connections now, do i...
            self.corrects()
        else:
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
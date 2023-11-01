from PyQt6.QtWidgets import *
from pathlib import Path
from pygame import mixer

#Banjo Tyrwo: Bango Gyro/The Dark Tower crossover
class mainwindow (QWidget):
    def __init__(self, parent = None):
        #super init
        super(mainwindow, self).__init__(parent)
        #set geometry
        self.setGeometry(300, 100, 300, 50)
        #set window title
        self.setWindowTitle("Banjo Tyrwo")

        #list of labels
        labels = ['first name', 'last name', 'email']
        #dictionary of textboxes
        #this is a property
        self.textboxes = {}

        #grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("We are on the lookout for")
        #addWidget(QWidget, row, column, rowspan, column span)
        layout.addWidget(title)

        self.checkbox1 = QComboBox()
        self.checkbox1.addItems(['1. Magicians', '2. Villagers', '3. Demons'])
        layout.addWidget(self.checkbox1)
        
        button = QPushButton("Submit")
        layout.addWidget(button)

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

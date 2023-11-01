from PyQt6.QtWidgets import *

from playsound import playsound

#Banjo Tyrwo: Bango Gyro/The Dark Tower crossover
class mainwindow (QWidget):
    def __init__(self, parent = None):
        #super init
        super(mainwindow, self).__init__(parent)
        #set geometry
        self.setGeometry(100, 100, 800, 50)
        #set window title
        self.setWindowTitle("Banjo Tyrwo")

        #list of labels
        labels = ['first name', 'last name', 'email']
        #dictionary of textboxes
        #this is a property
        self.textboxes = {}

        #grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        title = QLabel("We are on the lookout for")
        #addWidget(QWidget, row, column, rowspan, column span)
        layout.addWidget(title, 1, 1, 1, 1)

        #add label
        b1 = QLabel("1. Magicians")
        #addWidget(QWidget, row, column)
        layout.addWidget(b1, 2, 0)

        #add textbox
        b2 = QLabel("2. Villagers")
        #addWidget(QWidget, row, column)
        layout.addWidget(b2, 2, 1)

        #add textbox
        b3 = QLabel("3. Demons")
        #addWidget(QWidget, row, column)
        layout.addWidget(b3, 2, 2)


        b = QPushButton("Submit")
        #addWidget(QWidget, row, column, rowspan, column span)
        layout.addWidget(b, len(labels), 1, 1, 1)

        self.show()

def main():
    app = QApplication([])
    app.setStyleSheet(Path('style.qss').read_text())
    w = mainwindow()
    playsound.playsound('banjo.wav')
    w.show()
    app.exec()

if __name__ == '__main__':
    main()

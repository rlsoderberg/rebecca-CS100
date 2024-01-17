#after sleeping on this, i thought... we really don't need a signal on close message box
#first i thought, can't we do a signal on open message box? but that seems awkward
#more importantly, i realized that the message box has buttons! surely those can emit a signal
#so... with that, i think i'd also have to abandon the for loop
#instead count with while < and incremented counter

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('QMessageBox')
        self.setGeometry(100, 100, 300, 100)

        self.mainlayout = QHBoxLayout()
        self.setLayout(self.mainlayout)

        #so... the important thing is the info message box & the submit message box

        self.button = QPushButton('THE BUTTON')
        self.button.clicked.connect(self.submit)
        self.mainlayout.addWidget(self.button)

        self.show()
        #and i'm still going to sneakily put this here!!! yeah!!!
        self.info()
    
    def info(self):
        msgBox = QMessageBox.information(
            self,
            'Banjo Tyrwo',
            'Answer all questions\nto gain super combo.\nYou have one minute\nto answer each question.'
        )
        #well, that's one internet thing that didn't work! 
        #i'd like to omit the x button because how do you get a signal from that?
        msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
    def submit(self):
        if int(self.select) == int(self.correct):
            self.corrects()
        elif self.select != self.correct:
            self.incorrects()
        self.interaction_marker = True
    
    


if __name__ == '__main__':
    app = QApplication([])
    w = MainWindow()
    sys.exit(app.exec())
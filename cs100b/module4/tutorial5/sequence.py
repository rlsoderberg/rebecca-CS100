#ok, so i thought, let me just make a simple program with what i'm actually trying to do
#so where i'm stuck is emitting a signal when you close a message box?
#that's why i saved the zetcode guy, because he has a bunch of stuff and i'm like, maybe i should steal this
#so i'm going to try and use some of his code right now...
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *

#this is from zetguy. creating a whole new class? whooaaa!!!
#honestly, the rest of it... idk. it's about closing app, which, i want closing message box, right?
#but this is sure cool. creating a class? wow. qobject? what? cool.
class Communicate(QObject):

    closeApp = pyqtSignal()

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('QMessageBox')
        self.setGeometry(100, 100, 300, 100)

        layout = QHBoxLayout()
        self.setLayout(layout)

        #so... the important thing is the info message box & the submit message box

        self.button = QPushButton('THE BUTTON')
        self.button.clicked.connect(self.submit)
        self.mainlayout.addWidget(self.button)

        self.show()
        #and i'm still going to sneakily put this here!!! yeah!!!
        self.info()
    
    def info(self):
        QMessageBox.information(
            self,
            'Banjo Tyrwo',
            'Answer all questions\nto gain super combo.\nYou have one minute\nto answer each question.'
        )
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
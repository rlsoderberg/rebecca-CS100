#well, ok, i tried to isolate the click interaction
#you know what i got stuck on? self.setlayout!!! come on!!!

#so... it's about how you label the function? like mousePressEvent? that is sooo weird

import math
import sys
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.resize(500,500)
        self.setWindowTitle("Tic-Tac-Toe")

        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)

        self.title = QLabel(objectName='title')
        self.title.setText('Click Anywhere')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainlayout.addWidget(self.title)

    def mousePressEvent(self, event):
        print(f'event position x = {event.position().x()}')
        print(f'event position y = {event.position().y()}')

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
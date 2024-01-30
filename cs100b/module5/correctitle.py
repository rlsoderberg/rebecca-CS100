import math
import sys
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets

class MainWindow (QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.resize(500,500)
        self.setWindowTitle("Tic-Tac-Toe")

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.title = QLabel(objectName='title')
        self.title.setText('We are on the lookout for')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.title)

#respond to mousepress events
def mousePressEvent(self, event):
    print(f'event position x = {event.position().x()}')
    print(f'event position y = {event.position().x()}')

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()
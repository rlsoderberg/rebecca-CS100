#first thing from the tutorials, i need to look at signals!!!
#can i get this new window program to work without all those classes?
#well, here's the thing, doesn't it make sense to have a window that's a separate class?
#so how do you pass the location in THERE?
#like, i've tried including a location keyword in this argument on line 53 'self.w = secondwindow()'
#but then it complains about arguments!!!

import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtGui

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        screen = QtGui.QGuiApplication.primaryScreen()
        screenWidth = screen.geometry().width()
        screenHeight = screen.geometry().height()

        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a location:', self)

        self.cb_location = QComboBox(self)
        self.cb_location.addItem('Upper Left')
        self.cb_location.addItem('Upper Right')
        self.cb_location.addItem('Lower Left')
        self.cb_location.addItem('Lower Right')

        location_label = self.cb_location.activated.connect()
        print(location_label)

        self.result_label = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cb_location)
        layout.addWidget(self.result_label)

    def update(self):
        if self.cb_location.currentText() == 'Upper Left':
            self.result_label.setText('Upper Left')
            self.x = 50
            self.y = 50
        elif self.cb_location.currentText() == 'Upper Right':
            self.result_label.setText('Upper Right')
            self.x = (screenWidth - 250)
            self.y = 50
        elif self.cb_location.currentText() == 'Lower Left':
            self.result_label.setText('Lower Left')
            self.x = 50
            self.y = (screenHeight - 100)
        elif self.cb_location.currentText() == 'Lower Right':
            self.result_label.setText('Lower Right')
            self.x = (screenWidth - 250)
            self.y = (screenHeight - 100)

    def show_new_window(self):
        if self.w is None:
            self.w = secondwindow(self.x, self.y)
            self.w.show()

        else:
            self.w = None

        b = QLabel(self)
        # announce our presence with authority
        b.setText('push to toggle window')

#so... i'm trying to figure out how to pass in location!!!
#oh wait!!! something just happened!!! i labeled them with MainWindow!!! aha!!!
#uhhhh, now i'm getting this weird error about metaclass conflict
#am i supposed to make this a subclass, or something?
#but it seems be more correct to have secondwindow in a separate class
#also... i don't get metaclasses
#i'm going to move on from this, for now, and see if the tutorial will help me...
class secondwindow(QWidget, MainWindow.x, MainWindow.y):

    def __init__(self, x, y):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setGeometry(x, y, 200, 50)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
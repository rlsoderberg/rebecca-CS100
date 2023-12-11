#oops, i think i only went through the first section of the pyqt tutorials
#i'll go through them all later!!! but here's the one on combo boxes, which i will use to get mine working

import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtGui



class MainWindow(QWidget):
    def __init__(self, parent = None:
        super(mainwindow, self).__init__(parent)

        #maybe we could skip this whole screen size thing... maybe there's a way to do negative coords

        #for now... this one seems to give me the correct w&h, but 'cannot unpack non-iterable QRect object'
        #this one gave me height of 720, while the other one gave me 768, so i'm keeping it just in case
        #geometry = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        #print(geometry)
        screen = QtGui.QGuiApplication.primaryScreen()
        screenWidth = screen.geometry().width()
        screenHeight = screen.geometry().height()
        print(f'{screenWidth}, {screenHeight}')

        # create a grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a platform:', self)

        # create a combobox
        self.cb_location = QComboBox(self)
        self.cb_location.addItem('Upper Left')
        self.cb_location.addItem('Upper Right')
        self.cb_location.addItem('Lower Left')
        self.cb_location.addItem('Lower Right')

        self.cb_location.activated.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cb_location)
        layout.addWidget(self.result_label)

        self.update()
        
        # show the window
        self.show()

    def show_new_window(self, label):
        if self.w is None:
            if label == 'UL':
                self.w = UL_Window()
            elif label == 'UR':
                self.w = UR_Window(screenWidth)
            self.w.show()

        else:
            self.w = None


    def update(self):
        if self.cb_location.currentText() == 'Upper Left':
            self.result_label.setText('Upper Left')
            self.show_new_window('UL')
        elif self.cb_location.currentText() == 'Upper Right':
            self.result_label.setText('Upper Right')
            self.show_new_window('UR')
        elif self.cb_location.currentText() == 'Lower Left':
            self.result_label.setText('Lower Left')
        elif self.cb_location.currentText() == 'Lower Right':
            self.result_label.setText('Lower Right')

#is this REALLY the best way to do it? to make a class for each window location???
class UL_Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("UL Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setGeometry(50, 50, 200, 50)

class UR_Window(QWidget):
    def __init__(self, screenWidth):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("UR Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setGeometry((screenWidth - 50), 50, 200, 50)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
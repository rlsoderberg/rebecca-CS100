#right, ok, how many of these tutorials am i actually going to do right now???
#first i want to see if i can get my window location program to work, along with my first quiz program
#well... maybe i'll finish section 4 & section 5 first
#after 5, that sounds like it's all brand new stuff and idk if i want to do it right now!!!

#i'm finally getting around to sections 4 and 5!
#maybe tmi, but the notes do help me keep track of where i am, between long periods of sloth
#next is... QSpinBox

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(100, 100, 200, 50)
        self.setWindowTitle('QSpinBox')

        layout = QFormLayout()
        self.setLayout(layout)

        level = QSpinBox(minimum = 1, maximum = 62, value = 30, prefix = 'Level ')

        level.valueChanged.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addRow('Panda Level: ', level)

        layout.addRow(self.result_label)

        self.show()

    def update(self, value):
        self.result_label.setText(f'Current Panda Level: {value}')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

#a lot of these are going to be the same!!!
#i'm copy pasting until i get to something new...

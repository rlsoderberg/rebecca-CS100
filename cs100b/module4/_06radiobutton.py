import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

from _testimport import firstclass

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('PyQt6 QRadioButton')
        self.setMinimumWidth(300)

        #we are using a qvbox with endless height and minimum width!
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Please select a platform: ', self)

        #3 different buttons
        rb_android = QRadioButton('Android', self)
        rb_android.toggled.connect(self.update)

        rb_ios = QRadioButton('iOS', self)
        rb_ios.toggled.connect(self.update)

        rb_windows = QRadioButton('Windows', self)
        rb_windows.toggled.connect(self.update)

        #on this one, instead of printing to console, we are making a label
        self.result_label = QLabel('', self)

        layout.addWidget(label)
        layout.addWidget(rb_android)
        layout.addWidget(rb_ios)
        layout.addWidget(rb_windows)
        #do not forget self!!!
        layout.addWidget(self.result_label)

        self.show()

    #i am guessing that value will magically appear again?
    def update(self): #, value):
        #get the radio button to send the signal
        #wait, what? this time we are finding sender INSIDE the function
        rb = self.sender()

        if rb.isChecked():
            self.result_label.setText(f'You selected {rb.text()}.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #oh cool, you can print the arguments! well... it has one argument, the filename. 
    #would it have more arguments if it used more files?
    default = firstclass('bob')
    default.print_problem()
    #well, that wasn't it!!! ohhh well...
    print("Arguments:", sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


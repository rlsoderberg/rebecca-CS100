#import pyqt6
from PyQt6.QtWidgets import *


class mainwindow(QWidget):
    #constructor setting window properties
    def __init__(self, parent = None):
        #super calls parent class
        super(mainwindow, self).__init__(parent)
        #set window size
        self.setGeometry(100, 100, 200, 50)
        #set window title
        self.setWindowTitle('PyQt6')

        #list of labels for textboxes
        labels = ['first name: ', 'last name: ', 'email: ']
        #dictionary where we will store the input for each label. wait, why are we using this?
        self.textboxes = {}

        #set window layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        for l in labels:
            #make label item for each label
            lbl = QLabel(l)
            layout.addWidget(lbl)

            #text input for label
            txt = QLineEdit()
            layout.addWidget(txt)
            #put input in dictionary
            self.textboxes[l] = txt

        #make button
        b = QPushButton('Submit')
        layout.addWidget(b)

        self.show()

def main():
    #why does QApplication have brackets in parentheses?
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

#run only from this file directly
if __name__ =='__main__':
    main()






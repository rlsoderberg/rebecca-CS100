#why is it QtWidgets up here but QWidgets down there???
from PyQt6.QtWidgets import *

#main window class with parent class of QWidget
class mainwindow (QWidget):
    def __init__(self, parent = None):
        #super init
        super(mainwindow, self).__init__(parent)
        #set geometry
        self.setGeometry(100, 100, 200, 50)
        #set window title
        self.setWindowTitle("PyQt6")

        #list of labels
        labels = ['first name', 'last name', 'email']
        #dictionary of textboxes
        #this is a property
        self.textboxes = {}

        #grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        row = 0
        for l in labels:
            #add label
            lbl = QLabel(l)
            #addWidget(QWidget, row, column)
            layout.addWidget(lbl, row, 0)

            #add textbox
            txt = QLineEdit()
            #display beside label
            layout.addWidget(txt, row, 1)
            #store in dictionary
            self.textboxes[l] = txt

            row = row + 1

        b = QPushButton("Submit")
        #button at bottom, spanning both columns
        #addWidget(QWidget, row, column, rowspan, column span)
        layout.addWidget(b, len(labels), 0, 1, 2)

        self.show()

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__=="__main__":
    main()







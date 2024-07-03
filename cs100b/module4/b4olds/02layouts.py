from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        #need to call super-class __init__()
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle('PyQt6')

        #QHBoxLayout horizontally displays widgets
        layout = QHBoxLayout()
        self.setLayout(layout)
        #QLabels take labels all on one line, then add as Widget, with QHBoxLayout?
        b = QLabel('Hello')
        layout.addWidget(b)
        b = QLabel('World')
        layout.addWidget(b)

        self.show()

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    #no need to exit sys, because execution is being taken care of by QApplication?
    app.exec()

if __name__ == '__main__':
    main()

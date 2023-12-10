import sys
from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        # Set the window size
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("PyQt6")

        #Set up a horizontal layout
        # and show a couple of labels
        layout = QHBoxLayout()
        self.setLayout(layout)
        b = QLabel("Hello")
        layout.addWidget(b)
        b = QLabel("World")
        layout.addWidget(b)

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
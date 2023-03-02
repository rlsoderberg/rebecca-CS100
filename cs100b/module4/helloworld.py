import sys
from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("PyQt6")

        b = QLabel(self)
        b.setText("Hello World!")

        self.show()

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
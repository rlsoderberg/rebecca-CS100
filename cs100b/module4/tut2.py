#pyqt tutorial 2 - signals and slots, pt 2 (line_edit.textChanged/label.setText)

from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setWindowTitle("Qt Signals & Slots")

        label = QLabel()
        line_edit = QLineEdit()
        #textChanged signal goes to setText slot!
        line_edit.textChanged.connect(label.setText)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        self.setLayout(layout)

        self.show()

def main():
    #you always forget the brackets in the parentheses!!!!
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == "__main__":
    main()
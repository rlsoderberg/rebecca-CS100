from PyQt6.QtWidgets import *

class mainwindow (QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100, 100, 200, 50)
        self.setWindowTitle("PyQt6")

        labels = ['first name', 'last name', 'email']
        self.textboxes = {}

        #qformlayout
        layout = QFormLayout()
        self.setLayout(layout)

        for l in labels:
            txt = QLineEdit()
            #addRow automatically combines l with txt
            layout.addRow(l, txt)
            self.textboxes[l] = txt

        b = QPushButton("Submit")
        layout.addWidget(b)

        self.show()

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()



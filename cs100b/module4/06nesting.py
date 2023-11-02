from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("PyQt6")

        labels = ['first name', 'last name', 'email']
        self.textboxes = {}

        #qvbox for button
        mainlayout = QVBoxLayout()
        #formlayout for input rows 
        formlayout = QFormLayout()
        
        self.setLayout(mainlayout)
        mainlayout.addLayout(formlayout)

        for l in labels:
            txt = QLineEdit()
            formlayout.addRow(l, txt)
            self.textboxes[l] = txt

        #qvlayout button defaults to full width?
        b = QPushButton("Submit")
        mainlayout.addWidget(b)

        self.show()

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == "__main__":
    main()






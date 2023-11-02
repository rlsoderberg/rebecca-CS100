from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("PyQt6")

        labels = ['first name', 'last name', 'email']
        self.textboxes = {}

        layout = QFormLayout()
        self.setLayout(layout)

        for l in labels:
            txt = QLineEdit()
            layout.addRow(l, txt)
            self.textboxes[l] = txt

        b = QPushButton("Submit")
        #connect click signal to member function
        b.clicked.connect(self.button_clicked)
        layout.addWidget(b)

        #create an empty label
        self.labelResult = QLabel()
        layout.addWidget(self.labelResult)

        self.show()

    #new method sets result of empty label to show user input for first name
    def button_clicked(self):
        self.labelResult.setText(self.textboxes['first name'].text())
        

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__=="__main__":
    main()
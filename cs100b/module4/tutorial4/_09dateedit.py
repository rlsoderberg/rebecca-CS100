#well, i tried editing it so you could submit the date
#and i totally don't get how to pass things in and out of the functions!
#but it kind of started working anyway? whoa freaky

#oh, you know, i never labeled value as self.value, maybe that has something to do with it, idk tho

#ohhh, i was printing type(value)
#how did that even get there???
#anyway, I'm going to try to set result label in a way that's easier to understand

#ohhh, it was already setting result label, but with editingFinished, which weirds me out
#like, what even is that???
#also, toPyDate() is a thing apparently

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(100, 100, 200, 50)
        self.setWindowTitle('QDateEdit')

        layout = QFormLayout()
        self.setLayout(layout)

        self.date_edit = QDateEdit(self)


        self.result_label = QLabel('', self)

        layout.addRow('Date: ', self.date_edit)
        layout.addRow(self.result_label)

        button1 = QPushButton()
        button1.setText("Submit")

        layout.addRow(button1)
        button1.clicked.connect(self.update)

        self.show()

    def update(self):
        value = self.date_edit.date()
        self.result_label.setText((f'Date is {value.toPyDate()}.'))
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

#i have no idea how my submit button is working!!!
#and for some reason it prints <class 'PyQt6.QtCore.QDate'> 

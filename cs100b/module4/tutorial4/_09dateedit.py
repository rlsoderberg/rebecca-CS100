#well, i tried editing it so you could submit the date
#and i totally don't get how to pass things in and out of the functions!
#but it kind of started working anyway? whoa freaky

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
        self.date_edit.editingFinished.connect(self.update)


        self.result_label = QLabel('', self)

        layout.addRow('Date: ', self.date_edit)
        layout.addRow(self.result_label)

        button1 = QPushButton()
        button1.setText("Submit")

        layout.addRow(button1)

        self.show()

    def update(self):
        value = self.date_edit.date()
        print(type(value))
        self.result_label.setText(str(value.toPyDate()))
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

#i have no idea how my submit button is working!!!
#and for some reason it prints <class 'PyQt6.QtCore.QDate'> 

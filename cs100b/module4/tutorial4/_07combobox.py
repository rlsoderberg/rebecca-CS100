import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(100,100,200,50)
        self.setWindowTitle('PyQt6 QComboBox')

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel('Please select a color: ')

        self.combobox = QComboBox(self)

        self.combobox.addItem('red')
        self.combobox.addItem('blue')
        self.combobox.addItem('green')

#oh!!!!! it kept telling me 'MainWindow' object has no attribute 'result_label', and this is why!!!
#update isn't supposed to have parentheses!!!

        #comobox sends activated signal
        self.combobox.activated.connect(self.update)

        self.result_label = QLabel('', self)

        #don't foget to add widgets and show window
        layout.addWidget(title)
        layout.addWidget(self.combobox)
        layout.addWidget(self.result_label)

        self.show()

    def update(self):
        self.result_label.setText(
            f'You selected {self.combobox.currentText()}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

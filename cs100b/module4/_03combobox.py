#oops, i think i only went through the first section of the pyqt tutorials
#i'll go through them all later!!! but here's the one on combo boxes, which i will use to get mine working

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QComboBox
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QComboBox')
        self.setMinimumWidth(300)

        # create a grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a platform:', self)

        # create a combobox
        self.cb_location = QComboBox(self)
        self.cb_location.addItem('Upper Left')
        self.cb_location.addItem('Upper Right')
        self.cb_location.addItem('Lower Left')
        self.cb_location.addItem('Lower Right')

        self.cb_location.activated.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cb_location)
        layout.addWidget(self.result_label)

        # show the window
        self.show()

    def update(self):
        if self.cb_location.currentText() == 'Upper Left':
            self.result_label.setText('Upper Left')
        elif self.cb_location.currentText() == 'Upper Right':
            self.result_label.setText('Upper Right')
        elif self.cb_location.currentText() == 'Lower Left':
            self.result_label.setText('Lower Left')
        elif self.cb_location.currentText() == 'Lower Right':
            self.result_label.setText('Lower Right')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
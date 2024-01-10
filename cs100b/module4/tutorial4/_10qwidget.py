#well, i did qwidget, but qgroupbox is kind of better because you can put different kinds of things in it?
#oh well, it's basically the same, i think?

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('QWidget')

        layout = QHBoxLayout()
        self.setLayout(layout)

        #airplane pane
        airplane_pane = QWidget(self)
        form_layout = QFormLayout()
        airplane_pane.setLayout(form_layout)
        form_layout.addRow('Aircraft Manufacturer:', QLineEdit(airplane_pane))
        form_layout.addRow('Model Name:', QLineEdit(airplane_pane))
        form_layout.addRow('Model Number:', QLineEdit(airplane_pane))
        form_layout.addRow('Maximum Payload:', QLineEdit(airplane_pane))
        form_layout.addRow('Standard Seating Capacity:', QLineEdit(airplane_pane))
        form_layout.addRow('Ground Clearance:', QLineEdit(airplane_pane))
        layout.addWidget(airplane_pane)

        #airport pane
        airport_pane = QWidget(self)
        form_layout = QFormLayout()
        airport_pane.setLayout(form_layout)
        form_layout.addRow('IATA Airpot Code:', QLineEdit(airport_pane))
        form_layout.addRow('Airport Type:', QLineEdit(airport_pane))
        form_layout.addRow('Owner:', QLineEdit(airport_pane))
        form_layout.addRow('Operator:', QLineEdit(airport_pane))
        form_layout.addRow('Elevation:', QLineEdit(airport_pane))
        form_layout.addRow('Coordinates:', QLineEdit(airport_pane))
        layout.addWidget(airport_pane)

        self.show()

if __name__ == '__main__':
    app = QApplication([])
    w = MainWindow()
    sys.exit(app.exec())

#ok, so this is two forms right next to each other... now how do i do successive forms???
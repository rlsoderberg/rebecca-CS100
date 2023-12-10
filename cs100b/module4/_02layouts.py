#tie combo box to new window location
#tie cancel to close window
#tie push_button count to commit button text

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class mainwindow(QWidget):
    def __init__(self, parent = None):
        #so today i'm starting with someone's tab layout
        #this person uses self as an argument, for, like, everything
        super(mainwindow, self).__init__(parent)

        self.setWindowTitle('PyQt QTabWidget')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)

        # window pane
        personal_page = QWidget(self)
        layout = QFormLayout()
        personal_page.setLayout(layout)
        combobox1 = QComboBox()
        #here i am replacing this person's 'QComboBox(self)' with combobox1, which i think makes more sense
        layout.addRow('New Window Location:', combobox1)

        combobox1.addItem('Upper Left')
        combobox1.addItem('Upper Right')
        combobox1.addItem('Lower Left')
        combobox1.addItem('Lower Right')

        self.push_counter = 0

        # impatience pane
        contact_page = QWidget(self)
        layout = QFormLayout()
        contact_page.setLayout(layout)
        input = QLineEdit()
        layout.addRow('Impatience:', input)

        button1 = QPushButton()
        button1.setText("Commit")

        layout.addRow(button1)
        button1.clicked.connect(self.push_button)

        # add pane to the tab widget
        tab.addTab(personal_page, 'New Window')
        tab.addTab(contact_page, 'Impatience')

        main_layout.addWidget(tab, 0, 0, 2, 1)
        main_layout.addWidget(QPushButton('Open'), 2, 0,
                              alignment=Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(QPushButton('Cancel'), 2, 0,
                              alignment=Qt.AlignmentFlag.AlignRight)

        self.show()

    def push_button(self):
        self.push_counter += 1


if __name__ == '__main__':
    app = QApplication([])
    window = mainwindow()
    sys.exit(app.exec())
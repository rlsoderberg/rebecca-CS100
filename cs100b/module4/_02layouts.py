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

        self.w = None

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

        location = combobox1.currentTextChanged.connect(self.text_changed)
        #and when i try to print location it gives me some object...
        print(location)

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
        open_button = QPushButton('Open')
        main_layout.addWidget(open_button, 2, 0,
                              alignment=Qt.AlignmentFlag.AlignLeft)
        #i am trying to plug in location here, def show_new_window, call secondwindow, def secondwindow
        #but it doesn't like when i try to do that!!!
        open_button.clicked.connect(self.show_new_window)
        main_layout.addWidget(QPushButton('Cancel'), 2, 0,
                              alignment=Qt.AlignmentFlag.AlignRight)

        self.show()

    def text_changed(self, s):
        if s == 'Upper Left':
            location = 1
        elif s == 'Upper Right':
            location = 2
        elif s == 'Lower Left':
            location = 3
        elif s == 'Lower Right':
            location = 4
        
        return location

    def push_button(self):
        self.push_counter += 1

    def show_new_window(self):
        if self.w is None:
            self.w = secondwindow()
            self.w.show()

        else:
            self.w = None



class secondwindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setGeometry(50, 50, 200, 50)


if __name__ == '__main__':
    app = QApplication([])
    w = mainwindow()
    sys.exit(app.exec())
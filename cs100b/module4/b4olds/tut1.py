#pyqt tutorial 1 - signals and slots, pt 1 (button.clicked/button_clicked)

from PyQt6.QtWidgets import *

#i really don't get this *args, **kwargs thing
#like, it makes the app work, somehow?
#well, it seems that it literally wasn't working because i put a comment between class and def init
#...
class mainwindow (QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)

        self.setWindowTitle("Qt Signals & Slots")

        layout = QVBoxLayout()
        self.setLayout(layout)

        button = QPushButton("Push Me")
        button.clicked.connect(self.button_clicko)
        layout.addWidget(button)

        self.show()

    def button_clicko(self):
        print('clicked')

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    #so the other big difference was using sys for exec
    app.exec()

if __name__ == '__main__':
    main()

    

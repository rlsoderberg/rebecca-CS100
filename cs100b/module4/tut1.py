from PyQt6.QtWidgets import *

class mainwindow (QWidget):
    #i really don't get this *args, **kwargs thing
    #like, it makes the app work, somehow?
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Qt Signals & Slots")

        button = QPushButton("Push Me")
        button.clicked.connect(self.button_clicko)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)

        self.show()

    def button_clicko(self):
        print('clicked')

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()

    

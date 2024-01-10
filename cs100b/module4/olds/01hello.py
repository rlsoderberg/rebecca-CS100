#interact with system to open new window
import sys
#import gui library pyqt
from PyQt6.QtWidgets import *

class mainwindow (QWidget):
    def __init__(self, parent = None):
        #super calls parent class (QWidget)
        super(mainwindow, self).__init__(parent)
        #sets window size
        self.setGeometry(100,100,300,50)
        #sets title bar text
        self.setWindowTitle("PyQt6")

        #sets text label
        b = QLabel(self)
        b.setText("Hello World!")

        b = QLabel(self)
        b.setText("\t\t\tHello World!")

        self.show()

def main():
    app = QApplication([])
    #creates object of main window class
    w = mainwindow()
    w.show()
    
    #keeps app open until all code is executed?
    sys.exit(app.exec())

#you can import mainwindow class from wherever, but main only runs if you are running this file directly
if __name__ =='__main__':
    main()
        

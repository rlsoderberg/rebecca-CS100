import sys
from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    #ok, so... we're doing __init__ twice...
    def __init__(self, parent = None):
        #oh, so we're just initializing the parent, within the window, makes sense
        super(mainwindow, self).__init__(parent)
        #set the window size and location
        self.setGeometry(100, 100, 200, 50)
        #set window title
        self.setWindowTitle('PyQt6.1')

        #well... here's a bunch of stuff to toggle windows
        #oh wait!!! self.w is None because there's no external window yet!!! that kind of makes sense...
        #i still don't ENTIRELY get how this works, along with show_new_window
        self.w = None  # No external window yet.
        #the example i was looking at on...pythonguis.com... hey, is that even a reputable website???
        #it wanted me to do like, 'self.setCentralWidget(self.button)'
        p = QPushButton(
            text="push this button",
            parent=self
        )
        p.clicked.connect(self.show_new_window)
        #oh, um, i got help on pushbutton from the same website
        #anyway, the second window is working fine



    def show_new_window(self, checked):
        if self.w is None:
            self.w = secondwindow()
            self.w.show()

        else:
            self.w = None

        b = QLabel(self)
        # announce our presence with authority
        b.setText('push to toggle window')

#i'm going to try making a second window
#i don't know how to show multiple windows simultaneously...
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

def main():
    #we are making a QApplication???
    #i guess, looking at it again, i don't ENTIRELY understand all these new keywords
    #i was googling about a little and i saw someone say this:
    #QApplication starts a loop, which executes code related to every instance of QWidget
    #like, i don't know how true that is, but it sounds pretty cool!
    #and don't forget to put brackets in your parentheses!!!
    app = QApplication([])

    #i was googling about all these different built-in class attributes
    #i found that i can print the dict and it prints a bunch of stuff!
    #but only if you print before running the app
    print(mainwindow.__dict__)
    # create and show our window
    w = mainwindow()
    w.show()
    #when the user exits, close the app
    sys.exit(app.exec())


    

if __name__ == '__main__':
    main()

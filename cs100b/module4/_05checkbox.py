from PyQt6.QtWidgets import *
#the tutorial says i'm supposed to import these things but i'm not sure why
#ok, sys is for exit
import sys
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    #define init function and then...
    #so the argument at the end is what you're trying to inherit from parent
    #by the way, apparently you can also use super to create a proxy object, whatever that means
    #but anyway... this first argument...
    #well... apparently it kind of refers to the child window?
    #i guess it is what it is, although i DO wish i could be asking potentially irrelevant questions right now...

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('PyQt Checkbox')
        self.setGeometry(100, 100, 200, 50)

        #create grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        #create a checkbox
        checkbox = QCheckBox('I Agree', self)
        #so, apparently i need Qt for.. alignment flags? what even?
        #oh, i wonder if qt could help with screen dimensions

        #this is the state changed signal!!!
        checkbox.stateChanged.connect(self.on_checkbox_changed)
        #oh i get it, it connects to a function!!!
        #and it... automatically passes checkbox state to the function?
        layout.addWidget(checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)
        
        #this is the second part of the statechanged signal
        #the tutorial had an argument of value, which i don't see how that works here!!!
        #state = Qt.CheckState()
        #oh wait, i'm supposed to put it in its own function, with an argument of value!!!

        #show the window
        self.show()

    def on_checkbox_changed(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            print('Checked')
        elif state == Qt.CheckState.Unchecked:
            print("Unchecked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
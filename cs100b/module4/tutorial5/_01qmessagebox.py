import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('QMessageBox')
        self.setGeometry(100, 100, 300, 100)

        layout = QHBoxLayout()
        self.setLayout(layout)

        btn_question = QPushButton('Question')
        btn_question.clicked.connect(self.question)

        btn_info = QPushButton('Information')
        btn_info.clicked.connect(self.info)

        btn_warning = QPushButton('Warning')
        btn_warning.clicked.connect(self.warning)

        btn_critical = QPushButton('Critical')
        btn_critical.clicked.connect(self.critical)

        layout.addWidget(btn_question)
        layout.addWidget(btn_info)
        layout.addWidget(btn_warning)
        layout.addWidget(btn_critical)

        self.show()


    def info(self):
        QMessageBox.information(
            self,
            'Information',
            'Insufficient facts always invite danger.'
        )
    
    def warning(self):
        QMessageBox.warning(
            self,
            'Warning',
            'You would die before your stroke fell.'
        )

    def critical(self):
        QMessageBox.critical(
            self,
            'Critical',
            'Core overload. Emergency shutdown overridden.'
        )
        
    #hahaha, abstract buttons man
    #no actually, i'm still not sure how to put custom text on buttons
    #i'm just not entirely sure how to read these reference materials on pyqt6???
            
    def question(self):
        answer = QMessageBox.question(
            self, 
            'Confirmation',
            'What is love?',
            QMessageBox.StandardButton.Yes | 
            QMessageBox.StandardButton.No
        )
        
        if answer == QMessageBox.StandardButton.Yes:
            QMessageBox.information(
                self,
                'Information',
                'WhOoOoOoOoah',
                QMessageBox.StandardButton.Ok
            )
            self.close()

        elif answer == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self,
                'Information',
                'Wooo',
                QMessageBox.StandardButton.Ok
            )
            self.close()

if __name__ == '__main__':
    app = QApplication([])
    w = MainWindow()
    sys.exit(app.exec())

#i still need to learn about... Qt & alignment flags for screen dimensions? creating new screens? 
#i'm skipping input dialog & file dialog!!! this is the only thing happening today!!!
#and i'd still like to customize button text...

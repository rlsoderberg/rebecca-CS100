import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

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
        QMessageBox.information(
            self,
            'Warning',
            'You would die before your stroke fell.'
        )

    def critical(self):
        QMessageBox.information(
            self,
            'Critical',
            'Core overload. Emergency shutdown overridden.'
        )
    #hahaha, abstract buttons man
    #no actually, i'm still not sure how to put custom text on buttons
    #but at least it's kind of working? for some reason?
    def question(self):
        answer = QMessageBox.question(
            self, 
            'Confirmation',
            'What is love?',
        )

#
       # answer.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        #buttonX = answer.StandardButton(QtGui.QMessageBox.Yes)
      #  buttonX.setText("Don't Hurt Me")
       # buttonY = answer.StandardButton(QtGui.QMessageBox.No)
        #buttonY.setText('No More')



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
                'Ooh',
                QMessageBox.StandardButton.Ok
            )
            self.close()

if __name__ == '__main__':
    app = QApplication([])
    w = MainWindow()
    sys.exit(app.exec())

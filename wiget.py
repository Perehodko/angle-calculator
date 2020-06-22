from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit
from myGUI import Ui_Form
import sys

class mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Test"
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 500
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)

        # Create checkbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 100)

        # create button
        self.button = QPushButton('Run', self)
        self.button.move(300, 99)

        self.button.clicked.connect(self.onButtonClicked)
        self.show()

    def onButtonClicked(self):
        storeString = self.textbox.text()
        print(storeString)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()



sys.exit(app.exec())

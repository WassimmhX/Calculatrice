import sys
from exec import Exec
from PyQt5 import QtWidgets
class Main:
    def __init__(self):
        self.window=Exec()
app=QtWidgets.QApplication(sys.argv)
window=Main()
app.exec_()
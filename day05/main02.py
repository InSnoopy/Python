import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

form_class = uic.loadUiType("./main02.ui")[0]

class MyWindow(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        num = int(self.le.text())
        num1 = num * 2
        self.le.setText(str(num1))

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
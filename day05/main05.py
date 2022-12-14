import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

form_class = uic.loadUiType("./main05.ui")[0]

class MyWindow(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
 
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        a = self.le1.text()
        a = int(a)
        
        b = self.leb.text()
        b = int(b)
        
        c = a*b

        self.lec.setText(str(c))

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

form_class = uic.loadUiType("./main01.ui")[0]

class MyWindow(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
 
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function

    def myclick(self):
        self.lbl.setText("GoodEvening")

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 
import random

form_class = uic.loadUiType("./main04.ui")[0]

class MyWindow(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        mine = self.leMine.text()
        rnd = random.random()
        com = ""
        result = ""
        
        if(rnd>0.5):
            com = "홀"
        else:
            com = "짝"

        if(com == mine):
            result = "사용자 승리"
        else:
            result = "컴퓨터 승리"
        
        self.leCom.setText(com)
        self.leResult.setText(result)
    
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
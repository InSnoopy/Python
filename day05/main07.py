import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 
from random import random

form_class = uic.loadUiType("./main07.ui")[0]

arr3 = ["가위","바위","보"]

class MyWindow(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myclick)

    def myclick(self):
        user = self.leMine.text()
        rnd = int(random()*3)
        computer = arr3[rnd]
        result = ""
        
        if computer == "가위" and user == "가위" : result = "비김"
        if computer == "바위" and user == "바위" : result = "비김"
        if computer == "보" and user == "보" : result = "비김"
        
        if computer == "바위" and user == "가위" : result = "짐"
        if computer == "바위" and user == "바위" : result = "비김"
        if computer == "바위" and user == "보" : result = "이김"
        
        if computer == "보" and user == "가위" : result = "이김"
        if computer == "보" and user == "바위" : result = "짐"
        if computer == "보" and user == "보" : result = "비김"

        self.leCom.setText(computer)
        self.leResult.setText(result)

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
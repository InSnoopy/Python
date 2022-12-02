import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 
import random

form_class = uic.loadUiType("./mainX.ui")[0]

com = ""

class MyWindow(QMainWindow, form_class):
         

    def __init__(self): 
        super().__init__() 
        self.setupUi(self)            

        self.comRanNum()
        self.pb.clicked.connect(self.myclick) 

    def myclick(self):
        
        user = self.le.text()      
        strike = self.getStrike(user)
        ball = self.getBall(user)
        
        print(user)
        print(strike)
        print(ball)
        
        str_old = self.te.toPlainText()
        str_new = str(strike)+"S"+str(ball)+"B\n"
        print(strike)
        print(str_old)
        print(str_new)
        
        self.te.setPlainText(str_old+str_new)
        self.le.setText("")
        
        if(self.getStrike(user)==3):
            print("맞췄습니다.")


    def getStrike(self,user):

        userNum1 = user[0:1];
        userNum2 = user[1:2];
        userNum3 = user[2:3];
        
        comNum1 = com[0:1];
        comNum2 = com[1:2];
        comNum3 = com[2:3];
        
        strike = 0
        if userNum1 == comNum1:
            strike += 1
        if userNum2 == comNum2:
            strike += 1
        if userNum3 == comNum3:
            strike += 1
        
        return strike
    
    
    def getBall(self,user):

        userNum1 = user[0:1];
        userNum2 = user[1:2];
        userNum3 = user[2:3];
        
        comNum1 = com[0:1];
        comNum2 = com[1:2];
        comNum3 = com[2:3];
        
        ball = 0
        if userNum1 == comNum2 or userNum1 == comNum3:
            ball += 1
        if userNum2 == comNum1 or userNum2 == comNum3:
            ball += 1
        if userNum3 == comNum1 or userNum3 == comNum2:
            ball += 1
        
        return ball

    def comRanNum(self):
        for i in range(3):
            x = (int)(random.random()*9)
            com = com + str(x)

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
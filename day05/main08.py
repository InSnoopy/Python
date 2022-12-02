import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

form_class = uic.loadUiType("./main08.ui")[0]

class MyWindow(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        starS = self.lbl_s.text()
        starSS = int(starS)
        starL = self.lbl_l.text()
        starLL = int(starL)
        total = ""

        for i in range(starSS, starLL+1):
            print(i)
            total += self.drawStar(i)
  
        self.pte.setPlainText(total)
    
    def drawStar(self,cnt):
        star = ""
        for i in range(cnt):
            star += "*";
        star += "\n";
        return star

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

form_class = uic.loadUiType("./main06.ui")[0]

class MyWindow(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
 
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        dan = self.le.text()
        dan = int(dan)
        
        txt = ""
        
        txt += str(dan)+"*"+str(1)+"="+str((dan*1))+"\n"
        txt += str(dan)+"*"+str(2)+"="+str((dan*2))+"\n"
        txt += str(dan)+"*"+str(3)+"="+str((dan*3))+"\n"
        txt += str(dan)+"*"+str(4)+"="+str((dan*4))+"\n"
        txt += str(dan)+"*"+str(5)+"="+str((dan*5))+"\n"
        txt += str(dan)+"*"+str(6)+"="+str((dan*6))+"\n"
        txt += str(dan)+"*"+str(7)+"="+str((dan*7))+"\n"
        txt += str(dan)+"*"+str(8)+"="+str((dan*8))+"\n"
        txt += str(dan)+"*"+str(9)+"="+str((dan*9))+"\n"

        self.te.setText(txt)

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

form_class = uic.loadUiType("./main09.ui")[0]

class MyWindow(QMainWindow, form_class):
         
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        
    
        self.pb1.clicked.connect(lambda temp="",name="1":self.myClick2(name))
        self.pb1.clicked.connect(self.myclick) 
        self.pb2.clicked.connect(self.myclick) 
        self.pb3.clicked.connect(self.myclick) 
        self.pb4.clicked.connect(self.myclick) 
        self.pb5.clicked.connect(self.myclick) 
        self.pb6.clicked.connect(self.myclick) 
        self.pb7.clicked.connect(self.myclick) 
        self.pb8.clicked.connect(self.myclick) 
        self.pb9.clicked.connect(self.myclick) 
        self.pb0.clicked.connect(self.myclick) 
        
        self.pbCall.clicked.connect(self.mycall) 
       
    def mycall(self):   
        print("mycall")
        str_num = self.le.text()
        QMessageBox.about(self,'Calling',str_num)
        
    def myClick2(self, num):
        print("hi")
        print(num)
        # print(self.sender().text())
        
    def myclick(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        self.le.setText(str_old+str_new)
        
        print(self.sender().text())
    


if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
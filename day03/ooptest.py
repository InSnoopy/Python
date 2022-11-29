class Animal:
    def __init__(self):
        print("생성자")
        self.age = 0
 
    def getOlder(self):
        self.age += 1
        
    def __del__(self):
        print("소멸자")
        
class Humain(Animal):
    def __init__(self):
        super().__init__()
        self.language = 0
        
    def momstouch(self, stroke):
        self.language += stroke;
            
 
if __name__ == '__main__':
    
    human = Humain()
    print(human.age)
    print(human.language)
    human.getOlder()
    human.momstouch(5)
    print(human.age)
    print(human.language)
    


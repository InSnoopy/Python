# 로또를 생성하시오 (1~45 숫자중에서 중복없이 6개 가져오기)
from random import random

numberBox = []

for i in range(1,45+1):
    numberBox.append(i)

print(numberBox)


for i in range(100):
        
    rnd = int(random()*45)
    
    a = numberBox[0]
    b = numberBox[rnd]
    numberBox[0]=b
    numberBox[rnd]=a
    
for i in range(6):
    print(numberBox[i])
    
# 로또를 생성하시오 (1~45 숫자중에서 중복없이 6개 가져오기)
from random import random
#
#
# arr = range(0,6)
# rndNum = []
#
# for i in arr:
#     rnd = random.randint(1,45)
#     print(rndNum.append(rnd))
#
#     print(rndNum[i])


arr6 = [1,2,3,4,5,6]

for i in range(100):
        
    rnd = int(random()*6) 
    
    a = arr6[0]
    b = arr6[rnd]
    arr6[0]=b
    arr6[rnd]=a

print(arr6[0],arr6[1],arr6[2])
    
# 홀/짝을 넣으세요 홀
# 사용자:홀
# 컴퓨터:짝
# 결과: 컴퓨터 승리
import random

arr = ["홀","짝"]

rnd = random.randint(0,1)

user = input("홀/짝을 넣으세요")

computer = arr[rnd]
print(computer)

if user==computer:
    print("결과: 사용자 승리")
else:
    print("결과: 컴퓨터 승리")

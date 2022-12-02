# 가위/바위/보 넣으세요 가위
# 사용자:가위
# 컴퓨터:가위
# 결과: 비김
from random import random

arr3 = ["가위","바위","보"]
rnd = int(random()*3)
user = ""
computer = ""
result = ""

user = input("가위/바위/보 넣으세요 : ")
computer = arr3[rnd]

# 이렇게 직관적으로 쓰는게 좋다.
if computer == "가위" and user == "가위" : result = "비김"
if computer == "바위" and user == "바위" : result = "비김"
if computer == "보" and user == "보" : result = "비김"

if computer == "바위" and user == "가위" : result = "짐"
if computer == "바위" and user == "바위" : result = "비김"
if computer == "바위" and user == "보" : result = "이김"

if computer == "보" and user == "가위" : result = "이김"
if computer == "보" and user == "바위" : result = "짐"
if computer == "보" and user == "보" : result = "비김"
    
print("사용자 : {}".format(user))
print("컴퓨터 : {}".format(computer))
print("결과  : {}".format(result))

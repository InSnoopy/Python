# 첫번째 수를 넣으세요 1
# 두번째 수를 넣으세요 10
# 1에서 10까지 합은 55입니다.

a = input("첫번째 수를 넣으세요.")
b = input("두번째 수를 넣으세요.")

c = range(int(a),int(b)+1)

total = 0

for i in c:
    total += i

print("{}에서 {}까지 합은 {}입니다.".format(a,b,total))

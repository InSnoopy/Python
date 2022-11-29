# 첫번째 숫자를 넣으세요 1
# 두번째 숫자를 넣으세요 2
# 숫자의 합은 3입니다.

a = input("첫번째 숫자를 넣으세요")
b = input("두번째 숫자를 넣으세요")
sum = int(a)+int(b) # input으로 받은 값은 str

# print("숫자의 합은 " +str(sum)+ "입니다") # str + int = error
# print("숫자의 합은 ",str(sum),"입니다")
print("숫자의 합은 {}입니다.".format(sum)) # sum은 int인데 자동으로 형변환 한다.


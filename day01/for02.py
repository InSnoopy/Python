# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = range(10)
# arr = range(0,10)
arr = range(1,11)

print(arr) # range(1, 10)
print(list(arr)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0
for i in arr:
    total += i

print(total) # 55
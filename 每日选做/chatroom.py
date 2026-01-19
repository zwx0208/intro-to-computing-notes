s = input().strip()
target = "hello"
index = 0
for char in s:
    if index < len(target) and char == target[index]:
        index += 1
if index == len(target):
    print("YES")
else:
    print("NO")

#在 Python 中，and 操作符是短路求值的，会先计算左边的条件，如果左边为 False 就不会再计算右边。所以，要注意and前和后的条件顺序
#此题更好地理解了怎样使用指针，以及他并不算贪心题
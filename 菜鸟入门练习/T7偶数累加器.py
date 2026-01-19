# 要求：计算1-100中所有偶数的和
# 输出：2550
a=0
for i in range(101):
    if i%2==0:
        a+=i
print(a)
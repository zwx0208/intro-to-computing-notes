# 要求：打印完整九九乘法表
# 格式：
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
for j in range(1,10):
    for i in range(1,10):
        if i<j:
            print(f'{i}*{j}={i*j} ',end='')
        elif i==j:
            print(f'{i}*{j}={i*j}')
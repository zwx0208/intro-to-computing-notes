#🏆例1：读取多行数字，遇到 0 结束，对每个数输出它的平方
#🌟法1 while True + break （适用于有明确终止标记）
while True:
    n = int(input())
    if n==0:   #终止标志用if判断
        break
    print(n**2)
#🌟法2 sys.stdin.read() （一次性读取所有数据）
import sys
data = sys.stdin.read().strip().split()  #一次读取所有输入并转换为字符串列表
for s in data:
    n = int(s)  #注意这时的n是字符串形式！
    print(n * n)
    if n == 0:
        break
#🏆例2：读取多行数字，对每个数输出它的平方，直到输入结束
#🌟法3 try-except EOFError （输入流结束时结束）
try:
    while True:
        n = int(input())
        print(n * n)
except EOFError:  #这一行没有输入时
    pass
#🏆例3：
# 输入：Alice,25,90
#      Bob,30,85
#      Charlie,22,95
#🌟法4：for line in sys.stdin（逐行迭代，适合结构化数据）
import sys
for line in sys.stdin:
    name,age,score=line.strip().split(',')  #每行的结构都是固定的，只用处理一行即可
    print(f"{name}:年龄{age}岁,分数{score}分")

import sys
    # 输入矩阵：
    # n m
    # a11 a12 ... a1m
    # ...
    # an1 an2 ... anm
data = sys.stdin.read().strip().split()
n, m = map(int, data[:2])
matrix = []
idx = 2
for _ in range(n):
    row = list(map(int, data[idx:idx + m]))
    matrix.append(row)
    idx += m
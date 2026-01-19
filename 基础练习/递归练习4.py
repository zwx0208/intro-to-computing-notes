# 要求：用递归计算 a 的 b 次方 (a^b)
# 不能使用 ** 运算符或循环
# 示例：
# 输入：(2, 3) → 输出：8
# 输入：(5, 0) → 输出：1

def power(a, b):
    if b==0:
        return 1
    elif a==0:
        return 0
    return a*power(a,b-1)
print(power(2, 3))
print(power(5, 0))
print(power(3, 4))  
# 要求：用递归计算一个数字的各位数字乘积
# 示例：
# 输入：1234 → 输出：1*2*3*4 = 24
# 输入：305 → 输出：3*0*5 = 0
# 输入：7 → 输出：7

def digit_product(n):
    if n<10:
        return n
    else:
        return n%10*digit_product(n // 10)


print(digit_product(1234))
print(digit_product(305))
print(digit_product(7))
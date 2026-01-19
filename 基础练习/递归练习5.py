# 要求：用更少的递归步骤计算 a^b
# 利用公式：a^b = (a^(b//2))² × a^(b%2)
# 示例：
# 输入：(2, 10) → 输出：1024（只用5步而不是10步！）

def fast_power(a, b):
    if b==0:
        return 1
    elif b%2==0:
        return (fast_power(a,b//2))**2
    else:
        return (fast_power(a,b//2))**2*a


print(fast_power(2, 10))
print(fast_power(3, 5))   
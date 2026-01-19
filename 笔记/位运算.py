#1）检查第 k 位（从右数，最低位为第 0 位）
def get_bit(n, k):
    return (n >> k) & 1

#2）设置第 k 位为 1
def set_bit(n, k):
    return n | (1 << k)

#3）设置第 k 位为 0
def clear_bit(n, k):
    return n & ~(1 << k)

#4）切换第 k 位（1变0，0变1）
def toggle_bit(n, k):
    return n ^ (1 << k)

#5）获取最低位的 1 的位置（lowbit）
lowbit = n & -n

#输出0~2**n-1, 1<<n相当于2**n
for i in range(1<<n):
    print(i)
from collections import deque

# 1. 创建
dq = deque()                    # 空deque
dq = deque([1, 2, 3])           # 从列表创建
dq = deque("hello")             # 从字符串创建

# 2. 添加元素
dq.append(4)                    # 右端添加 → deque([1,2,3,4])
dq.appendleft(0)                # 左端添加 → deque([0,1,2,3,4])
dq.extend([5, 6])               # 右端扩展 → deque([0,1,2,3,4,5,6])
dq.extendleft([-1, -2])         # 左端扩展 → deque([-2,-1,0,1,2,3,4,5,6])
# 注意：extendleft是逆序添加！

# 3. 删除元素
x = dq.pop()                    # 右端删除，返回6
y = dq.popleft()                # 左端删除，返回-2
# deque([-1,0,1,2,3,4,5])

# 4. 其他操作
dq.rotate(2)                    # 向右旋转2位 → deque([4,5,-1,0,1,2,3])
dq.rotate(-1)                   # 向左旋转1位 → deque([5,-1,0,1,2,3,4])
len(dq)                         # 长度
dq.clear()                      # 清空

dq = deque(maxlen=3)            # 固定长度deque
for i in range(5):
    dq.append(i)
    print(f"添加{i}: {dq}")

# 输出：
# 添加0: deque([0], maxlen=3)
# 添加1: deque([0, 1], maxlen=3)
# 添加2: deque([0, 1, 2], maxlen=3)
# 添加3: deque([1, 2, 3], maxlen=3)  # 自动挤出第一个
# 添加4: deque([2, 3, 4], maxlen=3)  # 自动挤出第二个
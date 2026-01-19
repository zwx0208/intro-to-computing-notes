# 读取输入
lights = []
for _ in range(5):
    lights.append(list(map(int, input().split())))

rows, cols = 5, 6


# 按下 (i,j) 按钮，改变周围灯状态
def press_switch(state, i, j):
    for di, dj in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            state[ni][nj] ^= 1  # 0变1，1变0


# 枚举第一行的所有按法
found = False
for mask in range(1 << cols):  # 0~63
    # 初始化状态和按法记录
    state = [row[:] for row in lights]
    solution = [[0] * cols for _ in range(rows)]

    # 设置第一行的按法
    for j in range(cols):
        if (mask >> (cols - 1 - j)) & 1:  # 从左到右，高位对应左列
            solution[0][j] = 1
            press_switch(state, 0, j)

    # 递推1~4行
    for i in range(rows - 1):
        for j in range(cols):
            if state[i][j] == 1:
                solution[i + 1][j] = 1
                press_switch(state, i + 1, j)

    # 检查最后一行是否全灭
    if all(state[rows - 1][j] == 0 for j in range(cols)):
        found = True
        break

# 输出结果
if found:
    for row in solution:
        print(' '.join(str(x) for x in row))
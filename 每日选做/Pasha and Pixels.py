n, m, k = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

def find(matrix, a, b, n, m):
    if a >= 1 and b >= 1:
        if matrix[a-1][b-1] == 1 and matrix[a-1][b] == 1 and matrix[a][b-1] == 1 and matrix[a][b] == 1:
            return True
    if a >= 1 and b < m-1:
        if matrix[a-1][b] == 1 and matrix[a-1][b+1] == 1 and matrix[a][b] == 1 and matrix[a][b+1] == 1:
            return True
    if a < n-1 and b >= 1:
        if matrix[a][b-1] == 1 and matrix[a][b] == 1 and matrix[a+1][b-1] == 1 and matrix[a+1][b] == 1:
            return True
    if a < n-1 and b < m-1:
        if matrix[a][b] == 1 and matrix[a][b+1] == 1 and matrix[a+1][b] == 1 and matrix[a+1][b+1] == 1:
            return True
    return False

for x in range(k):
    a, b = map(int, input().split())
    i, j = a-1, b-1
    matrix[i][j] = 1
    if x >= 3:
        if find(matrix, i, j, n, m):
            print(x+1)
            exit(0)  # 直接退出程序，避免后续输入
print(0)






#更简洁的方法(储存方向！)
n, m, k = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
for move in range(1, k + 1):
    a, b = map(int, input().split())
    i, j = a - 1, b - 1
    matrix[i][j] = 1

    # 检查四个可能的2x2区域
    for di in [-1, 0]:
        for dj in [-1, 0]:
            ni, nj = i + di, j + dj
            # 确保2x2区域在边界内
            if 0 <= ni < n - 1 and 0 <= nj < m - 1:
                # 检查2x2区域是否全黑
                if (matrix[ni][nj] == 1 and
                        matrix[ni][nj + 1] == 1 and
                        matrix[ni + 1][nj] == 1 and
                        matrix[ni + 1][nj + 1] == 1):
                    print(move)
                    exit()
print(0)
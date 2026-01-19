n = int(input())
size = 2 * n - 1
matrix = [[0] * size for _ in range(size)]
i,j= 0, n - 1

for num in range(1, size * size + 1):
    matrix[i][j] = num
    ni= (i - 1) % size
    nj= (j + 1) % size
    if matrix[ni][nj] != 0 or (i== 0 and j == size - 1):
        i = (i + 1) % size
    else:
        i,j= ni, nj
for row in matrix:
    print(*row)
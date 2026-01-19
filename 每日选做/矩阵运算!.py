def main():
    matrices = []
    # 读取三个矩阵
    for _ in range(3):
        try:
            r, c = map(int,input().split())
            mat = []
            for i in range(r):
                mat.append(list(map(int,input().split())))

            matrices.append(mat)
        except:
            return
    A, B, C = matrices
#判断AB
    if len(A[0]) != len(B):
        print("Error!")
        return
#判断AB和C
    AB_rows, AB_cols = len(A), len(B[0])
    if AB_rows != len(C) or AB_cols != len(C[0]):
        print("Error!")
        return

# 计算 A × B
    AB = [[0] * AB_cols for _ in range(AB_rows)]
    for i in range(AB_rows):
        for j in range(AB_cols):
            for k in range(len(B)):
                AB[i][j] += A[i][k] * B[k][j]  #核心公式

# 计算 (A×B) + C 并输出
    for i in range(AB_rows):
        row = [AB[i][j] + C[i][j] for j in range(AB_cols)]
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
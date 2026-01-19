m,n=map(int,input().split())
matrix=[]
for i in range(m):
        matrix.append(list(map(int,input().split())))
if m == 1 and n == 1:
    print(matrix[0][0])
elif m == 1:
    print(sum(matrix[0]))
elif n == 1:
    print(sum(row[0] for row in matrix))
else:
    summary=sum(matrix[0]+matrix[m-1])
    for i in range(1,m-1):
        summary+=matrix[i][0]
        summary+=matrix[i][n-1]
    print(summary)
#矩阵一定要注意只有一个元素或一列、一行的情况


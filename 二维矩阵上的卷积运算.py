m,n,p,q=map(int,input().split())
matrix1=[]
matrix2=[]
for _ in range(m):
    matrix1.append(list(map(int,input().split())))
for _ in range(p):
    matrix2.append(list(map(int,input().split())))
def ji(i,j,matrix1,matrix2,p,q):
    count=0
    for a in range(p):
        for b in range(q):
            count+=matrix2[a][b]*matrix1[i+a][j+b]
    return count
for i in range(m+1-p):
    row=[]
    for j in range(n+1-q):
        row.append(ji(i,j,matrix1,matrix2,p,q))
    print(*row)


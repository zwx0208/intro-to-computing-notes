n,m=map(int,input().split())
bridges=[]
count=[0]*n
d=[[0]*n for _ in range(n)]
A=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    count[a]+=1
    count[b]+=1
    A[a][b]=1
    A[b][a]=1
for i in range(n):
    d[i][i]=count[i]
l=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        l[i][j]=d[i][j]-A[i][j]
for item in l:
    print(*item)


n, m = map(int, input().split())
# 初始化拉普拉斯矩阵 L（全0）
L = [[0] * n for _ in range(n)]
# 统计度数并构建邻接关系
for _ in range(m):
    a, b = map(int, input().split())
    # 更新度数（对角线元素）
    L[a][a] += 1
    L[b][b] += 1
    # 设置邻接关系为 -1
    L[a][b] = -1
    L[b][a] = -1
for row in L:
    print(*row)
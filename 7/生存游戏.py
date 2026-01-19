def check(mtrx,x,y):
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]
    count=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        count+=mtrx[nx][ny]
    if mtrx[x][y]==0 and count==3:
        return 1
    elif mtrx[x][y] and (count<2 or count>3):
        return 0
    return mtrx[x][y]
n,m=map(int,input().split())
mtrx=[]
mtrx.append([0]*(m+2))
for _ in range(n):
    mtrx.append([0]+list(map(int,input().split()))+[0])
mtrx.append([0]*(m+2))
Cell=[[0]*m for y in range(n)]
for i in range(n):
    for j in range(m):
        Cell[i][j]=check(mtrx,i+1,j+1)
for row in Cell:
    print(*row)




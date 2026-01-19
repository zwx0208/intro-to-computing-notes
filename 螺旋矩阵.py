n=int(input())
directions=[[0,1],[1,0],[0,-1],[-1,0]]
idx=0
matrix=[[0]*n for _ in range(n)]
x,y=0,0
for i in range(1,n**2+1):
    matrix[x][y]=i
    nx=x+directions[idx][0]
    ny=y+directions[idx][1]
    if nx<0 or nx>=n or ny<0 or ny>=n or matrix[nx][ny]!=0:
        idx=(idx+1)%4
        nx = x + directions[idx][0]
        ny = y + directions[idx][1]
    x=nx
    y=ny
for row in matrix:
    print(*row)



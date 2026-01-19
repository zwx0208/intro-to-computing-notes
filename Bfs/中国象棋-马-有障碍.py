from collections import deque
n,m,x,y=map(int,input().split())
k=int(input())
block=[]
for _ in range(k):
    i,j=map(int,input().split())
    block.append((i-1,j-1))
board=[[-1]*m for _ in range(n)]
x,y=x-1,y-1
queue=deque()
board[x][y]=0
queue.append((x,y))
while queue:
    x,y=queue.popleft()
    directions=[[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-2,1],[-1,-2],[-2,-1]]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==-1 and (nx,ny) not in block:
            if dx in (2,-2):
                mx,my=x+dx//2,y
            else:
                mx,my=x,y+dy//2
            if (mx,my) not in block:
                queue.append((nx,ny))
                board[nx][ny]=board[x][y]+1
for col in board:
    print(*col)
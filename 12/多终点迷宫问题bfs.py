from collections import deque
n,m=map(int,input().split())
puzzle=[]
for _ in range(n):
    puzzle.append(list(map(int,input().split())))
queue=deque()
queue.append((0,0))
count=[[-1]*m for _ in range(n)]
count[0][0]=0
directions=[(0,1),(0,-1),(1,0),(-1,0)]
while queue:
    x,y=queue.popleft()
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and puzzle[nx][ny]==0 and count[nx][ny]==-1:
            count[nx][ny]=count[x][y]+1
            queue.append((nx,ny))
for i in range(n):
    output=' '.join(str(count[i][j]) for j in range(m))
    print(output)
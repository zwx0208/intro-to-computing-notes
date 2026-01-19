from collections import deque
n,m=map(int,input().split())
puzzle=[]
for _ in range(n):
    puzzle.append(list(map(int,input().split())))
queue=deque()
queue.append((0,0))
prev_point=[[None]*m for _ in range(n)]
prev_point[0][0]=(-1,-1)
directions=[(0,1),(0,-1),(1,0),(-1,0)]
while queue:
    x,y=queue.popleft()
    if x==n-1 and y==m-1:
        break
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and puzzle[nx][ny]==0 and prev_point[nx][ny]==None:
            prev_point[nx][ny]=(x,y)
            queue.append((nx,ny))
back=[]
x,y=n-1,m-1
while (x,y)!=(-1,-1):
    back.append((x,y))
    x,y=prev_point[x][y]
back.reverse()
for (x,y) in back:
    print(x+1,y+1)
from collections import deque
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
count=0
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            count+=1
            queue=deque()
            queue.append((i,j))
            grid[i][j]=0
            while queue:
                x,y=queue.popleft()
                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                        queue.append((nx,ny))
                        grid[nx][ny]=0
print(count)
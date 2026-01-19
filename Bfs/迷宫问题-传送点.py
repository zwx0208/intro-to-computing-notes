from collections import deque
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
trans=[]
for i in range(n):
    for j in range(m):
        if grid[i][j]==2:
            trans.append(i);trans.append(j)
def bfs():
    queue=deque()
    queue.append((0,0,0))   # x,y,step(bfs转移的时候要带步数)
    grid[0][0]=1
    while queue:
        x,y,count=queue.popleft()
        if x == n - 1 and y == m - 1:
            return count
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0:
                grid[nx][ny]=1
                queue.append((nx,ny,count+1))
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 2:
                grid[nx][ny]=1
                queue.append((trans[0],trans[1],count+1))
                queue.append((trans[2], trans[3], count + 1))

    return -1
print(bfs())

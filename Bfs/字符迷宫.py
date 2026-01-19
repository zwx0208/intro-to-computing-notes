from collections import deque
n,m=map(int,input().split())
grid=[list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j]=='S':
            xs,ys=i,j
        if grid[i][j]=='T':
            xt,yt=i,j
def bfs():
    queue=deque()
    queue.append((xs,ys,0))   # x,y,step(bfs转移的时候要带步数)
    visited[xs][ys]=True
    while queue:
        x,y,count=queue.popleft()
        if x==xt and y==yt:
            return count
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]!='*' and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny,count+1))
    return -1
print(bfs())
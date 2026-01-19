from collections import deque
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
def bfs():
    queue=deque()
    queue.append((0,0,0))   # x,y,count(bfs转移的时候要带步数)
    visited[0][0] = True
    while queue:
        x,y,count=queue.popleft()
        if x == n - 1 and y == m - 1:
            return count
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,count+1))
        d=[[0,2],[0,-2],[2,0],[-2,0]]
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0 and not visited[nx][ny]:
                mx,my=x+dx//2,y+dy//2
                if grid[mx][my]==0:
                    visited[nx][ny] = True
                    queue.append((nx,ny,count+1))
    return -1
print(bfs())
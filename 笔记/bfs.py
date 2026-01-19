#模板 1：带步数记录（最常用）
from collections import deque

def bfs(grid, start, target):
    if grid[start[0]][start[1]] == 障碍:  # 起点检查
        return -1

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    queue.append((start[0], start[1], 0))  # (x, y, 步数)
    visited = set()
    visited.add((start[0], start[1]))  # 或直接修改原grid

    while queue:
        x, y, steps = queue.popleft()

        # 到达目标
        if (x, y) == target:
            return steps

        # 四个方向/八个方向
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 边界检查 + 可通行 + 未访问
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 可通行 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

    return -1  # 无法到达

#例：字符迷宫(规定起点终点)
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

#马走日，有障碍（多终点，有障碍排除）
from collections import deque
n,m,x,y=map(int,input().split())
k=int(input())
block=[]
for _ in range(k):
    i,j=map(int,input().split())
    block.append((i-1,j-1))
board=[[-1]*m for _ in range(n)]  #多终点要设置列表记录，初始设置为无法达到
x,y=x-1,y-1
queue=deque()
board[x][y]=0
queue.append((x,y))
while queue:
    x,y=queue.popleft()
    directions=[[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-2,1],[-1,-2],[-2,-1]]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==-1 and (nx,ny) not in block:   #一定要检查该点是否有记录，否则会死循环
            if dx in (2,-2):
                mx,my=x+dx//2,y
            else:
                mx,my=x,y+dy//2
            if (mx,my) not in block:
                queue.append((nx,ny))
                board[nx][ny]=board[x][y]+1
for col in board:
    print(*col)
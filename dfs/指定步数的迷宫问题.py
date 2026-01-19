n,m,k=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
directions=[[0,1],[0,-1],[1,0],[-1,0]]
def dfs(x,y,step):    #当前位置，步数
    if step>k:  #剪枝
        return False
    if x==n-1 and y==m-1:
        return step==k
    visited[x][y]=True
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and grid[nx][ny]!=1 and not visited[nx][ny]:
            if dfs(nx,ny,step+1):
                return True     #要接收nx,ny的结果
    visited[x][y]=False
    return False
print('Yes' if dfs(0,0,0) else 'No')
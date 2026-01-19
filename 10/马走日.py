def horse(n,m,x,y):
    directions=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    count=0
    visited=[[False]*m for _ in range(n)]

    def dfs(x,y,step):
        if step==n*m:
            nonlocal count
            count+=1
            return
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny]=True
                dfs(nx,ny,step+1)
                visited[nx][ny]=False
    visited[x][y]=True
    dfs(x,y,1)
    return count
t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    print(horse(n,m,x,y))



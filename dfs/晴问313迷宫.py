def solve():
    n,m=map(int,input().split())
    puzzle=[]
    for _ in range(n):
        puzzle.append(list(map(int,input().split())))
    visited=[[False]*m for _ in range(n)]
    count=0
    directions=[(-1,0),(1,0),(0,1),(0,-1)]
    def dfs(x,y):
        nonlocal count
        if x==n-1 and y==m-1:
            count+=1
            return
        visited[x][y]=True
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if (0<=nx<n and 0<=ny<m and puzzle[nx][ny]==0 and not visited[nx][ny]):
                dfs(nx,ny)
        visited[x][y]=False
    if puzzle[0][0]==0:
        dfs(0,0)
    print(count)
solve()

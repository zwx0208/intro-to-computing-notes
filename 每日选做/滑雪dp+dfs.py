r,c=map(int,input().split())
slope=[list(map(int,input().split())) for _ in range(r)]
dp=[[0]*c for _ in range(r)]
def dfs(x,y):
    if dp[x][y]!=0:
        return dp[x][y]
    directions=[[0,1],[0,-1],[1,0],[-1,0]]
    ml=1
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<r and 0<=ny<c and slope[nx][ny]<slope[x][y]:
            ml=max(ml,dfs(nx,ny)+1)
    dp[x][y]=ml
    return ml
ans=0
for i in range(r):
    for j in range(c):
        l=dfs(i,j)   #这样只调用一次dfs
        if l>ans:
            ans=l
print(ans)


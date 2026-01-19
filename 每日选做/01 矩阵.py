#bfs解法
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        m,n=len(mat),len(mat[0])
        visit=[[-1]*n for _ in range(m)]
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    visit[i][j]=0
                    q.append((i,j))
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            x,y=q.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and visit[nx][ny]==-1:
                    visit[nx][ny]=visit[x][y]+1
                    q.append((nx,ny))
        return visit

#dp解法
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        INF=10**9
        dp = [[INF] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    dp[i][j]=0
                else:
                    if i>0:
                        dp[i][j]=min(dp[i][j],dp[i-1][j]+1)
                    if j>0:
                        dp[i][j]=min(dp[i][j],dp[i][j-1]+1)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i<m-1:
                    dp[i][j]=min(dp[i][j],dp[i+1][j]+1)
                if j<n-1:
                    dp[i][j]=min(dp[i][j],dp[i][j+1]+1)
        return dp
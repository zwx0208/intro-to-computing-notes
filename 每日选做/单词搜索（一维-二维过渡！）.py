class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        visited=[[False]*n for _ in range(m)]
        def dfs(x,y,idx):
            if idx==len(word):
                return True
            if x<0 or x>=m or y<0 or y>=n:
                return False
            if board[x][y]!=word[idx] or visited[x][y]:
                return False
            visited[x][y]=True
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if dfs(nx,ny,idx+1):
                    return True
            visited[x][y]=False
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False


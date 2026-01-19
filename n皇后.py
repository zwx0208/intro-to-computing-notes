class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        board=[['.' for _ in range(n)] for _ in range(n)]
        used_col=[False]*n
        used_main=[False]*(2*n-1)
        used_vice=[False]*(2*n-1)
        def dfs(row):
            if row==n:
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                main=row-col+n-1
                vice=row+col
                if used_col[col] or used_vice[vice] or used_main[main]:
                    continue
                board[row][col]='Q' #选择
                used_main[main],used_vice[vice],used_col[col]=True,True,True
                dfs(row+1)          #递归
                board[row][col]='.' #回溯
                used_main[main], used_vice[vice], used_col[col] =False,False,False
        dfs(0)
        return result

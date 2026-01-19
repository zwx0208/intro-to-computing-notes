#编辑距离指的是讲一个字符串变为另一个字符串的最小步数，可以用于表征两个字符串的相似程度
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        return dp[m][n]

'''  这是一个示意表格:
     ""  r  o  s
""   0   1  2  3
h    1   ?  ?  ?
o    2   ?  ?  ?
r    3   ?  ?  ?
s    4   ?  ?  ?
e    5   ?  ?  ?
'''
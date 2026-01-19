class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        wordDict=set(wordDict)   #转成集合比列表的查询快很多
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j]==True and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[n]


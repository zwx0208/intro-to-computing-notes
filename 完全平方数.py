class Solution:
    def numSquares(self, n: int) -> int:
        nums = [x**2 for x in range(1, 101)]
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for num in nums:
            for i in range(num,n+1):
                dp[i]=min(dp[i],dp[i-num]+1)
        return dp[n]
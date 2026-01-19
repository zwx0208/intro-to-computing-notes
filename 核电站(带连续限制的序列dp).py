n,m=map(int,input().split())
dp=[[0]*m for _ in range(n+1)]  #让索引和坑编号对齐  dp[i][j]表示前i个坑，最后连续放了j个核物质的方案数
dp[1][0]=dp[1][1]=1
for i in range(2,n+1):
    dp[i][0]=sum(dp[i-1])   #第i个没放，则它的值为第i-1个所有情况的和
    for j in range(m-1):    #j小于m-1时，第i个还能再放也不会爆炸，直接转移
        dp[i][j+1]=dp[i-1][j]
print(sum(dp[n]))


'''
这是一个实例表格
i/j	0 (最后没放)	1 (最后连续1个)	2 (最后连续2个)
 1       1	         1	            0
 2	     2	         1	            1
 3 	     4	         2	            1    
 4	     7	         4	            2
'''

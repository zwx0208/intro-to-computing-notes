'''0:不选人 1：选第一排 2：选第二排'''
n=int(input())
students1=list(map(int,input().split()))
students2=list(map(int,input().split()))
dp=[[0]*(n+1) for _ in range(3)]
dp[0][0]=dp[1][0]=dp[2][0]=0
for i in range(1,n+1):
    dp[0][i]=max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
    dp[1][i]=max(dp[0][i-1],dp[2][i-1])+students1[i-1]
    dp[2][i]=max(dp[0][i-1],dp[1][i-1])+students2[i-1]
ans=max(dp[0][n],dp[1][n],dp[2][n])
print(ans)

#滚动数组优化
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp0, dp1, dp2 = 0, 0, 0  # 前一列的状态
for i in range(n):
    new0 = max(dp0, dp1, dp2)
    new1 = max(dp0, dp2) + a[i]
    new2 = max(dp0, dp1) + b[i]
    dp0, dp1, dp2 = new0, new1, new2
print(max(dp0, dp1, dp2))
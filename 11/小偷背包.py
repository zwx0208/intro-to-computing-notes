def backpack(n,b,price,weight):
    dp=[[0]*(b+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,b+1):
            dp[i][j]=dp[i-1][j]
            if j>=weight[i-1]:
                dp[i][j]=max(dp[i][j],dp[i-1][j-weight[i-1]]+price[i-1])
    return dp[n][b]
n,b=map(int,input().split())
price=list(map(int,input().split()))
weight=list(map(int,input().split()))
print(backpack(n,b,price,weight))
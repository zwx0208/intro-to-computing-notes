mod=1000000007
dp=[0]*100001
dp[0]=1
sum_dp=[0]*100001
t,k=map(int,input().split())
for i in range(1,100001):
    dp[i]=dp[i-1]%mod
    if i>=k:
        dp[i]=(dp[i-1]+dp[i-k])%mod
    sum_dp[i]=(sum_dp[i-1]+dp[i])%mod
for _ in range(t):
    m,n=map(int,input().split())
    print((sum_dp[n]-sum_dp[m-1]+mod)%mod)

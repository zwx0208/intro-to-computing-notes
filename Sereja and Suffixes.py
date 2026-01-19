n,m=map(int,input().split())
group=list(map(int,input().split()))
a=[0]+group  #转为下标从1开始的列表
dp=[0]*(n+2)
seen=[False]*100001
for i in range(n,0,-1):
    if not seen[a[i]]:
        dp[i]=dp[i+1]+1
        seen[a[i]]=True
    else:
        dp[i]=dp[i+1]
for _ in range(m):
    idx=int(input())
    print(dp[idx])

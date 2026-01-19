'''0: 体育馆关门，没有比赛 → 只能休息
1: 体育馆关门，但有比赛 → 可以休息或比赛
2: 体育馆开门，没有比赛 → 可以休息或运动
3: 体育馆开门，有比赛 → 可以休息、比赛或运动

0:休息 1：比赛 2：运动
'''
n=int(input())
INF=10**9
gym=list(map(int,input().split()))
dp=[[INF]*3 for _ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    today=gym[i-1]
    dp[i][0]=min(dp[i-1][0],dp[i-1][1],dp[i-1][2])+1
    if today==1 or today==3:
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])
    if today==2 or today==3:
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])
ans=min(dp[n][0],dp[n][1],dp[n][2])
print(ans)


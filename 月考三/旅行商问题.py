n=int(input())
cost=[list(map(int,input().split())) for _ in range(n)]
INF=10**9
dp=[[INF]*n for _ in range(1<<n)] #1向左移动1位就是乘2，移动n位就是2^n
dp[1][0]=0 #从城市0出发
for mask in range(1 << n):
    for i in range(n):
        if dp[mask][i] == INF:
            continue
        if not (mask >> i & 1):  #i必须已访问，不然mask不成立
            continue
        for j in range(n):      #尝试访问j
            if mask >> j & 1:   #所以j不能已访问
                continue
            new_mask = mask | (1 << j)  #将j设为已访问
            new_cost = dp[mask][i] + cost[i][j]
            if new_cost < dp[new_mask][j]:  #用max()好像比较慢，改成if判断
                dp[new_mask][j] = new_cost
ans = INF
full_mask = (1 << n) - 1
for i in range(n):
    if dp[full_mask][i] != INF:
        total = dp[full_mask][i] + cost[i][0]    #回到起点0
        if total < ans:
            ans = total
print(ans)
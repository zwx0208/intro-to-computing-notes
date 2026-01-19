# 三状态带限制dp通用模板
dp=[[0]*(n+1) for _ in range(3)]
for i in range(1, n + 1):
    # 状态0：可以从任意前状态转移
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + cost0

    # 状态1：不能从状态1转移
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + cost1

    # 状态2：不能从状态2转移
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + cost2
#物品可无限使用
def complete_knapsack(V, weights, values):
    """完全背包求最大价值"""
    n = len(weights)
    dp = [0] * (V + 1)

    for i in range(n):
        w, v = weights[i], values[i]
        for j in range(w, V + 1):  # 关键：从小到大
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[V]

def min_coins(amount, coins):
    """完全背包求最少硬币数"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def combination_count(target, nums):
    """完全背包求组合数"""
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for i in range(num, target + 1):
            dp[i] += dp[i - num]     #一维滚动数组优化
    return dp[target]
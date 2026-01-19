n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
prev_dp = [1] * m
for i in range(1, n):
    curr_dp = [0] * m
    prefix_sum = 0  #前缀和，用于统计前一行到当前位置的dp值（只增不降）
    k = 0  # 指向前一行的指针
    for j in range(m):
        while k < m and matrix[i - 1][k] <= matrix[i][j]:
            prefix_sum += prev_dp[k]
            k += 1
        curr_dp[j] = prefix_sum
    prev_dp = curr_dp
print(sum(prev_dp))
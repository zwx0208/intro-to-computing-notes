n = int(input())
a = list(map(int, input().split()))
# 预处理：对于每个位置，记录从该位置开始能覆盖到的最远距离
right_most = [0] * (n + 2)  # 多开一点空间
for i in range(1, n + 1):
    ai = a[i - 1]
    left = max(1, i - ai)
    right = min(n, i + ai)
    # 在左端点记录从这个点出发能到达的最远位置
    right_most[left] = max(right_most[left], right)

ans = 0
cur = 0  # 当前已覆盖到的最右位置
nxt = 0  # 下一次能覆盖到的最远位置
for i in range(1, n + 1):
    # 更新从当前位置能到达的最远距离
    nxt = max(nxt, right_most[i])
    # 如果到达当前覆盖的边界
    if i > cur:
        ans += 1
        cur=nxt
print(ans)
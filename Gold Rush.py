t = int(input())
def dfs(n, m):
    if n == m:
        return True
    if n % 3 != 0:
        return False
    if m > 2 * n // 3:
        return dfs(n // 3, m)  #剪枝
    return dfs(n // 3, m) or dfs(2 * n // 3, m)

for _ in range(t):
    n, m = map(int, input().split())
    print("YES" if dfs(n, m) else "NO")

L, M = map(int, input().split())
intervals = []
for _ in range(M):
    m, n = map(int, input().split())
    if m > n:
        m, n = n, m
    intervals.append((m, n))
intervals.sort()

tree = []
for m, n in intervals:
    if not tree or m > tree[-1][1]:
        tree.append([m, n])
    else:
        tree[-1][1] = max(tree[-1][1], n)

cut = sum(n - m + 1 for m, n in tree)
remain = (L + 1) - cut
print(remain)
n, k = map(int, input().split())
nums = list(map(int, input().split()))
result = []
def backtrack(start, path):
    if len(path) == k:
        result.append(path[:])
        return
    for i in range(start, n):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
backtrack(0, [])
for comb in result:
    print(' '.join(map(str, comb)))
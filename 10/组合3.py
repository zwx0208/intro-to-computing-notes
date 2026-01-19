n, k = map(int, input().split())
nums = list(map(int, input().split()))
result=set()
def backtrack(start, path):
    if len(path) == k:
        result.add(tuple(path))
        return
    for i in range(start, n):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
backtrack(0, [])
for item in result:
    print(' '.join(map(str,item)))

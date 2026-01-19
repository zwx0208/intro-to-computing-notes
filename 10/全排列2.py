n=int(input())
nums=list(map(int,input().split()))
result=set()
def dfs(path,visited):
    if len(path)==n:
        result.add(tuple(path))
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            dfs(path+[nums[i]],visited)
            visited[i]=False
dfs([],[False]*n)
for j in sorted(result):
    print(' '.join(map(str,j)))
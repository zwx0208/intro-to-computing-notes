def greedy(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        steps += 1
    return steps
n=int(input())
print(greedy(n))


#bfs
from collections import deque
def bfs(n):
    queue=deque()
    queue.append((1,0))   #当前值，步数
    visited= {1}
    while queue:
        current,step=queue.popleft()
        for nxt in [current+1,current*2]:
            if nxt==n:
                return step+1
            if nxt not in visited and nxt<=n:
                visited.add(nxt)
                queue.append((nxt,step+1))
n=int(input())
print(bfs(n))


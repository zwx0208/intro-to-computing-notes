def find(n,m):
    monkeys=list(range(1,n+1))
    index=0
    while len(monkeys)>1:
        index=(index+m-1)%len(monkeys)
        monkeys.pop(index)
    return monkeys[0]
while True:
    n,m=map(int,input().split())
    if m==0 and n==0:
        break
    print(find(n,m))


#用deque实现
from collections import deque
def find(n, m):
    queue = deque(range(1, n + 1))
    while len(queue) > 1:
        for _ in range(m - 1):
            queue.append(queue.popleft())
        queue.popleft()
    return queue[0]
while True:
    n,m=map(int,input().split())
    if m==0 and n==0:
        break
    print(find(n,m))
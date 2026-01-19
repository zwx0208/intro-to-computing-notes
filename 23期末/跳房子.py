from collections import deque
def bfs(n,m):
    queue=deque()
    queue.append((n,''))   #当前位置，操作序列
    visited={n}
    while queue:
        pos,path=queue.popleft()
        if pos==m:
            return len(path),path
        npos=pos*3
        if npos not in visited:
            visited.add(npos)
            queue.append((npos,path+'H'))
        npos = pos //2
        if npos not in visited:
            visited.add(npos)
            queue.append((npos, path + 'O'))
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    l,p=bfs(n,m)
    print(l)
    print(p)
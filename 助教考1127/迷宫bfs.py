from collections import deque
k=int(input())
for i in range(k):
    n=int(input())
    puzzle=[]
    for _ in range(n):
        puzzle.append(list(input().strip()))
    ha,la,hb,lb=map(int,input().split())
    if puzzle[ha][la]=='#' or puzzle[hb][lb]=='#':
        print('NO')
        continue
    if ha==hb and la==lb:
        print('YES')
        continue
    visited=[[False]*n for _ in range(n)]
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    queue=deque()
    queue.append((ha,la))
    visited[ha][la]=True
    found=False
    while queue:
        x,y=queue.popleft()
        if x==hb and y==lb:
            found=True
            break
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and puzzle[nx][ny]=='.' and visited[nx][ny]==False:
                visited[nx][ny]=True
                queue.append((nx,ny))
    print('YES' if found else 'NO')
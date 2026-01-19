k=int(input())
for _ in range(k):
    n=int(input())
    task=[]
    for _ in range(n):
        task.append(list(map(int,input().split())))
    task.sort(key=lambda x:x[1])
    ans=0
    visited=[False]*n
    for i in range(n):
        if not visited[i]:
            t=task[i][1]
            ans+=1
            for j in range(n):
                if not visited[j] and task[j][0]<=t<=task[j][1]:
                    visited[j]=True
    print(ans)


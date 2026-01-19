k=int(input())
for _ in range(k):
    l,n=map(int,input().split())
    ants=list(map(int,input().split()))
    maxt=0
    mint=0
    for ant in ants:
        if ant>=l//2:
            maxt=max(ant,maxt)
            mint=max(l-ant,mint)
        else:
            maxt=max(l-ant,maxt)
            mint=max(ant,mint)
    print(f'{mint} {maxt}')
#蚂蚁撞一起，速度没变，相当于蚂蚁穿过了对方
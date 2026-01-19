count=False
n,q=map(int,input().split())
group=[]
for _ in range(q):
    group.append(list(map(int,input().split())))
for [i,j] in group:
    if [j,i] in group:
        print('Yes')
        count=True
        break
if not count:
    print('No')
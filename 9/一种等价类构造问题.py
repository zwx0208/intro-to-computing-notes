m,n,k=map(int,input().split(','))
bag={}
for i in range(m+1,n):
    sumnum=sum(int(n) for n in str(i))
    if sumnum%k==0:
        if sumnum not in bag:
            bag[sumnum]=[]
        bag[sumnum].append(i)
for sumnum in sorted(bag.keys()):
    sumnum=sorted(bag[sumnum])
    print(','.join(map(str,sumnum)))
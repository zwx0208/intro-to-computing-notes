n=int(input())
num=list(map(int,input().split()))
if n<2:
    print(n)
else:
    length=1
    pd=0
    for i in range(1,n):
        cd=num[i]-num[i-1]
        if (pd>=0 and cd<0)or(pd<=0 and cd>0):
            length+=1
            pd=cd
    print(length)
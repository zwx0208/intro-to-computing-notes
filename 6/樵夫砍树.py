n=int(input())
trees=[]
for _ in range(n):
    trees.append(list(map(int, input().split())))
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    count=2
    prev=trees[0][0]
    for i in range(1,n-1):
        x,h=trees[i]
        if x-h>prev:
            count+=1
            prev=x
        elif x+h<trees[i+1][0]:
            count+=1
            prev=x+h
        else:
            prev=x
    print(count)
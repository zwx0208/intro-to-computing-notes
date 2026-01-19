from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    count_list=defaultdict(int)
    for i in range(n):
          count_list[a[i]-i]+=1
    for item in count_list.values():
        if item>=2:
            count+=item*(item-1)//2
    print(count)

import bisect
n=int(input())
shops=list(map(int,input().split()))
shops.sort()
q=int(input())
for _ in range(q):
    m=int(input())
    print(bisect.bisect_right(shops,m))
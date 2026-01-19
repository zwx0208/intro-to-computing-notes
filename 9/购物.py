from bisect import bisect_right

def solve():
    X,N=map(int,input().split())
    coins=list(map(int,input().split()))
    coins.sort()
    if coins[0]>1:
        print(-1)
        return
    cover=0
    count=0
    while cover<X:
        target=cover+1
        idx=bisect_right(coins,target)-1
        if idx<0:
            print(-1)
            return
        cover+=coins[idx]
        count+=1
    print(count)
solve()
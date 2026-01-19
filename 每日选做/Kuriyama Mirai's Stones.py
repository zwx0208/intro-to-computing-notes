n=int(input())
stones=list(map(int,input().split()))
m=int(input())
dp1=[0]*(n+1)
for i in range(1,n+1):
    dp1[i]=dp1[i-1]+stones[i-1]
dp2=[0]*(n+1)
stones.sort()
for i in range(1,n+1):
    dp2[i]=dp2[i-1]+stones[i-1]
for _ in range(m):
    typ,l,r=map(int,input().split())
    if typ==1:
        print(dp1[r]-dp1[l-1])
    else:
        print(dp2[r] - dp2[l - 1])

n=int(input())
M=list(map(int,input().split()))
b,c=0,0
for i in range(n):
    c+=M[i]
    if c<=b:
        b=c
print(-b+1)
l=int(input())+1
n=int(input())
students=list(map(int,input().split()))
maxt=0
mint=0
for s in students:
    if s>=l/2:
        maxt=max(s,maxt)
        mint=max(l-s,mint)
    else:
        maxt=max(l-s,maxt)
        mint=max(s,mint)
print(f'{mint} {maxt}')
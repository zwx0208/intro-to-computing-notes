t=int(input())
for _ in range(t):
    n=int(input())
    s1=(1+n)*n//2
    i=1
    while n>1:
        n//=2
        i+=1
    s2=2**i-1
    print(s1-2*s2)
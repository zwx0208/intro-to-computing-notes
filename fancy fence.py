k=int(input())
for _ in range(k):
    m=int(input())
    n=360/(180-m)
    if n%1==0 and n>=3:
        print('YES')
    else:
        print('NO')

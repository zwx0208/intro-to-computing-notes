a,b,c=map(float,input().split())
delta=b**2-4*a*c
if a==0:
    if b==0 and c!=0:
        print(0)
    elif b!=0:
        print(1)
        print(f'{-c/b:.5f}')
    elif b==0 and c==0:
        print(-1)
else:
    if delta < 0:
        print(0)
    elif delta == 0:
        print(1)
        print((-b+delta**0.5)/(2*a))
    else:
        if a>0:
            print(2)
            print(f'{(-b - delta ** 0.5) / (2 * a):.5f}')
            print(f'{(-b + delta ** 0.5) / (2 * a):.5f}')
        else:
            print(2)
            print(f'{(-b + delta ** 0.5) / (2 * a):.5f}')
            print(f'{(-b - delta ** 0.5) / (2 * a):.5f}')
n=int(input())
for _ in range(n):
    a=int(input())
    if a==1 or a==2:
        print('0')
    elif a%2==0:
        print(a//2-1)
    else:
        print(a//2)
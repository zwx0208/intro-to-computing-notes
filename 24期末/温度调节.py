t = int(input())
for _ in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())

    if a == b:
        print(0)
    elif abs(a - b) >= x:
        print(1)
    elif (a - l < x and r - a < x) or (b - l < x and r - b < x):
        print(-1)
    elif (r - a >= x and r - b >= x) or (a - l >= x and b - l >= x):
        print(2)
    else:
        print(3)

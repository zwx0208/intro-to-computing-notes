'''t=int(input())
for _ in range(t):
    x=int(input())
    y=0
    while y>=0:
        y+=1
        xy=int(str(x)+str(y))
        if xy%(x+y)==0:
            print(y)
            break   （超时了）'''
t = int(input())
for _ in range(t):
    x = int(input())
    print(2 * x)
#因为 `y = 2x` 时，`x#y = x * 10^d + 2x`，`x + y = 3x`，而 `(10^d + 2)` 总是能被 3 整除。




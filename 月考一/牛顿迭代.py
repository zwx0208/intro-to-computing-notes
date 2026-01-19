import sys
for line in sys.stdin:
    a=float(line)
    x=1
    count=0
    while True:
        count+=1
        x1=0.5*(x+a/x)
        if abs(x1-x)<=1e-6:
            break
        x=x1
    print(f'{count} {x1:.2f}')
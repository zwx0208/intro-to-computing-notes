n = int(input())
def sum(x):
    if x==1:
        return 0
    total=1
    for i in range(2,int(x**0.5)+ 1):
        if x%i==0:
            total+=i
            if i!=x//i:
                total+=x//i
    return total
divisums={}
for i in range(2,n+1):
    divisums[i]=sum(i)
pairs=[]
for a in range(2,n+1):
    b=divisums[a]
    if b>a and divisums.get(b)==a:
        pairs.append((a,b))
for a,b in pairs:
    print(f"{a} {b}")
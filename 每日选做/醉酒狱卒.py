n=int(input())
for _ in range(n):
    p=int(input())
    count=-1
    for i in range(p+1):
        j=int(i**0.5)
        if j**2==i:
            count+=1
    print(count)

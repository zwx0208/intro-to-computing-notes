while True:
    c=float(input())
    if c==0:
        break
    n=1
    length=0
    while length<c:
        n+=1
        length+=1/n
    print(f"{n-1} card(s)")

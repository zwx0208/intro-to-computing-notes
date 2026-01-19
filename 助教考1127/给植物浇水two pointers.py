n,a,b=map(int,input().split())
plants=list(map(int,input().split()))
pointer1=0
pointer2=n-1
count=0
alice=a
bob=b
while pointer1<=pointer2:
    if plants[pointer1]<=alice:
        alice-=plants[pointer1]
        pointer1+=1
    else:
        alice=a
        count+=1
        alice-=plants[pointer1]
        pointer1+=1
    if plants[pointer2]<=bob:
        bob-=plants[pointer2]
        pointer2-=1
    else:
        bob=b
        count+=1
        bob-=plants[pointer2]
        pointer2-=1
    if pointer1==pointer2:
        if alice!=bob:
            now=max(alice,bob)
            if now>=plants[pointer1]:
                break
            else:
                count+=1
                break
        else:
            if plants[pointer1] <= alice:
                break
            else:
                count+=1
                break
print(count)
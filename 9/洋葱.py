n=int(input())
onion=[]
layer=(n+1)//2
maxsum=0
for i in range(n):
    onion.append(list(map(int,input().split())))
for k in range(layer):
    count=0
    for i in range(k,n-k):
        count+=onion[k][i]
    if k!=n-k-1:
        for i in range(k,n-k):
            count+=onion[n-k-1][i]
    for j in range(k+1,n-k-1):
        count+=onion[j][k]
    for j in range(k+1,n-k-1):
            count+=onion[j][n-k-1]
    if count>maxsum:
        maxsum=count
print(maxsum)


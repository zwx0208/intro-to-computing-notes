s,n=map(int,input().split())
dragons=[]
for _ in range(n):
    a,b=map(int,input().split())
    dragons.append([a,b])
    dragon=sorted(dragons)
conquer=True
for item in dragon:
    if s>item[0]:
        s+=item[1]
    else:
        conquer=False
        break
print('YES' if conquer else 'NO')

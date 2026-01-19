n=int(input())
queue=list(map(int,input().split()))
check=True
for i in range(1,n):
    if queue[i]<queue[i-1]:
        check=False
print('YES' if check==True else 'NO')

d=int(input())
n=int(input())
square=[[0]*1025 for _ in range(1025)]
for _ in range(n):
    x,y,k=map(int,input().split())
    for i in range(max(x-d,0),min(x+d+1,1025)):
        for j in range(max(y-d,0),min(y+d+1,1025)):
            square[i][j]+=k
count=0
update=0
for i in range(1025):
    for j in range(1025):
        if square[i][j]>update:
            update=int(square[i][j])
            count=1
        elif square[i][j]==update:
            count+=1
print(count,update)

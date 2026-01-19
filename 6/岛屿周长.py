m,n=map(int,input().split())
Map=[]
for _ in range(m):
    Map.append(list(map(int,input().split())))
count=0
for i in range(m):
    for j in range(n):
        if Map[i][j]==1:
            if i==0 or Map[i-1][j]==0:
                count+=1
            if j==0 or Map[i][j-1]==0:
                count+=1
            if i==m-1 or Map[i+1][j]==0:
                count+=1
            if j==n-1 or Map[i][j+1]==0:
                count+=1
print(count)

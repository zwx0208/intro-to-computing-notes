a,b,k=map(int,input().split())
matrix=[[0]*b for _ in range(a)]
count=0
for _ in range(k):
    R,S,p,t=map(int,input().split())
    r=p//2
    if t==1:
        count+=1
        for i in range(max(R-1-r,0),min(R+r,a)):
            for j in range(max(S-1-r,0),min(S+r,b)):
                matrix[i][j]+=1
    else:
        for i in range(max(R-1-r,0),min(R+r,a)):
            for j in range(max(S-1-r,0),min(S+r,b)):
                matrix[i][j]-=1
ans=0
for row in matrix:
    for item in row:
        if item==count:
            ans+=1
print(ans)

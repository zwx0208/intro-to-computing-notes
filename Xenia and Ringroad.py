n,m=map(int,input().split())
ringroad=list(map(int,input().split()))
way=ringroad[0]-1
for i in range(1,m):
    if ringroad[i]>=ringroad[i-1]:
        way+=ringroad[i]-ringroad[i-1]
    elif ringroad[i]<ringroad[i-1]:
        way+=n-ringroad[i-1]+ringroad[i]
print(way)
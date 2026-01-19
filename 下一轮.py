m,n=map(int,input().split())
grade=list(map(int,input().split()))
s=grade[n-1]
count=0
for i in range(m):
    if grade[i]>=s and grade[i]>0:
        count+=1
print(count)
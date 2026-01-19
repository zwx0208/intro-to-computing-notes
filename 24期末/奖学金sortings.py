n=int(input())
students=[]
for i in range(n):
    s=list(map(int,input().split()))
    summary=sum(s)
    stu=[s[0],s[1],s[2],i+1,summary]
    students.append(stu)
nstu=sorted(students,key=lambda x:(x[-1],x[0],-x[-2]),reverse=True)
for j in range(min(n,5)):
    print(nstu[j][-2],nstu[j][-1])



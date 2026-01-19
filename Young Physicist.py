n=int(input())

force_list=[0,0,0]
for i in range(n):
    force=list(map(int,input().split()))
    for j in range(3):
        force_list[j]+=force[j]
if force_list==[0,0,0]:
    print('YES')
else:
    print('NO')
#列表的问题，善用索引

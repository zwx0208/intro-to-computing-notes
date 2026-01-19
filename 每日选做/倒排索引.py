n=int(input())
files={}
for i in range(n):
    files[i+1]=list(input().split())
m=int(input())
for _ in range(m):
    target=input()
    idx_list=[]
    for idx in range(1,n+1):
        if target in files[idx]:
            idx_list.append(idx)
    if not idx_list:
        print('NOT FOUND')
    else:
        print(*idx_list)

#一次AC，实力无需多言
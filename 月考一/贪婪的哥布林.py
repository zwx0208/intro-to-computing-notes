N,M=map(int,input().split())
tval=0
remain=M
item=[]
for _ in range(N):
    v,w=map(int,input().split())
    val=v/w
    item.append((val,v,w))
item.sort(reverse=True)
for unit_val,total_v,total_w in item:
    if remain>=total_w:
        tval+=total_v
        remain-=total_w
    else:
        tval+=unit_val*remain
        break
print(f'{tval:.2f}')


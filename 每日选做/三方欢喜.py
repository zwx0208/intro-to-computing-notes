import sys
data=sys.stdin.read().split()
n=int(data[0])
q=int(data[1])
exist=[[False]*(n+1) for _ in range(n+1)]
output=False
idx=2
for _ in range(q):
    a=int(data[idx])
    b=int(data[idx+1])
    idx+=2
    exist[a][b]=True    #a喜欢b，那么现在只需检查有没有c满足，c喜欢a且b喜欢c
    for c in range(1,n+1):
        if c!=a and c!=b and exist[c][a]==True and exist[b][c]==True:
            output=True
            break
print('Yes' if output else 'No')
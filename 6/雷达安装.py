import math
def solve(n,d,island):
    ranges=[]
    for x,y in island:
        if y>d:
            return -1
        length=math.sqrt(d**2-y**2)
        ranges.append((x-length,x+length))
    ranges.sort(key=lambda i:i[1])
    count=1
    current=ranges[0][1]
    for start,end in ranges[1:]:
        if current<start:
            count+=1
            current=end
    return count
Case=0
while True:
    try:
        n,d=map(int,input().split())
    except:
        break
    if n==0 and d==0:
        break
    Case+=1
    island=[]
    for _ in range(n):
        island.append(tuple(map(int,input().split())))
    result=solve(n,d,island)
    print(f'Case {Case}: {result}')
    input()
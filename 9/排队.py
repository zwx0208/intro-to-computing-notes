N,D=map(int,input().split())
height=[0]*N
judge=[False]*N
for i in range(N):
    height[i]=int(input())
output=[]
while False in judge:
    i,r=0,len(height)
    now_list=[]
    while i<r:
        if judge[i]:
            i+=1
            continue
        if len(now_list)==0:
            now_list.append(height[i])
            maxh,minh=height[i],height[i]
            judge[i]=True
            continue
        maxh=max(height[i],maxh)
        minh=min(height[i],minh)
        if maxh-height[i]<=D and height[i]-minh<=D:
            now_list.append(height[i])
            judge[i]=True
        i+=1
    now_list.sort()
    output.extend(now_list)
print(*output,sep='\n')

import math
from math import floor
s=input()
n=len(s)
m=floor(math.log2(n))
l1,l2=[],[]
for i in range(m+1):
    l1.append(s[2**i-1])
l,r=0,m
while l<=r:
    if l==r:
        l2.append(l1[l])
        break
    l2.append(l1[l])
    l+=1
    l2.append(l1[r])
    r-=1
print(''.join(map(str,l2)))
